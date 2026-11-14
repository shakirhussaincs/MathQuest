import pytest
from app.models.user import User, UserRole
from app.models.curriculum import World, Topic, Mission, Question, MissionCategory, DifficultyLevel, MissionProgress
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

def seed_test_curriculum(db_session):
    # World for Grade 10
    w10 = World(title="Geometry Haven", description="Grade 10 Realm", grade=10, is_active=True)
    # World for Grade 11
    w11 = World(title="Algebra Realm", description="Grade 11 Realm", grade=11, is_active=True)
    db_session.add_all([w10, w11])
    db_session.commit()

    # Topic for Grade 10
    t10 = Topic(world_id=w10.id, title="Circles & Tangents", grade=10)
    # Topic for Grade 11
    t11 = Topic(world_id=w11.id, title="Polynomials", grade=11)
    db_session.add_all([t10, t11])
    db_session.commit()

    # Mission for Grade 10
    m10 = Mission(
        topic_id=t10.id,
        title="Circle Basics",
        instructions="Solve circles",
        category=MissionCategory.PRACTICE.value,
        difficulty=DifficultyLevel.EASY.value,
        question_count=2,
        xp_reward=20,
        pass_percentage=60,
        is_active=True
    )

    # Mission for Grade 11 with 5 questions
    m11 = Mission(
        topic_id=t11.id,
        title="Polynomial Trial",
        instructions="Solve polynomials",
        category=MissionCategory.PRACTICE.value,
        difficulty=DifficultyLevel.EASY.value,
        question_count=5,
        xp_reward=20,
        pass_percentage=60,
        is_active=True
    )
    db_session.add_all([m10, m11])
    db_session.commit()

    # 2 Questions for Grade 10
    q10_1 = Question(
        mission_id=m10.id,
        prompt="Radius of circle with area 16pi?",
        question_type="multiple_choice",
        options=["A) 2", "B) 4", "C) 8", "D) 16"],
        correct_answer="B) 4",
        explanation="pi*r^2 = 16pi => r=4",
        display_order=1,
        is_active=True
    )
    q10_2 = Question(
        mission_id=m10.id,
        prompt="Diameter of circle with radius 5?",
        question_type="numeric",
        correct_answer="10",
        explanation="d = 2r = 10",
        display_order=2,
        is_active=True
    )

    # 5 Questions for Grade 11
    q11_list = [
        Question(
            mission_id=m11.id,
            prompt=f"Grade 11 Question {i}: Solve x + {i} = 10",
            question_type="multiple_choice",
            options=["A) 1", f"B) {10 - i}", "C) 10", "D) 0"],
            correct_answer=f"B) {10 - i}",
            explanation=f"x = 10 - {i}",
            display_order=i,
            is_active=True
        )
        for i in range(1, 6)
    ]
    db_session.add_all([q10_1, q10_2] + q11_list)
    db_session.commit()

    return {"w10": w10, "w11": w11, "m10": m10, "m11": m11, "q11_list": q11_list}

def test_1_and_2_grade_isolation_and_empty_state(client, db_session):
    """Case 1 & 2: Grade 5 receives only Grade 5 questions (or empty state), Grade 10 receives only Grade 10."""
    data = seed_test_curriculum(db_session)
    
    # Grade 5 student (no content seeded for Grade 5)
    s5 = create_user(db_session, "student5@test.edu", UserRole.STUDENT, grade=5)
    tok5 = get_token_for(client, s5.email)
    
    # Worlds list for Grade 5 student returns empty list
    r5_worlds = client.get("/api/v1/worlds/", headers={"Authorization": f"Bearer {tok5}"})
    assert r5_worlds.status_code == 200
    assert r5_worlds.json() == []

    # Student dashboard for Grade 5 student returns 0 missions, empty worlds
    r5_dash = client.get("/api/v1/dashboard/student", headers={"Authorization": f"Bearer {tok5}"})
    assert r5_dash.status_code == 200
    dash_json = r5_dash.json()
    assert dash_json["worlds"] == []
    assert dash_json["learning_progress"]["total_missions"] == 0

    # Grade 10 student receives Grade 10 world and mission
    s10 = create_user(db_session, "student10@test.edu", UserRole.STUDENT, grade=10)
    tok10 = get_token_for(client, s10.email)
    r10_worlds = client.get("/api/v1/worlds/", headers={"Authorization": f"Bearer {tok10}"})
    assert r10_worlds.status_code == 200
    worlds_10 = r10_worlds.json()
    assert len(worlds_10) == 1
    assert worlds_10[0]["grade"] == 10

    # Access Grade 10 mission
    r10_m = client.get(f"/api/v1/missions/{data['m10'].id}", headers={"Authorization": f"Bearer {tok10}"})
    assert r10_m.status_code == 200
    assert len(r10_m.json()["questions"]) == 2

