"""
Phase 5 — MissionSession Concurrency & Persistence Hardening Tests
===================================================================
9 test cases covering:
  - Duplicate active session prevention (partial unique index + IntegrityError path)
  - Independent question orders for different students
  - Session order persistence across page-refresh
  - New order issued after mission completion
  - HTTP 503 on DB read failure
  - HTTP 503 on DB write failure, no dangling session persisted
  - Single-question mission works correctly
  - Answer validation, XP, and completion still work end-to-end

NOTE ON ADVISORY LOCK COVERAGE
-------------------------------
Tests 2 and 3 run on SQLite (in-memory via conftest.py).
SQLite does not execute the pg_advisory_xact_lock() statement
(it is skipped in get_or_create_attempt_order when dialect != 'postgresql').
These tests therefore do NOT prove that the PostgreSQL advisory lock
prevents cross-instance first-question collisions — they only verify
that the Python-level logic produces the correct output for a single process.
To verify PostgreSQL advisory lock behaviour, deploy against a real
PostgreSQL instance and run concurrent load tests.
"""

import pytest
from unittest.mock import patch, MagicMock
from sqlalchemy.exc import IntegrityError as SQLAlchemyIntegrityError

from app.models.user import User, UserRole
from app.models.curriculum import (
    World, Topic, Mission, Question, MissionCategory, DifficultyLevel,
    MissionSession
)
from app.services.security import hash_password
from app.services.mission_service import get_or_create_attempt_order


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def _make_user(db, email, grade=10):
    u = User(
        email=email,
        display_name=email,
        password_hash=hash_password("ValidPassword123!"),
        role=UserRole.STUDENT,
        grade=grade,
        is_active=True,
    )
    db.add(u)
    db.commit()
    db.refresh(u)
    return u


def _get_token(client, email):
    res = client.post("/api/v1/auth/login", json={"email": email, "password": "ValidPassword123!"})
    assert res.status_code == 200, res.text
    return res.json()["access_token"]


def _seed_mission(db, grade=10, num_questions=3):
    """Creates a World → Topic → Mission → Questions chain and returns them."""
    w = World(title=f"HardeningWorld-{grade}-{num_questions}",
              description="Test", grade=grade, is_active=True)
    db.add(w)
    db.commit()

    t = Topic(world_id=w.id, title=f"TestTopic-{grade}", grade=grade)
    db.add(t)
    db.commit()

    m = Mission(
        topic_id=t.id,
        title=f"HardeningMission-{grade}-{num_questions}",
        instructions="Test mission",
        category=MissionCategory.PRACTICE.value,
        difficulty=DifficultyLevel.EASY.value,
        question_count=num_questions,
        xp_reward=20,
        pass_percentage=60,
        is_active=True,
    )
    db.add(m)
    db.commit()

    questions = []
    for i in range(1, num_questions + 1):
        q = Question(
            mission_id=m.id,
            prompt=f"Q{i}: What is {i} + {i}?",
            question_type="multiple_choice",
            options=[f"A) {i}", f"B) {i * 2}", f"C) {i * 3}", f"D) {i * 4}"],
            correct_answer=f"B) {i * 2}",
            explanation=f"{i} + {i} = {i * 2}",
            display_order=i,
            is_active=True,
        )
        db.add(q)
        questions.append(q)
    db.commit()
    for q in questions:
        db.refresh(q)
    db.refresh(m)
    return w, t, m, questions


# ---------------------------------------------------------------------------
# Test 1 — Same student double-request → only one active session
# ---------------------------------------------------------------------------

def test_1_duplicate_active_session_prevented(db_session):
    """
    Two consecutive calls to get_or_create_attempt_order() for the same
    (student, mission) must return a consistent order and must not create
    more than one active MissionSession row.

    This exercises:
      - The initial DB lookup returning None (creates new session).
      - The second call finding the existing active session and returning
        the same order without creating a duplicate.
    The partial unique index (uq_active_user_mission_session) enforces this
    at the database level; IntegrityError handling ensures graceful recovery.
    """
    u = _make_user(db_session, "dup_test@example.com")
    _, _, m, questions = _seed_mission(db_session, grade=10, num_questions=3)
    q_ids = [q.id for q in questions]

    order1 = get_or_create_attempt_order(db_session, u.id, m.id, q_ids)
    order2 = get_or_create_attempt_order(db_session, u.id, m.id, q_ids)

    assert set(order1) == set(q_ids), "First call must return all question IDs"
    assert order1 == order2, "Second call must return the SAME persisted order"

    active_sessions = db_session.query(MissionSession).filter(
        MissionSession.user_id == u.id,
        MissionSession.mission_id == m.id,
        MissionSession.is_active == True,
    ).all()
    assert len(active_sessions) == 1, (
        f"Expected exactly 1 active session, found {len(active_sessions)}"
    )


