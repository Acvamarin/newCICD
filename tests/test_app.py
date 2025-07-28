import pytest
from app import app, db, User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    db.create_all()
    yield app.test_client()
    db.drop_all()

def test_add_user(client):
    response = client.post('/users', json={'name': 'John Doe'})
    assert response.status_code == 201
    assert response.get_json()['name'] == 'John Doe'

def test_get_users(client):
    client.post('/users', json={'name': 'John Doe'})
    response = client.get('/users')
    assert response.status_code == 200
    assert len(response.get_json()) == 1

