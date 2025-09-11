numbers_str=input("Numbers (space separated):")
numbers_list=[int(num_str) for num_str in numbers_str.split()]
print(numbers_list)
num_sum=sum(numbers_list)
num_avg=num_sum/len(numbers_list)
print(num_sum)
print(num_avg)


file_name='numbers_data.txt'
with open(file_name, 'w') as writer:
    writer.write(f'List: {numbers_list}\n')
    writer.write(f'Tuple: {num_sum}\n')
    writer.write(f'Average: {num_avg}')

with open(file_name, 'r') as reader:
    line_list=reader.readline()
    line_sum=reader.readline()
    line_tuple=reader.readline()
    print(line_list)
    print(line_tuple)