# ---------------------------------------------------------------------------
# Test 2 — Two students → (likely) different first questions
# ---------------------------------------------------------------------------

def test_2_different_students_get_independent_orders(db_session):
    """
    Two different students starting the same mission receive independently
    generated question sequences. When >= 2 questions exist, the Python-level
    logic actively avoids assigning the same first question as another
    currently active session.

    NOTE: This test runs on SQLite. The pg_advisory_xact_lock() statement
    is skipped because dialect != 'postgresql'. This does NOT prove
    PostgreSQL cross-instance coordination; see module docstring.
    """
    u1 = _make_user(db_session, "student_a@example.com")
    u2 = _make_user(db_session, "student_b@example.com")
    _, _, m, questions = _seed_mission(db_session, grade=10, num_questions=3)
    q_ids = [q.id for q in questions]

    # Student A starts first
    order_a = get_or_create_attempt_order(db_session, u1.id, m.id, q_ids)

    # Student B starts while A's session is active — should avoid A's first question
    order_b = get_or_create_attempt_order(db_session, u2.id, m.id, q_ids)

    assert set(order_a) == set(q_ids), "Student A must get all question IDs"
    assert set(order_b) == set(q_ids), "Student B must get all question IDs"

    # First questions should differ (this will occasionally collide with 2-question missions
    # but with 3 questions the avoidance logic makes different first IDs highly likely)
    # We assert the orders are not identical (permutation-level independence)
    # Accept same first ID only if it was unavoidable (all candidates taken)
    if order_a[0] == order_b[0]:
        # Only acceptable when every candidate first question was already taken
        # With 3 questions and 1 active session, there are always 2 free candidates
        pytest.fail(
            f"Both students received the same first question ID ({order_a[0]}). "
            "The avoidance logic did not function correctly on SQLite."
        )


# ---------------------------------------------------------------------------
# Test 3 — No _ACTIVE_SESSION_CACHE usage in service module
# ---------------------------------------------------------------------------

def test_3_no_in_memory_cache_in_service():
    """
    Verify that mission_service.py does NOT contain _ACTIVE_SESSION_CACHE.
    This confirms the unreliable in-memory fallback has been fully removed.
    The DB is now the sole source of truth.
    """
    import inspect
    import app.services.mission_service as svc
    source = inspect.getsource(svc)
    assert "_ACTIVE_SESSION_CACHE" not in source, (
        "Found _ACTIVE_SESSION_CACHE in mission_service.py — the in-memory "
        "fallback must be fully removed."
    )


# ---------------------------------------------------------------------------
# Test 4 — Refresh returns same persisted order (no re-randomization)
# ---------------------------------------------------------------------------

def test_4_refresh_returns_same_order(client, db_session):
    """
    Fetching /api/v1/missions/{id} twice for the same student while a session
    is active must return the identical question order both times.
    Re-randomization across page refreshes would corrupt the student's attempt.
    """
    u = _make_user(db_session, "refresh_student@example.com", grade=10)
    tok = _get_token(client, u.email)
    _, _, m, questions = _seed_mission(db_session, grade=10, num_questions=3)

    headers = {"Authorization": f"Bearer {tok}"}
    r1 = client.get(f"/api/v1/missions/{m.id}", headers=headers)
    assert r1.status_code == 200, r1.text
    ids1 = [q["id"] for q in r1.json()["questions"]]

    r2 = client.get(f"/api/v1/missions/{m.id}", headers=headers)
    assert r2.status_code == 200, r2.text
    ids2 = [q["id"] for q in r2.json()["questions"]]

    assert ids1 == ids2, (
        f"Question order changed between requests (refresh broke order).\n"
        f"First:  {ids1}\nSecond: {ids2}"
    )


