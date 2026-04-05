import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_user():
    payload = {"username": "test1", "password": "password1"}
    response = client.post("/register", json=payload)
    
    assert response.status_code == 201
    assert response.json()["username"] == "testuser"

def test_register_duplicate_user():
    payload = {"username": "test1", "password": "password1"}
    response = client.post("/register", json=payload)
    
    assert response.status_code == 409
    assert "already exists" in response.json()["detail"].lower()

def test_register_invalid_data():
    payload = {"username": "test2"}
    response = client.post("/register", json=payload)

    assert response.status_code == 422

def test_login_success():
    payload = {"username": "test1", "password": "password1"}
    response = client.post("/login", json=payload)
    
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_wrong_password():
    payload = {"username": "test1", "password": "wrong1"}
    response = client.post("/login", json=payload)
    
    assert response.status_code == 401

def test_login_non_existent_user():
    payload = {"username": "test2", "password": "password2"}

    response = client.post("/login", json=payload)
    assert response.status_code == 404