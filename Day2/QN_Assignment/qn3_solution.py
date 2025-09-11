sentence = input("Please enter a sentence: ")
word_list = sentence.split()
uppercase_word_tuple = tuple(word.upper() for word in word_list)

file_name = 'sentence_data.txt'
with open(file_name, 'w') as writer:
    writer.write(f'Original Word List: {word_list}\n')
    writer.write(f'Uppercase Word Tuple: {uppercase_word_tuple}\n')
    print(f"\nData successfully saved to '{file_name}'.")
    
    print(f"\nReading data from '{file_name}':")
with open(file_name, 'r') as reader:
        read_list_line = reader.readline().strip() # .strip() removes trailing newline
        read_tuple_line = reader.readline().strip()
        print(read_list_line)
        print(read_tuple_line)
