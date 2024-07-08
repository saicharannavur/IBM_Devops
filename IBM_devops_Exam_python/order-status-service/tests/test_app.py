import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_statuses(client):
    rv = client.get('/statuses')
    assert rv.status_code == 200

def test_get_status(client):
    rv = client.get('/statuses/1')
    assert rv.status_code == 404

def test_add_status(client):
    rv = client.post('/statuses', json={"id": 1, "status": "Order Placed"})
    assert rv.status_code == 201
    assert rv.get_json() == {"id": 1, "status": "Order Placed"}
 
