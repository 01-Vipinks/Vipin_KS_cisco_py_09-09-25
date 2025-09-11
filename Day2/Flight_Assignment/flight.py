import json
import pickle

class Flight:
    def __init__(self, id, number, airline_name, seats, price, source, destination):
        self.id = id
        self.number = number
        self.airline_name = airline_name
        self.seats = seats
        self.price = price
        self.source = source
        self.destination = destination

    def to_dict(self):
        return {"id": self.id,
            "number": self.number,
            "airline_name": self.airline_name,
            "seats": self.seats,
            "price": self.price,
            "source": self.source,
            "destination": self.destination}

def save_to_json(flights, filename="flights.json"):
    with open(filename, "w") as f:
        json.dump([flight.to_dict() for flight in flights], f, indent=4)
    print(f"Flights saved to {filename}")

def load_from_json(filename="flights.json"):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

def save_to_binary(flights, filename="flights.dat"):
    with open(filename, "wb") as f:
        pickle.dump(flights, f)
    print(f"Flights saved to {filename} (binary)")

def load_from_binary(filename="flights.dat"):
    with open(filename, "rb") as f:
        flights = pickle.load(f)
    return flights

flights = []
n = int(input("Enter number of flights: "))

for i in range(n):
    print(f"\nEnter details for flight {i+1}:")
    id = int(input("ID: "))
    number = input("Flight Number: ")
    airline_name = input("Airline Name: ")
    seats = int(input("Seats: "))
    price = float(input("Price: "))
    source = input("Source: ")
    destination = input("Destination: ")
    flights.append(Flight(id, number, airline_name, seats, price, source, destination))

save_to_json(flights)
print("From JSON:", load_from_json())

save_to_binary(flights)
binary_flights = load_from_binary()
print("From Binary:", [f.to_dict() for f in binary_flights])