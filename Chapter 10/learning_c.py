filename = 'learning_c.txt'

with open(filename) as file_object:
    for line in file_object:
        line = line.replace('Python', 'C')
        print(line)