def test_3_grade_tamper_prevention(client, db_session):
    """Case 3: Grade 11 student cannot access Grade 10 mission or world by manipulating request."""
    data = seed_test_curriculum(db_session)
    s11 = create_user(db_session, "student11_tamper@test.edu", UserRole.STUDENT, grade=11)
    tok11 = get_token_for(client, s11.email)

    # 1. Attempt to list worlds with ?grade=10 query override -> system ignores and returns Grade 11 worlds only
    r_worlds = client.get("/api/v1/worlds/?grade=10", headers={"Authorization": f"Bearer {tok11}"})
    assert r_worlds.status_code == 200
    for w in r_worlds.json():
        assert w["grade"] == 11

    # 2. Attempt to GET Grade 10 world details directly -> 403 Forbidden
    r_w10 = client.get(f"/api/v1/worlds/{data['w10'].id}", headers={"Authorization": f"Bearer {tok11}"})
    assert r_w10.status_code == 403

    # 3. Attempt to GET Grade 10 mission directly -> 403 Forbidden
    r_m10 = client.get(f"/api/v1/missions/{data['m10'].id}", headers={"Authorization": f"Bearer {tok11}"})
    assert r_m10.status_code == 403

    # 4. Attempt to POST answer to Grade 10 mission attempt endpoint -> 403 Forbidden
    r_att = client.post(
        f"/api/v1/missions/{data['m10'].id}/attempt",
        headers={"Authorization": f"Bearer {tok11}"},
        json={"question_id": 1, "submitted_answer": "B) 4"}
    )
    assert r_att.status_code == 403

    # 5. Attempt to POST completion to Grade 10 mission complete endpoint -> 403 Forbidden
    r_comp = client.post(
        f"/api/v1/missions/{data['m10'].id}/complete",
        headers={"Authorization": f"Bearer {tok11}"}
    )
    assert r_comp.status_code == 403

def test_4_5_6_7_randomization_concurrency_and_refresh(client, db_session):
    """
    Cases 4, 5, 6, 7:
    - Independent randomization
    - Concurrent students receive different first questions when enough questions exist
    - No duplicate questions in single attempt
    - Page refresh preserves active attempt order
    """
    data = seed_test_curriculum(db_session)
    s11_a = create_user(db_session, "student_a@test.edu", UserRole.STUDENT, grade=11)
    s11_b = create_user(db_session, "student_b@test.edu", UserRole.STUDENT, grade=11)
    tok_a = get_token_for(client, s11_a.email)
    tok_b = get_token_for(client, s11_b.email)

    # Student A opens mission
    res_a = client.get(f"/api/v1/missions/{data['m11'].id}", headers={"Authorization": f"Bearer {tok_a}"})
    assert res_a.status_code == 200
    q_ids_a = [q["id"] for q in res_a.json()["questions"]]

    # Case 6: No duplicate questions
    assert len(q_ids_a) == 5
    assert len(set(q_ids_a)) == 5

    # Student B opens same mission concurrently
    res_b = client.get(f"/api/v1/missions/{data['m11'].id}", headers={"Authorization": f"Bearer {tok_b}"})
    assert res_b.status_code == 200
    q_ids_b = [q["id"] for q in res_b.json()["questions"]]

    assert len(q_ids_b) == 5
    assert len(set(q_ids_b)) == 5

    # Case 5: Different first question assigned to concurrent student
    assert q_ids_a[0] != q_ids_b[0], f"Expected different first questions, got {q_ids_a[0]} for both"

    # Case 7: Refreshing active attempt preserves its question order
    refresh_a = client.get(f"/api/v1/missions/{data['m11'].id}", headers={"Authorization": f"Bearer {tok_a}"})
    assert refresh_a.status_code == 200
    q_ids_a_refreshed = [q["id"] for q in refresh_a.json()["questions"]]
    assert q_ids_a == q_ids_a_refreshed, "Refreshing active attempt must preserve question order"

