def test_register_student_success(client):
    """FR-01, FR-03: Student can register with valid details and grade (1-12)."""
    response = client.post("/api/v1/auth/register", json={
        "email": "newstudent@mathquest.edu",
        "display_name": "Hamza Tariq",
        "password": "Password123!",
        "role": "student",
        "grade": 11,
        "avatar": "avatar_explorer_1"
    })
    assert response.status_code == 201
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    assert data["user"]["email"] == "newstudent@mathquest.edu"
    assert data["user"]["display_name"] == "Hamza Tariq"
    assert data["user"]["grade"] == 11
    assert data["user"]["role"] == "student"

def test_register_duplicate_email_fails(client, test_student_user):
    """TC-02: Registering with an existing email returns 400 Bad Request."""
    response = client.post("/api/v1/auth/register", json={
        "email": test_student_user.email,
        "display_name": "Duplicate Student",
        "password": "Password123!",
        "role": "student",
        "grade": 12
    })
    assert response.status_code == 400
    assert "already exists" in response.json()["detail"]

def test_register_student_missing_grade_fails(client):
    """FR-03: Grade is mandatory for students."""
    response = client.post("/api/v1/auth/register", json={
        "email": "nograde@mathquest.edu",
        "display_name": "No Grade Student",
        "password": "Password123!",
        "role": "student"
    })
    assert response.status_code == 422  # Pydantic validation failure

def test_login_success(client, test_student_user):
    """FR-02: User can log in with correct credentials."""
    response = client.post("/api/v1/auth/login", json={
        "email": test_student_user.email,
        "password": "StudentPass123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["user"]["email"] == test_student_user.email

def test_login_wrong_password_fails(client, test_student_user):
    """NFR-04: Incorrect password rejected with 401."""
    response = client.post("/api/v1/auth/login", json={
        "email": test_student_user.email,
        "password": "WrongPassword999"
    })
    assert response.status_code == 401
    assert "Invalid email or password" in response.json()["detail"]

def test_login_nonexistent_user_fails(client):
    response = client.post("/api/v1/auth/login", json={
        "email": "ghost@mathquest.edu",
        "password": "Password123"
    })
    assert response.status_code == 401

def test_logout(client, student_token):
    """FR-02: User can log out."""
    response = client.post(
        "/api/v1/auth/logout",
        headers={"Authorization": f"Bearer {student_token}"}
    )
    assert response.status_code == 200
    assert "Successfully logged out" in response.json()["message"]

def test_password_reset_flow(client, test_student_user):
    """FR-06: Requesting and confirming password reset works end-to-end."""
    # 1. Request reset
    req_resp = client.post("/api/v1/auth/forgot-password", json={
        "email": test_student_user.email
    })
    assert req_resp.status_code == 200
    detail = req_resp.json()["detail"]
    assert "Reset token" in detail
    token = detail.split("Reset token (prototype mode): ")[1]

    # 2. Confirm reset with new password
    confirm_resp = client.post("/api/v1/auth/reset-password", json={
        "reset_token": token,
        "new_password": "NewSecretPass456!"
    })
    assert confirm_resp.status_code == 200
    assert "successfully reset" in confirm_resp.json()["message"]

    # 3. Old password should fail now
    old_login = client.post("/api/v1/auth/login", json={
        "email": test_student_user.email,
        "password": "StudentPass123"
    })
    assert old_login.status_code == 401

    # 4. New password should succeed
    new_login = client.post("/api/v1/auth/login", json={
        "email": test_student_user.email,
        "password": "NewSecretPass456!"
    })
    assert new_login.status_code == 200

