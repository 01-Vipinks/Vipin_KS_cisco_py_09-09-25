from db import repo_sql_dict as repo

def menu():
    message = '''
Options are:
1 - Create Flight
2 - List All Flights
3 - Read Flight By Id
4 - Update Flight Price
5 - Delete Flight
6 - Exit
Your Option:'''
    choice = int(input(message))
    if choice == 1:
        id = int(input('ID:'))
        number = input('Number:')
        airline_name = input('Airline Name:')
        capacity = int(input('Capacity:'))
        price = float(input('Price:'))
        source = input('Source:')
        destination = input('Destination:')
        is_active = (input('Active(y/n):').upper() == 'Y')
        flight = {'id': id, 'number': number, 'airline_name': airline_name,
                  'capacity': capacity, 'price': price,
                  'source': source, 'destination': destination,
                  'is_active': is_active}
        try:
            repo.create_flight(flight)
            print("Flight created successfully.")
        except repo.FlightAlreadyExistError as ex:
            print(f"{ex}")
        except repo.DatabaseError as ex:
            print(f"{ex}")
    elif choice == 2:
        print('List of Flights:')
        for flight in repo.read_all_flight():
            print(flight)
    elif choice == 3:
        id = int(input('ID:'))
        flight = repo.read_by_id(id)
        if flight is None:
            print('Flight not found.')
        else:
            print(flight)
    elif choice == 4:
        id = int(input('ID:'))
        flight = repo.read_by_id(id)
        if flight is None:
            print('Flight Not Found')
        else:
            print(flight)
            price = float(input('New Price:'))
            new_flight = {'id': flight['id'],
                          'number': flight['number'],
                          'airline_name': flight['airline_name'],
                          'capacity': flight['capacity'],
                          'price': price,
                          'source': flight['source'],
                          'destination': flight['destination'],
                          'is_active': flight['is_active']}
            repo.update(id, new_flight)
            print('Flight price updated successfully.')
    elif choice == 5:
        id = int(input('ID:'))
        flight = repo.read_by_id(id)
        if flight is None:
            print('Flight Not Found')
        else:
            repo.delete_flight(id)
            print('Flight deleted successfully.')
    elif choice == 6:
        print('Thank you for using Application')
        return choice

def menus():
    choice = menu()
    while choice != 6:
        choice = menu()

menus()