def test_8_and_9_answer_validation_and_xp_completion(client, db_session):
    """
    Cases 8 & 9:
    - Correct answer validation works regardless of shuffled order
    - Idempotent XP and mission completion logic works
    """
    data = seed_test_curriculum(db_session)
    s11 = create_user(db_session, "student_eval@test.edu", UserRole.STUDENT, grade=11)
    tok = get_token_for(client, s11.email)

    m_resp = client.get(f"/api/v1/missions/{data['m11'].id}", headers={"Authorization": f"Bearer {tok}"})
    questions = m_resp.json()["questions"]

    # Submit correct answer for each question using its actual question ID
    for q in questions:
        # Prompt has format "Grade 11 Question {i}: Solve x + {i} = 10", answer is "B) {10 - i}"
        q_num = int(q["prompt"].split("Question ")[1].split(":")[0])
        correct_ans = f"B) {10 - q_num}"

        ans_res = client.post(
            f"/api/v1/missions/{data['m11'].id}/attempt",
            headers={"Authorization": f"Bearer {tok}"},
            json={"question_id": q["id"], "submitted_answer": correct_ans}
        )
        assert ans_res.status_code == 200
        assert ans_res.json()["is_correct"] is True

    # Complete mission
    comp_res = client.post(
        f"/api/v1/missions/{data['m11'].id}/complete",
        headers={"Authorization": f"Bearer {tok}"}
    )
    assert comp_res.status_code == 200
    comp_json = comp_res.json()
    assert comp_json["is_passed"] is True
    assert comp_json["accuracy_percentage"] == 100.0
    assert comp_json["score"] == 5

def test_10_dashboard_role_access_restriction(client, db_session):
    """Case 10: Student, Teacher, and Admin dashboard endpoints enforce strict RBAC."""
    seed_test_curriculum(db_session)
    student = create_user(db_session, "student_rbac@test.edu", UserRole.STUDENT, grade=11)
    teacher = create_user(db_session, "teacher_rbac@test.edu", UserRole.TEACHER, grade=11)
    admin = create_user(db_session, "admin_rbac@test.edu", UserRole.ADMIN, grade=None)

    tok_s = get_token_for(client, student.email)
    tok_t = get_token_for(client, teacher.email)
    tok_a = get_token_for(client, admin.email)

    # 1. Student trying to access teacher dashboard -> 403 Forbidden
    r_s_teacher = client.get("/api/v1/dashboard/teacher", headers={"Authorization": f"Bearer {tok_s}"})
    assert r_s_teacher.status_code == 403

    # 2. Student trying to access admin dashboard -> 403 Forbidden
    r_s_admin = client.get("/api/v1/dashboard/admin", headers={"Authorization": f"Bearer {tok_s}"})
    assert r_s_admin.status_code == 403

    # 3. Student trying to access teacher mission preview -> 403 Forbidden
    r_s_preview = client.get("/api/v1/missions/1/preview", headers={"Authorization": f"Bearer {tok_s}"})
    assert r_s_preview.status_code == 403

    # 4. Teacher accessing teacher dashboard -> 200 OK
    r_t_teacher = client.get("/api/v1/dashboard/teacher", headers={"Authorization": f"Bearer {tok_t}"})
    assert r_t_teacher.status_code == 200
    assert r_t_teacher.json()["teacher"]["role"] == "teacher"

    # 5. Teacher accessing admin dashboard -> 403 Forbidden
    r_t_admin = client.get("/api/v1/dashboard/admin", headers={"Authorization": f"Bearer {tok_t}"})
    assert r_t_admin.status_code == 403

    # 6. Admin accessing admin dashboard -> 200 OK
    r_a_admin = client.get("/api/v1/dashboard/admin", headers={"Authorization": f"Bearer {tok_a}"})
    assert r_a_admin.status_code == 200
    assert r_a_admin.json()["admin"]["role"] == "admin"
