import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_cancellations(client):
    rv = client.get('/cancellations')
    assert rv.status_code == 200

def test_get_cancellation(client):
    rv = client.get('/cancellations/1')
    assert rv.status_code == 404

def test_add_cancellation(client):
    rv = client.post('/cancellations', json={"id": 1, "order_id": 123, "reason": "Customer Request"})
    assert rv.status_code == 201
    assert rv.get_json() == {"id": 1, "order_id": 123, "reason": "Customer Request"}
 
