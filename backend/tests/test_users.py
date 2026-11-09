def test_get_my_profile(client, student_token, test_student_user):
    """Student can retrieve their own profile."""
    response = client.get(
        "/api/v1/users/me",
        headers={"Authorization": f"Bearer {student_token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == test_student_user.email
    assert data["display_name"] == test_student_user.display_name
    assert data["grade"] == 11

def test_update_my_profile(client, student_token):
    """FR-04: Student can update their display name, grade, avatar, and bio."""
    response = client.patch(
        "/api/v1/users/me",
        json={
            "display_name": "Zayd Updated",
            "grade": 12,
            "avatar": "avatar_wizard_gold",
            "bio": "Aiming for 100% accuracy in Calculus!"
        },
        headers={"Authorization": f"Bearer {student_token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["display_name"] == "Zayd Updated"
    assert data["grade"] == 12
    assert data["avatar"] == "avatar_wizard_gold"
    assert data["bio"] == "Aiming for 100% accuracy in Calculus!"

def test_change_password_success(client, student_token, test_student_user):
    """Student can change password with correct current password."""
    response = client.post(
        "/api/v1/users/me/change-password",
        json={
            "old_password": "StudentPass123",
            "new_password": "BrandNewPassword789!"
        },
        headers={"Authorization": f"Bearer {student_token}"}
    )
    assert response.status_code == 200
    assert "successfully updated" in response.json()["message"]

    # Verify new password works
    login_resp = client.post("/api/v1/auth/login", json={
        "email": test_student_user.email,
        "password": "BrandNewPassword789!"
    })
    assert login_resp.status_code == 200

def test_change_password_wrong_old_fails(client, student_token):
    """Changing password fails if old password is wrong."""
    response = client.post(
        "/api/v1/users/me/change-password",
        json={
            "old_password": "WrongOldPassword",
            "new_password": "BrandNewPassword789!"
        },
        headers={"Authorization": f"Bearer {student_token}"}
    )
    assert response.status_code == 400
    assert "Current password entered is incorrect" in response.json()["detail"]

def test_rbac_student_cannot_access_admin_endpoint(client, student_token):
    """FR-05, TC-07: Students are strictly forbidden from admin management endpoints."""
    response = client.get(
        "/api/v1/users/",
        headers={"Authorization": f"Bearer {student_token}"}
    )
    assert response.status_code == 403
    assert "Access denied" in response.json()["detail"]

def test_admin_can_list_users(client, admin_token, test_student_user):
    """Admin can list and query registered users."""
    response = client.get(
        "/api/v1/users/",
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code == 200
    users = response.json()
    assert len(users) >= 2
    emails = [u["email"] for u in users]
    assert test_student_user.email in emails

def test_admin_update_role_and_deactivate(client, admin_token, test_student_user):
    """Admin can promote role to teacher and toggle account activation."""
    # 1. Update role to teacher
    role_resp = client.patch(
        f"/api/v1/users/{test_student_user.id}/role",
        json={"role": "teacher"},
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert role_resp.status_code == 200
    assert role_resp.json()["role"] == "teacher"

    # 2. Deactivate user account
    deactivate_resp = client.patch(
        f"/api/v1/users/{test_student_user.id}/status",
        json={"is_active": False},
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert deactivate_resp.status_code == 200
    assert deactivate_resp.json()["is_active"] is False

    # 3. Deactivated user cannot log in
    login_resp = client.post("/api/v1/auth/login", json={
        "email": test_student_user.email,
        "password": "StudentPass123"
    })
    assert login_resp.status_code == 403
    assert "deactivated" in login_resp.json()["detail"]

def test_admin_cannot_deactivate_self(client, admin_token, test_admin_user):
    """Admin cannot accidentally deactivate their own account."""
    response = client.patch(
        f"/api/v1/users/{test_admin_user.id}/status",
        json={"is_active": False},
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code == 400
    assert "cannot deactivate your own" in response.json()["detail"]

