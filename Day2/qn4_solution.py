names_str = input("Please enter names separated by spaces: ")
names_list = names_str.split()
names_list.sort()
names_tuple = tuple(names_list)

file_name = 'names_data.txt'
with open(file_name, 'w') as writer:
    writer.write(f'Sorted Names List: {names_list}\n')
    writer.write(f'Names Tuple: {names_tuple}\n')
    print(f"\nData successfully saved to '{file_name}'.")

with open(file_name, 'r') as reader:
    read_list_line = reader.readline().strip()
    read_tuple_line = reader.readline().strip()
    print(read_list_line)
    print(read_tuple_line)
