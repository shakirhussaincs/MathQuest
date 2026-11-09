from datetime import datetime, date, timedelta, timezone
from app.models.user import User, UserRole
from app.models.curriculum import Topic, Mission, Question, Attempt
from app.models.gamification import RewardLedger, UserStreak
from app.services.curriculum_seed import seed_curriculum_and_badges
from app.services.security import hash_password

def test_daily_streak_tracking_and_bonus_xp(client, student_token, test_student_user, db_session):
    """FR-34: Daily streak claims award +5 XP idempotently without double-claims on same day."""
    # 1. First claim today
    claim1 = client.post("/api/v1/gamification/streak/claim", headers={"Authorization": f"Bearer {student_token}"})
    assert claim1.status_code == 200
    data1 = claim1.json()
    assert data1["current_streak"] == 1
    assert data1["xp_awarded"] == 5

    # 2. Second claim today (Idempotent)
    claim2 = client.post("/api/v1/gamification/streak/claim", headers={"Authorization": f"Bearer {student_token}"})
    assert claim2.status_code == 200
    data2 = claim2.json()
    assert data2["current_streak"] == 1
    assert data2["xp_awarded"] == 0
    assert "already logged" in data2["message"]

def test_leaderboard_privacy_and_ranking(client, student_token, test_student_user, db_session):
    """FR-43, FR-44, FR-45, NFR-08: Leaderboard ranks by XP, handles ties, and never exposes emails."""
    # Create another student with equal XP to test ties
    peer_student = User(
        email="peer@mathquest.edu",
        display_name="Sara Peer",
        password_hash=hash_password("Pass123!"),
        role=UserRole.STUDENT,
        grade=11,
        is_active=True
    )
    db_session.add(peer_student)
    db_session.commit()

    # Award 50 XP to both
    db_session.add_all([
        RewardLedger(user_id=test_student_user.id, event_type="test", reference_id="t1", xp_delta=50),
        RewardLedger(user_id=peer_student.id, event_type="test", reference_id="t2", xp_delta=50)
    ])
    db_session.commit()

    resp = client.get("/api/v1/gamification/leaderboard", headers={"Authorization": f"Bearer {student_token}"})
    assert resp.status_code == 200
    board = resp.json()
    assert len(board) >= 2

    for entry in board:
        # FR-44, NFR-08: Privacy check
        assert "email" not in entry
        assert "password" not in entry
        assert "display_name" in entry
        assert "total_xp" in entry

    # FR-45: Tie check - both with 50 XP have equal rank (rank 1)
    tied_entries = [e for e in board if e["total_xp"] == 50]
    assert len(tied_entries) == 2
    assert tied_entries[0]["rank"] == tied_entries[1]["rank"]

def test_leaderboard_grade_filter(client, student_token, test_student_user, db_session):
    """FR-46: Leaderboard filterable by Grade 11 or Grade 12."""
    g12_student = User(
        email="g12@mathquest.edu",
        display_name="Calculus Ace",
        password_hash=hash_password("Pass123!"),
        role=UserRole.STUDENT,
        grade=12,
        is_active=True
    )
    db_session.add(g12_student)
    db_session.commit()

    # Query Grade 11
    resp11 = client.get("/api/v1/gamification/leaderboard?grade=11", headers={"Authorization": f"Bearer {student_token}"})
    assert resp11.status_code == 200
    for e in resp11.json():
        assert e["grade"] == 11

    # Query Grade 12
    resp12 = client.get("/api/v1/gamification/leaderboard?grade=12", headers={"Authorization": f"Bearer {student_token}"})
    assert resp12.status_code == 200
    for e in resp12.json():
        assert e["grade"] == 12

def test_adaptive_difficulty_recommendation(client, student_token, test_student_user, db_session):
    """FR-40, FR-41, FR-42: Rule-based difficulty recommendation adjusts based on rolling accuracy."""
    seed_curriculum_and_badges(db_session)

    topic = db_session.query(Topic).first()

    # 1. Baseline (< 3 attempts) -> easy
    rec1 = client.get(f"/api/v1/gamification/adaptive/{topic.id}", headers={"Authorization": f"Bearer {student_token}"})
    assert rec1.status_code == 200
    assert rec1.json()["recommended_difficulty"] == "easy"

    # 2. Add 4 correct attempts (100% accuracy) -> hard
    mission = db_session.query(Mission).filter(Mission.topic_id == topic.id).first()
    q = db_session.query(Question).filter(Question.mission_id == mission.id).first()
    for _ in range(4):
        db_session.add(Attempt(
            user_id=test_student_user.id,
            question_id=q.id,
            submitted_answer=q.correct_answer,
            is_correct=True,
            attempted_at=datetime.now(timezone.utc)
        ))
    db_session.commit()

    rec2 = client.get(f"/api/v1/gamification/adaptive/{topic.id}", headers={"Authorization": f"Bearer {student_token}"})
    assert rec2.status_code == 200
    assert rec2.json()["recommended_difficulty"] == "hard"
    assert "High proficiency" in rec2.json()["explanation"]

