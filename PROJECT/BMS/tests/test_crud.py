import pytest
from app.models import Account, db
from app.crud import create_account, read_by_id, update_account, delete_account

@pytest.fixture(scope="module")
def test_client():
    from app.routes import application
    application.config['TESTING'] = True
    application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with application.app_context():
        db.create_all()
        yield application.test_client()
        db.drop_all()

def test_create_and_read_account(test_client):
    account_data = {'id': 1, 'name': 'Test Account', 'number': '1234567890', 'balance': 1000.0}
    create_account(account_data)
    fetched = read_by_id(1)
    assert fetched['name'] == 'Test Account'
    assert fetched['balance'] == 1000.0

def test_update_account(test_client):
    updated_data = {'name': 'Updated Account', 'number': '0987654321', 'balance': 1500.0}
    update_account(1, updated_data)
    fetched = read_by_id(1)
    assert fetched['name'] == 'Updated Account'
    assert fetched['balance'] == 1500.0

def test_delete_account(test_client):
    delete_account(1)
    with pytest.raises(Exception):
        read_by_id(1)
