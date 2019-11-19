filename = 'programming_poll.txt'

active = True
while active:
    prompt = input("Why do you love programming? ")
    if prompt == 'q':
        active = False
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{prompt}.\n")
