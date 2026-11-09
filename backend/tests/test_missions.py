from app.models.curriculum import World, Topic, Mission, Question, MissionProgress
from app.services.curriculum_seed import seed_curriculum_and_badges

def test_linear_equations_mission_structure(client, student_token, db_session):
    """Module 4: Linear Equations mission has 5 questions with MCQ and Numeric types."""
    seed_curriculum_and_badges(db_session)

    m1 = db_session.query(Mission).filter(Mission.title == "Linear Equation Challenge").first()
    assert m1 is not None
    assert m1.question_count == 5

    questions = db_session.query(Question).filter(Question.mission_id == m1.id).all()
    assert len(questions) == 5

    types = [q.question_type for q in questions]
    assert "multiple_choice" in types
    assert "numeric" in types

def test_numeric_answer_submission_and_tolerance(client, student_token, db_session):
    """FR-15: Numeric-answer questions accept floats and integers within tolerance."""
    seed_curriculum_and_badges(db_session)

    m1 = db_session.query(Mission).filter(Mission.title == "Linear Equation Challenge").first()
    numeric_q = db_session.query(Question).filter(
        Question.mission_id == m1.id,
        Question.question_type == "numeric"
    ).first()
    assert numeric_q is not None  # correct answer is "6"

    # 1. Correct integer submission
    resp1 = client.post(
        f"/api/v1/missions/{m1.id}/attempt",
        json={"question_id": numeric_q.id, "submitted_answer": "6"},
        headers={"Authorization": f"Bearer {student_token}"}
    )
    assert resp1.status_code == 200
    assert resp1.json()["is_correct"] is True

    # 2. Correct float representation (6.0 within tolerance)
    resp2 = client.post(
        f"/api/v1/missions/{m1.id}/attempt",
        json={"question_id": numeric_q.id, "submitted_answer": "6.00"},
        headers={"Authorization": f"Bearer {student_token}"}
    )
    assert resp2.status_code == 200
    assert resp2.json()["is_correct"] is True

    # 3. Incorrect numeric submission
    resp3 = client.post(
        f"/api/v1/missions/{m1.id}/attempt",
        json={"question_id": numeric_q.id, "submitted_answer": "10"},
        headers={"Authorization": f"Bearer {student_token}"}
    )
    assert resp3.status_code == 200
    assert resp3.json()["is_correct"] is False
    assert "explanation" in resp3.json()

def test_mission_unlocking_progression(client, student_token, test_student_user, db_session):
    """FR-10, FR-36, FR-38: Mission 2 is locked until Mission 1 is completed with pass score."""
    seed_curriculum_and_badges(db_session)

    m1 = db_session.query(Mission).filter(Mission.title == "Linear Equation Challenge").first()
    m2 = db_session.query(Mission).filter(Mission.title == "Determinant Inversion Mastery").first()

    # 1. Inspect m2 before completing m1 - should be locked
    m2_resp = client.get(f"/api/v1/missions/{m2.id}", headers={"Authorization": f"Bearer {student_token}"})
    assert m2_resp.status_code == 200
    assert m2_resp.json()["is_unlocked"] is False
    assert "Requires completing" in m2_resp.json()["unlock_explanation"]

    # Attempting to submit to locked m2 should be rejected with 403
    q_m2 = db_session.query(Question).filter(Question.mission_id == m2.id).first()
    attempt_blocked = client.post(
        f"/api/v1/missions/{m2.id}/attempt",
        json={"question_id": q_m2.id, "submitted_answer": "5"},
        headers={"Authorization": f"Bearer {student_token}"}
    )
    assert attempt_blocked.status_code == 403

    # 2. Complete m1 with passing score (at least 60%)
    m1_questions = db_session.query(Question).filter(Question.mission_id == m1.id).all()
    for q in m1_questions:
        client.post(
            f"/api/v1/missions/{m1.id}/attempt",
            json={"question_id": q.id, "submitted_answer": q.correct_answer},
            headers={"Authorization": f"Bearer {student_token}"}
        )

    complete_m1 = client.post(
        f"/api/v1/missions/{m1.id}/complete",
        headers={"Authorization": f"Bearer {student_token}"}
    )
    assert complete_m1.status_code == 200
    assert complete_m1.json()["is_passed"] is True

    # 3. Now m2 should be unlocked!
    m2_unlocked = client.get(f"/api/v1/missions/{m2.id}", headers={"Authorization": f"Bearer {student_token}"})
    assert m2_unlocked.status_code == 200
    assert m2_unlocked.json()["is_unlocked"] is True

def test_mission_retry_functionality(client, student_token, test_student_user, db_session):
    """FR-39: Student can retry a mission; retry increments attempt count and updates score."""
    seed_curriculum_and_badges(db_session)

    m1 = db_session.query(Mission).filter(Mission.title == "Linear Equation Challenge").first()
    questions = db_session.query(Question).filter(Question.mission_id == m1.id).all()

    # First Run: Answer 3 correctly and 2 incorrectly (60%)
    for idx, q in enumerate(questions):
        ans = q.correct_answer if idx < 3 else "Wrong Answer"
        client.post(
            f"/api/v1/missions/{m1.id}/attempt",
            json={"question_id": q.id, "submitted_answer": ans},
            headers={"Authorization": f"Bearer {student_token}"}
        )
    run1 = client.post(f"/api/v1/missions/{m1.id}/complete", headers={"Authorization": f"Bearer {student_token}"})
    assert run1.status_code == 200
    assert run1.json()["score"] == 3
    assert run1.json()["accuracy_percentage"] == 60.0

    # Second Run (Retry): Answer all 5 correctly (100%)
    for q in questions:
        client.post(
            f"/api/v1/missions/{m1.id}/attempt",
            json={"question_id": q.id, "submitted_answer": q.correct_answer},
            headers={"Authorization": f"Bearer {student_token}"}
        )
    run2 = client.post(f"/api/v1/missions/{m1.id}/complete", headers={"Authorization": f"Bearer {student_token}"})
    assert run2.status_code == 200
    assert run2.json()["score"] == 5
    assert run2.json()["accuracy_percentage"] == 100.0

    # Check progress record in database: attempts_count should be 2
    prog = db_session.query(MissionProgress).filter(
        MissionProgress.user_id == test_student_user.id,
        MissionProgress.mission_id == m1.id
    ).first()
    assert prog.attempts_count == 2
    assert prog.score == 5

