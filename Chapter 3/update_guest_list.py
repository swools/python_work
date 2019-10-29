guests = ['Aaron Sorkin', 'Drake', 'Aaron Judge']

print(f"{guests[0]}, would you like to come to a dinner party?")
print(f"{guests[1]}, would you like to come to a dinner party?")
print(f"{guests[2]}, would you like to come to a dinner party?")

print(f"{guests.pop(1)}, cannot make it to the party.")

guests.append('Ryan Gosling')

for guest in guests:
    print(f"{guest}, would you like to come to a dinner party?")
