from app.models import db, Account
from app.exceptions import AccountNotFoundError, AccountAlreadyExistError, DatabaseError

def create_account(account):
    existing = db.session.query(Account).filter_by(id=account['id']).first()
    if existing:
        raise AccountAlreadyExistError(f"Account with id {account['id']} already exists.")
    try:
        account_model = Account(
            id=account['id'],
            name=account['name'],
            number=account['number'],
            balance=account['balance']
        )
        db.session.add(account_model)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise DatabaseError(f"Failed to create account: {e}")

def read_all_accounts():
    accounts = db.session.query(Account).all()
    dict_accounts = [account.to_dict() for account in accounts]
    return dict_accounts

def read_model_by_id(id):
    account = db.session.query(Account).filter_by(id=id).first()
    if not account:
        raise AccountNotFoundError(f"Account with id {id} not found.")
    return account

def read_by_id(id):
    account = read_model_by_id(id)
    return account.to_dict()

def update_account(id, new_account):
    account = db.session.query(Account).filter_by(id=id).first()
    if not account:
        raise AccountNotFoundError(f"Account with id {id} not found.")
    try:
        account.name = new_account['name']
        account.number = new_account['number']
        account.balance = new_account['balance']
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise DatabaseError(f"Failed to update account: {e}")

def delete_account(id):
    account = db.session.query(Account).filter_by(id=id).first()
    if not account:
        raise AccountNotFoundError(f"Account with id {id} not found.")
    try:
        db.session.delete(account)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise DatabaseError(f"Failed to delete account: {e}")
