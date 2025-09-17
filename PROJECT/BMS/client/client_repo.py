"""
Consuming Accounts Management APIs
- Consumer Account App
- Account Client
API REPO
"""

import sys
import os
import requests

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
    response = requests.post(url, json=account, timeout=10)
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
    response = requests.get(url, timeout=10)
    dict_accounts = response.json()
    logger.info("Read all accounts via client.")
    return dict_accounts

def read_by_id(account_id):
    """
    Retrieve a specific account by id.

    Args:
        account_id (int): Account id

    Returns:
        dict: Account details
    """
    url = f'{BASE_URL}/accounts/{account_id}'
    response = requests.get(url, timeout=10)
    account_dict = response.json()
    logger.info("Read account by ID via client.", extra={"id": account_id})
    return account_dict

def update(account_id, new_account):
    """
    Update a specific account by id.

    Args:
        account_id (int): Account id
        new_account (dict): New account data

    Returns:
        dict: Updated account details
    """
    url = f'{BASE_URL}/accounts/{account_id}'
    response = requests.put(url, json=new_account, timeout=10)
    updated_account_dict = response.json()
    logger.info("Updated account by ID via client.", extra={"id": account_id, "new_account": new_account})
    return updated_account_dict

def delete_account(account_id):
    """
    Delete a specific account by id.

    Args:
        account_id (int): Account id

    Returns:
        dict: Deletion message
    """
    url = f'{BASE_URL}/accounts/{account_id}'
    response = requests.delete(url, timeout=10)
    message_dict = response.json()
    logger.info("Deleted account by ID via client.", extra={"id": account_id})
    return message_dict
