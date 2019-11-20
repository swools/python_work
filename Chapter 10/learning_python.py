filename = 'Chapter 10/learning_python.txt'

with open(filename) as file_object:
    contents_list = file_object.readlines()

for line in contents_list:
    print(line.strip())

with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

with open(filename) as file_object:
    contents = file_object.read()

print(contents)
