import client_repo as repo

def menu():
    message = '''
Options are:
1 - Create Account
2 - List All Accounts
3 - Read Account By Id
4 - Update Account
5 - Delete Account
6 - Exit
Your Option:'''
    choice = int(input(message))
    if choice == 1:
        id = int(input('ID:'))
        name = input('Name:')
        number = input('Number:')
        balance = float(input('Balance:'))

        account = {'id': id, 'name': name, 'number': number, 'balance': balance}

        createdAcc = repo.create_account(account)
        print(f'Created: {createdAcc}')
        print('Account Created Successfully.')
    elif choice == 2:
        print('List of Accounts:')
        for account in repo.read_all_accounts():
            print(account)
    elif choice == 3:
        id = int(input('ID:'))
        account = repo.read_by_id(id)
        if account is None:
            print('Account not found.')
        else:
            print(account)
    elif choice == 4:
        id = int(input('ID:'))
        account = repo.read_by_id(id)
        if account is None:
            print('Account Not Found')
        else:
            print(account)
            name = input('New Name:')
            number = input('New Number:')
            balance = float(input('New Balance:'))
            new_account = {
                'id': account['id'],
                'name': name,
                'number': number,
                'balance': balance
            }
            updatedAcc = repo.update(id, new_account)
            print(f'Updated: {updatedAcc}')
            print('Account updated successfully.')
    elif choice == 5:
        id = int(input('ID:'))
        account = repo.read_by_id(id)
        if account is None:
            print('Account Not Found')
        else:
            messageDict = repo.delete_account(id)
            print(messageDict['message'])
    elif choice == 6:
        print('Thank you for using Application')

    return choice

def menus():
    choice = menu()
    while choice != 6:
        choice = menu()

menus()
