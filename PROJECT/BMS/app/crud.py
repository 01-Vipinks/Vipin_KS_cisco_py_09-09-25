"""
CRUD operations for Account management in Banking Management System.

Provides functions to create, read, update, and delete Account records
using SQLAlchemy ORM. Includes error handling via custom exceptions.
"""

from app.models import db, Account
from app.exceptions import AccountNotFoundError, AccountAlreadyExistError, DatabaseError

def create_account(account):
    """
    Create a new account in the database.

    Args:
        account (dict): Dictionary with keys 'id', 'name', 'number', 'balance'.

    Raises:
        AccountAlreadyExistError: If an account with the same id already exists.
        DatabaseError: If database operation fails.

    Returns:
        None
    """
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
    """
    Retrieve all accounts from the database.

    Returns:
        list: List of accounts as dictionaries.
    """
    accounts = db.session.query(Account).all()
    dict_accounts = [account.to_dict() for account in accounts]
    return dict_accounts

def read_model_by_id(id):
    """
    Retrieve the Account model instance by id.

    Args:
        id (int): Account id.

    Raises:
        AccountNotFoundError: If account is not found.

    Returns:
        Account: ORM model instance.
    """
    account = db.session.query(Account).filter_by(id=id).first()
    if not account:
        raise AccountNotFoundError(f"Account with id {id} not found.")
    return account

def read_by_id(id):
    """
    Retrieve account details as a dictionary by id.

    Args:
        id (int): Account id.

    Raises:
        AccountNotFoundError: If account is not found.

    Returns:
        dict: Account details.
    """
    account = read_model_by_id(id)
    return account.to_dict()

def update_account(id, new_account):
    """
    Update an existing account's details.

    Args:
        id (int): Account id to update.
        new_account (dict): Updated account fields: 'name', 'number', 'balance'.

    Raises:
        AccountNotFoundError: If account is not found.
        DatabaseError: If update operation fails.

    Returns:
        None
    """
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
    """
    Delete an account from the database by id.

    Args:
        id (int): Account id.

    Raises:
        AccountNotFoundError: If account is not found.
        DatabaseError: If delete operation fails.

    Returns:
        None
    """
    account = db.session.query(Account).filter_by(id=id).first()
    if not account:
        raise AccountNotFoundError(f"Account with id {id} not found.")
    try:
        db.session.delete(account)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise DatabaseError(f"Failed to delete account: {e}")
