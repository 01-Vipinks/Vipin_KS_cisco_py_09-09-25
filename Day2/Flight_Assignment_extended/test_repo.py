import pytest 
from db import db_setup
from db import repo_sql_dict as repo

@pytest.fixture(autouse=True)
def setup():
    db_setup.Base.metadata.drop_all(db_setup.engine)
    db_setup.Base.metadata.create_all(db_setup.engine)
    yield
    db_setup.Base.metadata.drop_all(db_setup.engine)

def test_create_flight():
    flight = {
        'id': 201,
        'number': 'AI202',
        'airline_name': 'Air India',
        'capacity': 180,
        'price': 6500.0,
        'source': 'Delhi',
        'destination': 'Mumbai',
        'is_active': True
    }
    repo.create_flight(flight)
    saved_flight = repo.read_by_id(201)
    assert (saved_flight is not None)
    assert (saved_flight['id'] == 201)
    assert (saved_flight['number'] == 'AI202')
    assert (saved_flight['airline_name'] == 'Air India')
    assert (saved_flight['capacity'] == 180)
    assert (saved_flight['price'] == 6500.0)
    assert (saved_flight['source'] == 'Delhi')
    assert (saved_flight['destination'] == 'Mumbai')
    assert (saved_flight['is_active'] is True)
