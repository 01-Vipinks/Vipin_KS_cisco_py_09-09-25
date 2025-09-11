import json
flight={'flight_number': '1700', 'airline': 'Indigo',
        'capacity':225,'price':4500,
        'source':'Bangalore', 'destintion':'Hyderabad'}
file_name='flight.json'

print('Before file:', flight)
with open(file_name, 'w') as writer:
    json.dump(flight, writer)  #flight is written byte by byte into flight.dat
    print("Saved the flight to file")

with open(file_name, 'r') as reader:
    flight_from_file=json.load(reader)  #the byte by byte from the file is read from flight.dat and converted as flight object
    print('Flight after read from file:', flight_from_file)