# ---------------------------------------------------------------------------
# Test 5 — Complete → new session issues a fresh order
# ---------------------------------------------------------------------------

def test_5_completion_deactivates_session_and_allows_new_order(client, db_session):
    """
    After a student completes a mission, the active session must be marked
    is_active=False. A subsequent GET of the mission must create a new active
    session (possibly with a different order).
    """
    u = _make_user(db_session, "complete_student@example.com", grade=10)
    tok = _get_token(client, u.email)
    _, _, m, questions = _seed_mission(db_session, grade=10, num_questions=2)

    headers = {"Authorization": f"Bearer {tok}"}

    # 1. Start mission — creates active session
    r1 = client.get(f"/api/v1/missions/{m.id}", headers=headers)
    assert r1.status_code == 200, r1.text
    q_list = r1.json()["questions"]

    # 2. Submit all correct answers via /attempt
    for q in q_list:
        db_q = db_session.query(Question).filter(Question.id == q["id"]).first()
        res_att = client.post(
            f"/api/v1/missions/{m.id}/attempt",
            json={"question_id": q["id"], "submitted_answer": db_q.correct_answer},
            headers=headers,
        )
        assert res_att.status_code == 200, res_att.text

    # Finalize the mission
    res_complete = client.post(
        f"/api/v1/missions/{m.id}/complete",
        headers=headers,
    )
    assert res_complete.status_code == 200, res_complete.text

    # 3. After completion, the old session must be deactivated
    old_active = db_session.query(MissionSession).filter(
        MissionSession.user_id == u.id,
        MissionSession.mission_id == m.id,
        MissionSession.is_active == True,
    ).count()
    assert old_active == 0, "Active session was not deactivated after mission completion"

    # 4. A new GET should create a fresh session
    r2 = client.get(f"/api/v1/missions/{m.id}", headers=headers)
    assert r2.status_code == 200, r2.text

    new_active = db_session.query(MissionSession).filter(
        MissionSession.user_id == u.id,
        MissionSession.mission_id == m.id,
        MissionSession.is_active == True,
    ).count()
    assert new_active == 1, "New active session was not created after retry"


# ---------------------------------------------------------------------------
# Test 6 — DB read failure → HTTP 503
# ---------------------------------------------------------------------------

def test_6_db_read_failure_returns_503(client, db_session):
    """
    If the database is unavailable when reading active sessions,
    the endpoint must return HTTP 503 SERVICE_UNAVAILABLE.
    No silent fallback to an in-memory cache is permitted.
    """
    u = _make_user(db_session, "dbfail_student@example.com", grade=10)
    tok = _get_token(client, u.email)
    _, _, m, _ = _seed_mission(db_session, grade=10, num_questions=2)

    headers = {"Authorization": f"Bearer {tok}"}

    original_query = db_session.query

    def failing_query(*args, **kwargs):
        # Fail any query targeted at MissionSession
        if args and getattr(args[0], "__name__", "") == "MissionSession":
            raise Exception("Simulated DB connection failure")
        return original_query(*args, **kwargs)

    with patch.object(db_session, "query", side_effect=failing_query):
        r = client.get(f"/api/v1/missions/{m.id}", headers=headers)

    assert r.status_code == 503, (
        f"Expected 503 on DB read failure, got {r.status_code}: {r.text}"
    )
    assert "unavailable" in r.json().get("detail", "").lower(), (
        "Response detail must indicate service unavailability"
    )


# ---------------------------------------------------------------------------
# Test 7 — DB write failure → HTTP 503 and no dangling session
# ---------------------------------------------------------------------------

