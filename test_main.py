from fastapi.testclient import TestClient
from main import app
from sqlalchemy.orm import Session
from models import UserCreate
import json

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_create_user(db_session: Session):
    user_data = {"email": "test@test.com", "password": "password123"}
    response = client.post("/users/", data=json.dumps(user_data))
    assert response.status_code == 200
    user = UserCreate(**user_data)
    db_user = db_session.query(User).filter(User.email == user.email).first()
    assert db_user is not None

def test_get_user(db_session: Session):
    user_data = {"email": "test@test.com", "password": "password123"}
    db_user = User(**user_data)
    db_session.add(db_user)
    db_session.commit()
    response = client.get(f"/users/{db_user.id}")
    assert response.status_code == 200
    response_user = User(**response.json())
    assert response_user.id == db_user.id

# Here are some of the tests
# Здесь всего часть тестов