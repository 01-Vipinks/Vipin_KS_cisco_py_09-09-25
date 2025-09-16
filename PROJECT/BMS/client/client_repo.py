"""
    Consuming Accounts Management APIs
    - Consumer Account App
    - Account Client

    API REPO
"""

import requests  # pip install requests

BASE_URL = "http://127.0.0.1:5000"

def create_account(account):
    url = f'{BASE_URL}/accounts'
    response = requests.post(url, json=account)
    created_account_dict = response.json()
    return created_account_dict

def read_all_accounts():
    url = f'{BASE_URL}/accounts'
    response = requests.get(url)
    dict_accounts = response.json()
    return dict_accounts

def read_by_id(id):
    url = f'{BASE_URL}/accounts/{id}'
    response = requests.get(url)
    account_dict = response.json()
    return account_dict

def update(id, new_account):
    url = f'{BASE_URL}/accounts/{id}'
    response = requests.put(url, json=new_account)
    updated_account_dict = response.json()
    return updated_account_dict

def delete_account(id):
    url = f'{BASE_URL}/accounts/{id}'
    response = requests.delete(url)
    message_dict = response.json()
    return message_dict
