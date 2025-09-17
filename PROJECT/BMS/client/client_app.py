"""
Command line client for the Banking Management System.

Provides a menu-driven interface to interact with account management APIs.
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import client_repo as repo


def menu():
    """
    Display menu options and handle user input for account operations.

    Returns:
        int: The user's chosen menu option.
    """
    message = '''
Options are:
1 - Create Account
2 - List All Accounts
3 - Read Account By Id
4 - Update Account
5 - Delete Account
6 - Exit
Your Option:'''
    try:
        choice = int(input(message))
    except ValueError:
        print("Invalid input, please enter a number.")
        return 0

    if choice == 1:
        account_id = int(input('ID: '))
        name = input('Name: ')
        number = input('Number: ')
        balance = float(input('Balance: '))

        account = {'id': account_id, 'name': name, 'number': number, 'balance': balance}

        created_account = repo.create_account(account)
        print(f'Created: {created_account}')
        print('Account Created Successfully.')

    elif choice == 2:
        print('List of Accounts:')
        for account in repo.read_all_accounts():
            print(account)

    elif choice == 3:
        account_id = int(input('ID: '))
        account = repo.read_by_id(account_id)
        if account is None:
            print('Account not found.')
        else:
            print(account)

    elif choice == 4:
        account_id = int(input('ID: '))
        account = repo.read_by_id(account_id)
        if account is None:
            print('Account Not Found')
        else:
            print(account)
            name = input('New Name: ')
            number = input('New Number: ')
            balance = float(input('New Balance: '))
            new_account = {
                'id': account['id'],
                'name': name,
                'number': number,
                'balance': balance
            }
            updated_account = repo.update(account_id, new_account)
            print(f'Updated: {updated_account}')
            print('Account updated successfully.')

    elif choice == 5:
        account_id = int(input('ID: '))
        account = repo.read_by_id(account_id)
        if account is None:
            print('Account Not Found')
        else:
            message_dict = repo.delete_account(account_id)
            print(message_dict.get('message', 'No message returned.'))

    elif choice == 6:
        print('Thank you for using Application')

    else:
        print('Invalid option')

    return choice


def menus():
    """
    Run the menu loop until the user chooses to exit.
    """
    choice = menu()
    while choice != 6:
        choice = menu()


if __name__ == "__main__":
    menus()
