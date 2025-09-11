numbers_str = input("Please enter numbers separated by spaces: ")
numbers_list = [int(num_str) for num_str in numbers_str.split() if num_str.strip()]
max_value = max(numbers_list)
min_value = min(numbers_list)

file_name = 'minmax_data.txt'
with open(file_name, 'w') as writer:
    writer.write(f'Numbers List: {numbers_list}\n')
    writer.write(f'Maximum Value: {max_value}\n')
    writer.write(f'Minimum Value: {min_value}\n')
print(f"\nData successfully saved to '{file_name}'.")

print(f"\nReading data from '{file_name}':")
with open(file_name, 'r') as reader:
    read_list_line = reader.readline().strip()
    read_max_line = reader.readline().strip()
    read_min_line = reader.readline().strip()
            
    print(read_list_line)
    print(read_max_line)
    print(read_min_line)
