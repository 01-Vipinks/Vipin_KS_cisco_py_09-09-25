"""
    Consuming Accounts Management APIs
    - Consumer Account App
    - Account Client

    API REPO
"""

import requests
import sys
import os

# Import the project logger from app/logger.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))
from app.logger import logger

BASE_URL = "http://127.0.0.1:5000"

def create_account(account):
    """
    Create an account by making a POST request to the API.

    Args:
        account (dict): account data to create

    Returns:
        dict: Created account details
    """
    url = f'{BASE_URL}/accounts'
    response = requests.post(url, json=account)
    created_account_dict = response.json()
    logger.info("Account created via client.", extra={"account": account})
    return created_account_dict

def read_all_accounts():
    """
    Retrieve a list of all accounts from the API.

    Returns:
        list: List of account details
    """
    url = f'{BASE_URL}/accounts'
    response = requests.get(url)
    dict_accounts = response.json()
    logger.info("Read all accounts via client.")
    return dict_accounts

def read_by_id(id):
    """
    Retrieve a specific account by id.

    Args:
        id (int): Account id

    Returns:
        dict: Account details
    """
    url = f'{BASE_URL}/accounts/{id}'
    response = requests.get(url)
    account_dict = response.json()
    logger.info("Read account by ID via client.", extra={"id": id})
    return account_dict

def update(id, new_account):
    """
    Update a specific account by id.

    Args:
        id (int): Account id
        new_account (dict): New account data

    Returns:
        dict: Updated account details
    """
    url = f'{BASE_URL}/accounts/{id}'
    response = requests.put(url, json=new_account)
    updated_account_dict = response.json()
    logger.info("Updated account by ID via client.", extra={"id": id, "new_account": new_account})
    return updated_account_dict

def delete_account(id):
    """
    Delete a specific account by id.

    Args:
        id (int): Account id

    Returns:
        dict: Deletion message
    """
    url = f'{BASE_URL}/accounts/{id}'
    response = requests.delete(url)
    message_dict = response.json()
    logger.info("Deleted account by ID via client.", extra={"id": id})
    return message_dict
