from app.models.curriculum import World, Topic, Mission, Question
from app.services.curriculum_seed import seed_curriculum_and_badges

def test_four_worlds_seeded(client, student_token, db_session):
    """Module 3: All 4 required worlds are present across Grades 11 and 12."""
    seed_curriculum_and_badges(db_session)

    all_worlds = db_session.query(World).all()
    assert len(all_worlds) == 4
    titles = [w.title for w in all_worlds]
    assert "Algebra Kingdom" in titles
    assert "Trigonometry Island" in titles
    assert "Calculus Tower" in titles
    assert "Statistics City" in titles

def test_grade_11_student_filtering(client, student_token, db_session):
    """Module 3: Grade 11 student receives Grade 11 realms."""
    seed_curriculum_and_badges(db_session)

    resp = client.get("/api/v1/worlds/", headers={"Authorization": f"Bearer {student_token}"})
    assert resp.status_code == 200
    worlds = resp.json()
    assert len(worlds) == 2
    titles = [w["title"] for w in worlds]
    assert "Algebra Kingdom" in titles
    assert "Trigonometry Island" in titles
    assert "Calculus Tower" not in titles

def test_topic_learning_objectives_and_categorisation(client, student_token, db_session):
    """Module 3: Topics show descriptions, learning objectives, and mission categories."""
    seed_curriculum_and_badges(db_session)

    w1 = db_session.query(World).filter(World.title == "Algebra Kingdom").first()
    resp = client.get(f"/api/v1/worlds/{w1.id}", headers={"Authorization": f"Bearer {student_token}"})
    assert resp.status_code == 200
    data = resp.json()

    assert len(data["topics"]) >= 2
    topic1 = data["topics"][0]
    assert len(topic1["learning_objectives"]) >= 2
    assert len(topic1["missions"]) >= 2

    # Check categories
    categories = [m["category"] for m in topic1["missions"]]
    assert "concept_exploration" in categories or "practice" in categories

def test_anti_cheat_mission_payload(client, student_token, db_session):
    """FR-27: Question correct_answer and explanation are NOT exposed prior to submission."""
    seed_curriculum_and_badges(db_session)

    m1 = db_session.query(Mission).first()
    resp = client.get(f"/api/v1/missions/{m1.id}", headers={"Authorization": f"Bearer {student_token}"})
    assert resp.status_code == 200
    mission_data = resp.json()

    for q in mission_data["questions"]:
        assert "correct_answer" not in q
        assert "explanation" not in q

def test_fr11_student_blocked_from_other_grade_mission(client, student_token, db_session):
    """FR-11: Grade 11 student cannot access a Grade 12 Calculus mission."""
    seed_curriculum_and_badges(db_session)

    calc_world = db_session.query(World).filter(World.title == "Calculus Tower").first()
    calc_topic = db_session.query(Topic).filter(Topic.world_id == calc_world.id).first()
    calc_mission = db_session.query(Mission).filter(Mission.topic_id == calc_topic.id).first()

    resp = client.get(f"/api/v1/missions/{calc_mission.id}", headers={"Authorization": f"Bearer {student_token}"})
    assert resp.status_code == 403
    assert "belongs to Grade 12" in resp.json()["detail"]

def test_submit_answer_and_idempotent_xp(client, student_token, db_session):
    """FR-17, FR-22, FR-24, FR-33: Answer checked, explanation revealed, XP awarded idempotently."""
    seed_curriculum_and_badges(db_session)

    m1 = db_session.query(Mission).first()
    q1 = db_session.query(Question).filter(Question.mission_id == m1.id).first()

    # 1. First submission (Correct)
    resp1 = client.post(
        f"/api/v1/missions/{m1.id}/attempt",
        json={"question_id": q1.id, "submitted_answer": q1.correct_answer},
        headers={"Authorization": f"Bearer {student_token}"}
    )
    assert resp1.status_code == 200
    res1_data = resp1.json()
    assert res1_data["is_correct"] is True
    assert res1_data["xp_awarded"] == 10
    assert "explanation" in res1_data
    assert len(res1_data["explanation"]) > 5

    # 2. Second duplicate submission (Same Question)
    resp2 = client.post(
        f"/api/v1/missions/{m1.id}/attempt",
        json={"question_id": q1.id, "submitted_answer": q1.correct_answer},
        headers={"Authorization": f"Bearer {student_token}"}
    )
    assert resp2.status_code == 200
    assert resp2.json()["xp_awarded"] == 0  # Idempotent - no duplicate XP awarded!

def test_complete_mission_and_badge_unlock(client, student_token, test_student_user, db_session):
    """FR-19, FR-28, FR-31: Finalize mission, award completion bonus XP, unlock badges."""
    seed_curriculum_and_badges(db_session)

    m1 = db_session.query(Mission).first()
    questions = db_session.query(Question).filter(Question.mission_id == m1.id).all()

    # Submit all correct answers
    for q in questions:
        client.post(
            f"/api/v1/missions/{m1.id}/attempt",
            json={"question_id": q.id, "submitted_answer": q.correct_answer},
            headers={"Authorization": f"Bearer {student_token}"}
        )

    # Complete mission
    resp = client.post(
        f"/api/v1/missions/{m1.id}/complete",
        headers={"Authorization": f"Bearer {student_token}"}
    )
    assert resp.status_code == 200
    comp_data = resp.json()
    assert comp_data["score"] == len(questions)
    assert comp_data["accuracy_percentage"] == 100.0
    assert comp_data["bonus_xp_awarded"] == m1.xp_reward

    # Verify badge unlocks
    unlocked_codes = [b["code"] for b in comp_data["badges_unlocked"]]
    assert "first_steps" in unlocked_codes
    assert "accuracy_star" in unlocked_codes

def test_admin_can_create_world_and_topic(client, admin_token, db_session):
    """FR-58: Administrator creates a new mathematics world and topic."""
    # 1. Create World
    w_resp = client.post(
        "/api/v1/worlds/",
        json={
            "title": "Geometry Citadel",
            "description": "Explore Euclidean and analytic geometry.",
            "grade": 11,
            "icon": "shield",
            "theme_color": "blue"
        },
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert w_resp.status_code == 201
    world_id = w_resp.json()["world"]["id"]

    # 2. Add Topic
    t_resp = client.post(
        f"/api/v1/worlds/{world_id}/topics",
        json={
            "title": "Circle Theorems",
            "description": "Chords, tangents, and cyclic quadrilaterals.",
            "learning_objectives": ["Prove tangent perpendicularity", "Angle at centre theorem"]
        },
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert t_resp.status_code == 201
    assert "Circle Theorems" in t_resp.json()["topic"]["title"]

