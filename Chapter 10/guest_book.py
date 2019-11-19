filename = 'guest_book.txt'


active = True
while active:
    guest = input("What is your name? ")
    if guest == "q":
        active = False
    else:
        with open(filename, 'a') as file_object:
            print(f"Welcome, {guest}")
            file_object.write(f"{guest.title()}\n")