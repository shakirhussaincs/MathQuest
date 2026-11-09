from app.models.curriculum import Mission, Question
from app.services.curriculum_seed import seed_curriculum_and_badges

def test_module5_user_example_submitting_incorrect_4(client, student_token, test_student_user, db_session):
    """
    Module 5 Core Verification (Exact SRS / User Example):
    Question: Solve 3x + 5 = 20.
    If student enters 4:
    1. Identify answer as incorrect.
    2. Display correct answer: x = 5.
    3. Explain subtraction and division steps.
    4. Provide diagnostic mistake explanation.
    5. Allow student to practise similar questions (related practice recommendation).
    """
    seed_curriculum_and_badges(db_session)

    m1 = db_session.query(Mission).filter(Mission.title == "Linear Equation Challenge").first()
    q1 = db_session.query(Question).filter(
        Question.mission_id == m1.id,
        Question.prompt.contains("3x + 5 = 20")
    ).first()
    assert q1 is not None

    # Student enters 4 (incorrect answer)
    response = client.post(
        f"/api/v1/missions/{m1.id}/attempt",
        json={"question_id": q1.id, "submitted_answer": "4"},
        headers={"Authorization": f"Bearer {student_token}"}
    )
    assert response.status_code == 200
    data = response.json()

    # 1. Identified as incorrect
    assert data["is_correct"] is False
    assert data["xp_awarded"] == 0

    # 2. Correct answer displayed
    assert "5" in data["correct_answer"]

    # 3. Step-by-step subtraction and division steps explained
    steps = data["step_by_step_solution"]
    assert len(steps) >= 2
    full_steps_text = " ".join(steps).lower()
    assert "subtract" in full_steps_text or "subtraction" in full_steps_text
    assert "divide" in full_steps_text or "division" in full_steps_text

    # 4. Mistake explanation
    assert data["mistake_analysis"] is not None
    assert "4" in data["mistake_analysis"]

    # 5. Related practice recommendation
    assert data["related_practice"] is not None
    assert data["related_practice"]["mission_id"] == m1.id
    assert "practice" in data["related_practice"]["reason"].lower() or "similar" in data["related_practice"]["reason"].lower()

def test_module5_correct_answer_feedback(client, student_token, test_student_user, db_session):
    """Module 5: Correct answer verified, +10 XP awarded, full step-by-step solution provided."""
    seed_curriculum_and_badges(db_session)

    m1 = db_session.query(Mission).filter(Mission.title == "Linear Equation Challenge").first()
    q1 = db_session.query(Question).filter(
        Question.mission_id == m1.id,
        Question.prompt.contains("3x + 5 = 20")
    ).first()

    response = client.post(
        f"/api/v1/missions/{m1.id}/attempt",
        json={"question_id": q1.id, "submitted_answer": "B) 5"},
        headers={"Authorization": f"Bearer {student_token}"}
    )
    assert response.status_code == 200
    data = response.json()

    assert data["is_correct"] is True
    assert data["xp_awarded"] == 10
    assert len(data["step_by_step_solution"]) >= 2
    assert "Correct!" in data["message"]

