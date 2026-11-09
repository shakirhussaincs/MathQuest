import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.main import app
from app.models.user import User, UserRole
from app.services.security import hash_password

# In-memory SQLite for high-speed, isolated unit and integration testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    """Creates a fresh in-memory database for each test function."""
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(db_session):
    """Provides a TestClient wired to the in-memory test database."""
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()

@pytest.fixture
def test_admin_user(db_session):
    admin = User(
        email="admin_test@mathquest.edu",
        display_name="Test Admin",
        password_hash=hash_password("AdminPass123"),
        role=UserRole.ADMIN,
        grade=None,
        is_active=True
    )
    db_session.add(admin)
    db_session.commit()
    db_session.refresh(admin)
    return admin

@pytest.fixture
def test_student_user(db_session):
    student = User(
        email="student_test@mathquest.edu",
        display_name="Test Student",
        password_hash=hash_password("StudentPass123"),
        role=UserRole.STUDENT,
        grade=11,
        is_active=True
    )
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)
    return student

@pytest.fixture
def admin_token(client, test_admin_user):
    resp = client.post("/api/v1/auth/login", json={
        "email": test_admin_user.email,
        "password": "AdminPass123"
    })
    return resp.json()["access_token"]

@pytest.fixture
def student_token(client, test_student_user):
    resp = client.post("/api/v1/auth/login", json={
        "email": test_student_user.email,
        "password": "StudentPass123"
    })
    return resp.json()["access_token"]

