"""
Flask API routes for the Banking Management System.

Defines RESTful endpoints for Account CRUD operations,
error handling for custom exceptions, and integrates email notification
after account creation. Uses SQLAlchemy ORM via the crud layer.
"""

from datetime import datetime
from flask import Flask, request, jsonify
from app import crud  # Fixed import style to follow pylint recommendation
from app.config import config
import app.emailer as mail
from app.exceptions import AccountNotFoundError, AccountAlreadyExistError, DatabaseError

application = Flask(__name__)

# Database configuration and initialization
application.config['SQLALCHEMY_DATABASE_URI'] = config['DB_URL']
application.config['SQLALCHEMY_ECHO'] = True

crud.db.init_app(application)  # App-to-db configuration update

# Table creation at first startup
with application.app_context():
    crud.db.create_all()


@application.errorhandler(AccountNotFoundError)
def handle_not_found_error(error):
    """
    Flask error handler for AccountNotFoundError.
    Returns:
        Response: JSON error message with HTTP 404.
    """
    response = jsonify({'error': str(error)})
    response.status_code = 404
    return response


@application.errorhandler(AccountAlreadyExistError)
def handle_already_exist_error(error):
    """
    Flask error handler for AccountAlreadyExistError.
    Returns:
        Response: JSON error message with HTTP 409.
    """
    response = jsonify({'error': str(error)})
    response.status_code = 409
    return response


@application.errorhandler(DatabaseError)
def handle_database_error(error):
    """
    Flask error handler for DatabaseError.
    Returns:
        Response: JSON error message with HTTP 500.
    """
    response = jsonify({'error': str(error)})
    response.status_code = 500
    return response


@application.route("/accounts", methods=['POST'])
def create_account():
    """
    Create a new account.
    Expects JSON with keys: 'id', 'name', 'number', 'balance'.
    Sends notification email upon creation.
    Returns:
        Response: JSON of created account or error.
    """
    account_dict = request.json
    try:
        crud.create_account(account_dict)
        acc_id = account_dict['id']
        saved_account_dict = crud.read_by_id(acc_id)

        # Send notification email
        now = datetime.now()
        date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
        subject = f'{date_time_str} Account {account_dict["name"]} Created.'
        mail_body = f'''Account created successfully.
id : {acc_id}
name : {account_dict["name"]}
number : {account_dict["number"]}
balance : {account_dict["balance"]}
        '''
        result = mail.send_gmail(mail.FROM_ADDRESS, subject, mail_body)
        print(f'mail sent?{result}')

        return jsonify(saved_account_dict)
    except (AccountAlreadyExistError, DatabaseError) as e:
        return handle_database_error(e)


@application.route("/accounts", methods=['GET'])
def read_all_accounts():
    """
    Retrieve all accounts in the database.
    Returns:
        Response: JSON array of accounts.
    """
    accounts_dict = crud.read_all_accounts()
    return jsonify(accounts_dict)


@application.route("/accounts/<acc_id>", methods=['GET'])
def read_account_by_id(acc_id):
    """
    Retrieve a specific account by id.
    Args:
        acc_id (int): Account id.
    Returns:
        Response: JSON of account if found, error otherwise.
    """
    try:
        acc_id = int(acc_id)
        account_dict = crud.read_by_id(acc_id)
        return jsonify(account_dict)
    except AccountNotFoundError as e:
        return handle_not_found_error(e)


@application.route("/accounts/<acc_id>", methods=['PUT'])
def update_account(acc_id):
    """
    Update an existing account's details.
    Expects JSON body with new account values.
    Args:
        acc_id (int): Account id.
    Returns:
        Response: JSON of updated account or error.
    """
    try:
        acc_id = int(acc_id)
        account_dict = request.json
        crud.update_account(acc_id, account_dict)
        saved_account_dict = crud.read_by_id(acc_id)
        return jsonify(saved_account_dict)
    except (AccountNotFoundError, DatabaseError) as e:
        return handle_database_error(e)


@application.route("/accounts/<acc_id>", methods=['DELETE'])
def delete_account(acc_id):
    """
    Delete an account by id.
    Args:
        acc_id (int): Account id.
    Returns:
        Response: JSON message of success or error.
    """
    try:
        acc_id = int(acc_id)
        crud.delete_account(acc_id)
        return jsonify({'message': 'Deleted Successfully'})
    except (AccountNotFoundError, DatabaseError) as e:
        return handle_database_error(e)