def test_7_db_write_failure_returns_503_no_dangling_session(client, db_session):
    """
    If db.commit() fails while writing a new MissionSession,
    the endpoint must return HTTP 503 and must NOT leave a dangling
    un-committed / half-written session that could block future attempts.
    """
    u = _make_user(db_session, "writefail_student@example.com", grade=10)
    tok = _get_token(client, u.email)
    _, _, m, _ = _seed_mission(db_session, grade=10, num_questions=2)

    headers = {"Authorization": f"Bearer {tok}"}

    original_commit = db_session.commit
    call_count = {"n": 0}

    def failing_commit():
        call_count["n"] += 1
        # Fail only the first commit (session creation), pass subsequent ones
        if call_count["n"] == 1:
            raise Exception("Simulated DB write failure")
        return original_commit()

    with patch.object(db_session, "commit", side_effect=failing_commit):
        r = client.get(f"/api/v1/missions/{m.id}", headers=headers)

    assert r.status_code == 503, (
        f"Expected 503 on DB write failure, got {r.status_code}: {r.text}"
    )

    # No active session should exist after a write failure
    active_count = db_session.query(MissionSession).filter(
        MissionSession.user_id == u.id,
        MissionSession.mission_id == m.id,
        MissionSession.is_active == True,
    ).count()
    assert active_count == 0, (
        f"Found {active_count} active session(s) after a simulated write failure — "
        "dangling session leak detected."
    )


# ---------------------------------------------------------------------------
# Test 8 — Single-question mission works correctly
# ---------------------------------------------------------------------------

def test_8_single_question_mission_works(client, db_session):
    """
    A mission with exactly 1 question must work without errors.
    get_or_create_attempt_order() short-circuits for single-question missions
    (no randomization needed, no session created) — the question is returned
    correctly and answer submission works.
    """
    u = _make_user(db_session, "single_q_student@example.com", grade=10)
    tok = _get_token(client, u.email)
    _, _, m, questions = _seed_mission(db_session, grade=10, num_questions=1)

    headers = {"Authorization": f"Bearer {tok}"}

    r = client.get(f"/api/v1/missions/{m.id}", headers=headers)
    assert r.status_code == 200, r.text
    data = r.json()
    assert len(data["questions"]) == 1, "Single-question mission must return exactly 1 question"
    assert data["questions"][0]["id"] == questions[0].id

    # Submit correct answer via /attempt
    res_att = client.post(
        f"/api/v1/missions/{m.id}/attempt",
        json={"question_id": questions[0].id, "submitted_answer": questions[0].correct_answer},
        headers=headers,
    )
    assert res_att.status_code == 200, res_att.text
    assert res_att.json()["is_correct"] is True

    # Complete mission
    res_complete = client.post(
        f"/api/v1/missions/{m.id}/complete",
        headers=headers,
    )
    assert res_complete.status_code == 200, res_complete.text
    result = res_complete.json()
    assert result["score"] == 1
    assert result["total_questions"] == 1
    assert result["is_passed"] is True


# ---------------------------------------------------------------------------
# Test 9 — Answer validation, XP, and completion unchanged
# ---------------------------------------------------------------------------

def test_9_xp_and_completion_work_correctly(client, db_session):
    """
    End-to-end: student completes mission with all correct answers.
    Verifies:
      - is_passed is True when all answers are correct
      - XP is awarded (total_mission_xp > 0)
      - badges_unlocked and score are present in response
      - accuracy_percentage is 100%
    """
    u = _make_user(db_session, "xp_student@example.com", grade=10)
    tok = _get_token(client, u.email)
    _, _, m, questions = _seed_mission(db_session, grade=10, num_questions=3)

    headers = {"Authorization": f"Bearer {tok}"}

    # Fetch mission to establish question order
    r = client.get(f"/api/v1/missions/{m.id}", headers=headers)
    assert r.status_code == 200, r.text
    q_list = r.json()["questions"]

    # Submit correct answer for each question in the returned order
    for q in q_list:
        db_q = db_session.query(Question).filter(Question.id == q["id"]).first()
        res_att = client.post(
            f"/api/v1/missions/{m.id}/attempt",
            json={"question_id": q["id"], "submitted_answer": db_q.correct_answer},
            headers=headers,
        )
        assert res_att.status_code == 200, res_att.text
        assert res_att.json()["is_correct"] is True

    # Complete the mission
    res = client.post(
        f"/api/v1/missions/{m.id}/complete",
        headers=headers,
    )
    assert res.status_code == 200, res.text
    result = res.json()

    assert result["score"] == 3, f"Expected score 3, got {result['score']}"
    assert result["total_questions"] == 3
    assert result["is_passed"] is True, "Mission should be passed with 100% correct answers"
    assert result["accuracy_percentage"] == 100.0
    assert result["total_mission_xp"] > 0, "XP must be awarded for a passed mission"
    assert "badges_unlocked" in result
    assert "new_total_xp" in result
    assert "new_level" in result
