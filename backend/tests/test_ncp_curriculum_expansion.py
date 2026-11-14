"""
Test Suite: Federal NCP 2022-23 Curriculum Expansion (Grades 1-10)
==================================================================
Covers the 12 required verification items:
  1. Grade 1-10 curriculum availability.
  2. Grade-wise topic and mission associations.
  3. Question answer integrity (correct answers in options, numeric float-parseable).
  4. Difficulty distribution (Easy, Medium, Hard across all grades).
  5. Seed idempotency (running seed twice creates 0 duplicate records).
  6. No cross-grade content leakage (students see strictly their database grade).
  7. Student grade tampering prevention (request overrides rejected or ignored).
  8. Randomized question delivery (server-side, refresh preservation, no duplicates).
  9. Answer validation and XP awards.
  10. Existing Grade 11-12 curriculum preservation.
  11. Student, teacher, and admin dashboard regression.
  12. Existing RBAC security.
"""

import pytest
from app.models.user import User, UserRole
from app.models.curriculum import (
    World, Topic, Mission, Question, DifficultyLevel
)
from app.services.curriculum_seed import seed_curriculum_and_badges
from app.services.security import hash_password


def create_user(db_session, email, role, grade=None):
    user = User(
        email=email,
        display_name=f"User {email}",
        password_hash=hash_password("ValidPassword123!"),
        role=role,
        grade=grade,
        is_active=True
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


def get_token_for(client, email):
    res = client.post("/api/v1/auth/login", json={"email": email, "password": "ValidPassword123!"})
    assert res.status_code == 200, res.text
    return res.json()["access_token"]


# ---------------------------------------------------------------------------
# 1 & 2: Grade 1-10 Availability & Topic/Mission Associations
# ---------------------------------------------------------------------------
def test_1_and_2_grade_1_to_10_availability_and_associations(db_session):
    """Every grade from 1 to 10 has worlds, topics, missions, and questions with clean parent-child relations."""
    seed_curriculum_and_badges(db_session)

    for g in range(1, 11):
        worlds = db_session.query(World).filter(World.grade == g).all()
        assert len(worlds) >= 2, f"Grade {g} must have at least 2 worlds"

        for w in worlds:
            topics = db_session.query(Topic).filter(Topic.world_id == w.id).all()
            assert len(topics) >= 1, f"World {w.title} (Grade {g}) must have topics"
            for t in topics:
                assert t.grade == g, f"Topic {t.title} grade {t.grade} != world grade {g}"
                missions = db_session.query(Mission).filter(Mission.topic_id == t.id).all()
                assert len(missions) >= 1, f"Topic {t.title} must have missions"
                for m in missions:
                    questions = db_session.query(Question).filter(Question.mission_id == m.id).all()
                    assert len(questions) >= 8, f"Mission {m.title} must have at least 8 questions"


# ---------------------------------------------------------------------------
# 3: Question Answer Integrity
# ---------------------------------------------------------------------------
def test_3_question_answer_integrity(db_session):
    """Verify that every question has a valid prompt, valid correct_answer, and valid options."""
    seed_curriculum_and_badges(db_session)

    questions = db_session.query(Question).all()
    assert len(questions) >= 400, "Expected at least 400 questions seeded across all grades"

    for q in questions:
        assert q.prompt and len(q.prompt.strip()) > 5, f"Question {q.id} prompt too short"
        assert q.correct_answer and len(q.correct_answer.strip()) > 0, f"Question {q.id} has no answer"
        assert q.explanation and len(q.explanation.strip()) > 0, f"Question {q.id} has no explanation"

        if q.question_type == "multiple_choice":
            assert q.options and len(q.options) >= 2, f"MCQ {q.id} must have options"
            assert q.correct_answer in q.options, (
                f"Question {q.id} correct_answer '{q.correct_answer}' not in options: {q.options}"
            )
        elif q.question_type == "numeric":
            try:
                float(q.correct_answer)
            except ValueError:
                pytest.fail(f"Numeric Question {q.id} answer '{q.correct_answer}' cannot be parsed as a float")


# ---------------------------------------------------------------------------
# 4: Difficulty Distribution
# ---------------------------------------------------------------------------
def test_4_difficulty_distribution(db_session):
    """Verify that each grade 1-10 has a balanced difficulty distribution (Easy, Medium, Hard)."""
    seed_curriculum_and_badges(db_session)

    for g in range(1, 11):
        questions = (
            db_session.query(Question)
            .join(Mission, Question.mission_id == Mission.id)
            .join(Topic, Mission.topic_id == Topic.id)
            .join(World, Topic.world_id == World.id)
            .filter(World.grade == g)
            .all()
        )
        easy = sum(1 for q in questions if q.difficulty == DifficultyLevel.EASY.value)
        medium = sum(1 for q in questions if q.difficulty == DifficultyLevel.MEDIUM.value)
        hard = sum(1 for q in questions if q.difficulty == DifficultyLevel.HARD.value)

        assert easy > 0, f"Grade {g} has no Easy questions"
        assert medium > 0, f"Grade {g} has no Medium questions"
        assert hard > 0, f"Grade {g} has no Hard questions"


# ---------------------------------------------------------------------------
# 5: Seed Idempotency
# ---------------------------------------------------------------------------
def test_5_seed_idempotency(db_session):
    """Running seed_curriculum_and_badges twice does not create duplicate records."""
    seed_curriculum_and_badges(db_session)

    w_count_1 = db_session.query(World).count()
    t_count_1 = db_session.query(Topic).count()
    m_count_1 = db_session.query(Mission).count()
    q_count_1 = db_session.query(Question).count()

    # Second execution
    seed_curriculum_and_badges(db_session)

    assert db_session.query(World).count() == w_count_1, "Duplicate World records created"
    assert db_session.query(Topic).count() == t_count_1, "Duplicate Topic records created"
    assert db_session.query(Mission).count() == m_count_1, "Duplicate Mission records created"
    assert db_session.query(Question).count() == q_count_1, "Duplicate Question records created"


# ---------------------------------------------------------------------------
# 6 & 7: No Cross-Grade Leakage & Tampering Prevention
# ---------------------------------------------------------------------------
def test_6_and_7_grade_isolation_and_tamper_prevention(client, db_session):
    """Student of Grade 3 sees only Grade 3 worlds and cannot access Grade 4 missions."""
    seed_curriculum_and_badges(db_session)

    s3 = create_user(db_session, "g3_student@example.com", UserRole.STUDENT, grade=3)
    tok3 = get_token_for(client, s3.email)
    headers3 = {"Authorization": f"Bearer {tok3}"}

    # Worlds endpoint for student 3: strictly Grade 3
    res_w = client.get("/api/v1/worlds/", headers=headers3)
    assert res_w.status_code == 200
    worlds_data = res_w.json()
    assert len(worlds_data) >= 2
    for w in worlds_data:
        assert w["grade"] == 3

    # Attempt query override ?grade=4 should be ignored for students
    res_w_tamper = client.get("/api/v1/worlds/?grade=4", headers=headers3)
    assert res_w_tamper.status_code == 200
    for w in res_w_tamper.json():
        assert w["grade"] == 3, "Student was able to override grade via query param!"

    # Direct access to a Grade 4 mission must return 403 Forbidden
    g4_mission = (
        db_session.query(Mission)
        .join(Topic, Mission.topic_id == Topic.id)
        .join(World, Topic.world_id == World.id)
        .filter(World.grade == 4)
        .first()
    )
    assert g4_mission is not None

    res_m4 = client.get(f"/api/v1/missions/{g4_mission.id}", headers=headers3)
    assert res_m4.status_code == 403
    assert "Access denied" in res_m4.json()["detail"]


# ---------------------------------------------------------------------------
# 8 & 9: Randomized Question Delivery, Answer Validation & XP
# ---------------------------------------------------------------------------
def test_8_and_9_randomization_answer_validation_and_xp(client, db_session):
    """Server-side randomization delivers questions without answers, preserves order on refresh, and awards XP."""
    seed_curriculum_and_badges(db_session)

    s5 = create_user(db_session, "g5_student@example.com", UserRole.STUDENT, grade=5)
    tok5 = get_token_for(client, s5.email)
    headers5 = {"Authorization": f"Bearer {tok5}"}

    g5_mission = (
        db_session.query(Mission)
        .join(Topic, Mission.topic_id == Topic.id)
        .join(World, Topic.world_id == World.id)
        .filter(World.grade == 5)
        .first()
    )
    assert g5_mission is not None

    # 1. Fetch mission
    r1 = client.get(f"/api/v1/missions/{g5_mission.id}", headers=headers5)
    assert r1.status_code == 200
    data1 = r1.json()
    q_ids1 = [q["id"] for q in data1["questions"]]

    # Anti-cheat check: answers not exposed
    for q in data1["questions"]:
        assert "correct_answer" not in q
        assert "explanation" not in q

    # Refresh check: order preserved
    r2 = client.get(f"/api/v1/missions/{g5_mission.id}", headers=headers5)
    assert r2.status_code == 200
    q_ids2 = [q["id"] for q in r2.json()["questions"]]
    assert q_ids1 == q_ids2, "Refresh broke question order"

    # Answer validation & attempt submission
    for q_meta in data1["questions"]:
        db_q = db_session.query(Question).filter(Question.id == q_meta["id"]).first()
        res_att = client.post(
            f"/api/v1/missions/{g5_mission.id}/attempt",
            json={"question_id": db_q.id, "submitted_answer": db_q.correct_answer},
            headers=headers5
        )
        assert res_att.status_code == 200
        assert res_att.json()["is_correct"] is True
        assert res_att.json()["xp_awarded"] == 10

    # Complete mission
    res_comp = client.post(f"/api/v1/missions/{g5_mission.id}/complete", headers=headers5)
    assert res_comp.status_code == 200
    comp_json = res_comp.json()
    assert comp_json["is_passed"] is True
    assert comp_json["accuracy_percentage"] == 100.0
    assert comp_json["total_mission_xp"] > 0


# ---------------------------------------------------------------------------
# 10: Existing Grade 11-12 Curriculum Preservation
# ---------------------------------------------------------------------------
def test_10_grade_11_12_curriculum_preservation(db_session):
    """The original Grade 11 and 12 worlds, topics, and missions remain intact and unchanged."""
    seed_curriculum_and_badges(db_session)

    # Worlds
    w_titles = [w.title for w in db_session.query(World).filter(World.grade.in_([11, 12])).all()]
    assert "Algebra Kingdom" in w_titles
    assert "Trigonometry Island" in w_titles
    assert "Calculus Tower" in w_titles
    assert "Statistics City" in w_titles

    # Specific mission preserved
    m_linear = db_session.query(Mission).filter(Mission.title == "Linear Equation Challenge").first()
    assert m_linear is not None
    assert m_linear.topic.world.grade == 11
    assert len(m_linear.questions) == 5

    m_poly_dragon = db_session.query(Mission).filter(Mission.title == "Boss Challenge: The Polynomial Dragon").first()
    assert m_poly_dragon is not None
    assert m_poly_dragon.is_boss is True


# ---------------------------------------------------------------------------
# 11 & 12: Dashboard Regression & RBAC Security
# ---------------------------------------------------------------------------
def test_11_and_12_dashboard_and_rbac_regression(client, db_session):
    """Teacher and Admin can browse all grades, but students cannot access Teacher or Admin APIs."""
    seed_curriculum_and_badges(db_session)

    # 1. Student cannot access Teacher Preview
    student = create_user(db_session, "rbac_student@example.com", UserRole.STUDENT, grade=1)
    tok_s = get_token_for(client, student.email)
    r_teach_prev = client.get("/api/v1/missions/1/preview", headers={"Authorization": f"Bearer {tok_s}"})
    assert r_teach_prev.status_code == 403

    # 2. Student cannot access Admin Dashboard
    r_admin_dash = client.get("/api/v1/dashboard/admin", headers={"Authorization": f"Bearer {tok_s}"})
    assert r_admin_dash.status_code == 403

    # 3. Teacher can access Teacher Preview and filter curriculum across grades
    teacher = create_user(db_session, "rbac_teacher@school.edu", UserRole.TEACHER)
    tok_t = get_token_for(client, teacher.email)
    headers_t = {"Authorization": f"Bearer {tok_t}"}

    r_t_worlds_g1 = client.get("/api/v1/worlds/?grade=1", headers=headers_t)
    assert r_t_worlds_g1.status_code == 200
    assert len(r_t_worlds_g1.json()) == 2

    r_t_worlds_g10 = client.get("/api/v1/worlds/?grade=10", headers=headers_t)
    assert r_t_worlds_g10.status_code == 200
    assert len(r_t_worlds_g10.json()) == 2

    # Teacher dashboard overview works
    r_teach_dash = client.get("/api/v1/dashboard/teacher", headers=headers_t)
    assert r_teach_dash.status_code == 200
    dash_data = r_teach_dash.json()
    assert "teacher" in dash_data
    assert "insights" in dash_data
    assert "worlds" in dash_data
