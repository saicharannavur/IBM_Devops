import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_dishes(client):
    rv = client.get('/dishes')
    assert rv.status_code == 200

def test_get_dish(client):
    rv = client.get('/dishes/1')
    assert rv.status_code == 200
    assert rv.get_json() == {"id": 1, "name": "Pizza", "price": 10.99}

def test_add_dish(client):
    rv = client.post('/dishes', json={"id": 4, "name": "Salad", "price": 6.99})
    assert rv.status_code == 201
    assert rv.get_json() == {"id": 4, "name": "Salad", "price": 6.99}
 
