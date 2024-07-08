import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_orders(client):
    rv = client.get('/orders')
    assert rv.status_code == 200

def test_get_order(client):
    rv = client.get('/orders/1')
    assert rv.status_code == 404

def test_add_order(client):
    rv = client.post('/orders', json={"id": 1, "dish": "Pizza", "quantity": 2})
    assert rv.status_code == 201
    assert rv.get_json() == {"id": 1, "dish": "Pizza", "quantity": 2}
 
