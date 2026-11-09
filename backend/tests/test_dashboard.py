from datetime import datetime, timezone
from app.models.curriculum import World, Topic, Mission, MissionProgress, Attempt, MissionStatus
from app.models.gamification import RewardLedger, Badge, UserBadge
from app.services.curriculum_seed import seed_curriculum_and_badges

def test_student_dashboard_initial_state(client, student_token, test_student_user, db_session):
    """Module 2: Dashboard returns welcome profile, Level 1, 0 XP, worlds, and badges."""
    seed_curriculum_and_badges(db_session)

    response = client.get(
        "/api/v1/dashboard/student",
        headers={"Authorization": f"Bearer {student_token}"}
    )
    assert response.status_code == 200
    data = response.json()

    # 1. Welcome screen and profile
    profile = data["student_profile"]
    assert profile["display_name"] == test_student_user.display_name
    assert profile["grade"] == 11
    assert profile["avatar"] is not None

    # 2. Current player level & Total XP
    gamification = data["gamification"]
    assert gamification["level"] == 1
    assert gamification["current_xp"] == 0
    assert gamification["next_level_xp"] == 100
    assert gamification["rank_title"] == "Novice Numeromancer"

    # 3. Learning progress
    progress = data["learning_progress"]
    assert progress["total_missions"] > 0
    assert progress["completed_missions"] == 0
    assert progress["completion_percentage"] == 0.0

    # 4. Available mathematics worlds (Grade 11)
    worlds = data["worlds"]
    assert len(worlds) >= 2
    world_titles = [w["title"] for w in worlds]
    assert "Algebra Kingdom" in world_titles
    assert "Trigonometry Island" in world_titles
    assert worlds[0]["is_unlocked"] is True

    # 5. Recommended next mission
    rec = data["recommended_next_mission"]
    assert rec is not None
    assert rec["title"] == "Linear Equation Challenge"

    # 6. Achievement summary
    achievements = data["achievements"]
    assert achievements["total_badges"] >= 5
    assert achievements["earned_badges_count"] == 0

def test_student_dashboard_with_xp_and_progression(client, student_token, test_student_user, db_session):
    """Module 2: Level climbs to Level 2 when XP crosses 100 threshold."""
    seed_curriculum_and_badges(db_session)

    # Award 120 XP to student in RewardLedger
    ledger_entry = RewardLedger(
        user_id=test_student_user.id,
        event_type="mission_completed",
        reference_id="m_1_initial",
        xp_delta=120
    )
    db_session.add(ledger_entry)
    db_session.commit()

    response = client.get(
        "/api/v1/dashboard/student",
        headers={"Authorization": f"Bearer {student_token}"}
    )
    assert response.status_code == 200
    data = response.json()

    gamification = data["gamification"]
    assert gamification["level"] == 2
    assert gamification["current_xp"] == 120
    assert gamification["rank_title"] == "Equation Apprentice"
    assert gamification["progress_percentage"] > 0

def test_student_dashboard_recently_completed_and_accuracy(client, student_token, test_student_user, db_session):
    """Module 2: Displays completed mission in recent list and updates accuracy."""
    seed_curriculum_and_badges(db_session)

    m1 = db_session.query(Mission).first()
    # Record completed mission progress
    mp = MissionProgress(
        user_id=test_student_user.id,
        mission_id=m1.id,
        status=MissionStatus.COMPLETED.value,
        score=3,
        accuracy=100.0,
        attempts_count=3,
        completed_at=datetime.now(timezone.utc)
    )
    db_session.add(mp)
    db_session.commit()

    response = client.get(
        "/api/v1/dashboard/student",
        headers={"Authorization": f"Bearer {student_token}"}
    )
    assert response.status_code == 200
    data = response.json()

    # Progress updated
    assert data["learning_progress"]["completed_missions"] == 1
    assert data["learning_progress"]["completion_percentage"] > 0

    # Recently completed
    recents = data["recently_completed_missions"]
    assert len(recents) == 1
    assert recents[0]["mission_title"] == m1.title
    assert recents[0]["accuracy"] == 100.0

def test_student_dashboard_earned_badge_display(client, student_token, test_student_user, db_session):
    """Module 2: Shows awarded badges as earned in achievement summary."""
    seed_curriculum_and_badges(db_session)

    first_badge = db_session.query(Badge).filter(Badge.code == "first_steps").first()
    ub = UserBadge(user_id=test_student_user.id, badge_id=first_badge.id)
    db_session.add(ub)
    db_session.commit()

    response = client.get(
        "/api/v1/dashboard/student",
        headers={"Authorization": f"Bearer {student_token}"}
    )
    assert response.status_code == 200
    achievements = response.json()["achievements"]
    assert achievements["earned_badges_count"] == 1

    earned_badges = [b for b in achievements["badges"] if b["is_earned"]]
    assert len(earned_badges) == 1
    assert earned_badges[0]["code"] == "first_steps"

def test_worlds_and_topics_endpoints(client, student_token, db_session):
    """Module 2: Worlds list and world details with topic missions."""
    seed_curriculum_and_badges(db_session)

    list_resp = client.get("/api/v1/worlds/", headers={"Authorization": f"Bearer {student_token}"})
    assert list_resp.status_code == 200
    worlds = list_resp.json()
    assert len(worlds) >= 2
    w1_id = worlds[0]["id"]

    detail_resp = client.get(f"/api/v1/worlds/{w1_id}", headers={"Authorization": f"Bearer {student_token}"})
    assert detail_resp.status_code == 200
    w_detail = detail_resp.json()
    assert w_detail["id"] == w1_id
    assert len(w_detail["topics"]) >= 1
    assert len(w_detail["topics"][0]["missions"]) >= 1

