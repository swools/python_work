guests = ['Aaron Sorkin', 'Drake', 'Aaron Judge']

print(f"{guests[0]}, would you like to come to a dinner party?")
print(f"{guests[1]}, would you like to come to a dinner party?")
print(f"{guests[2]}, would you like to come to a dinner party?")

print(f"{guests.pop(1)}, cannot make it to the party.")

guests.append('Ryan Gosling')

for guest in guests:
    print(f"{guest}, would you like to come to a dinner party?")

print("I found a bigger dinner table")

guests.insert(0, "Daniel Jones")
guests.insert(len(guests) // 2, "Eli Manning")
guests.append("Robert Downey Jr.")

for guest in guests:
    print(f"{guest}, would you like to come to a dinner party?")

print("I can only invite two people")

print(f"{guests.pop()}, I'm sorry I cannot invite you to dinner")
print(f"{guests.pop()}, I'm sorry I cannot invite you to dinner")
print(f"{guests.pop()}, I'm sorry I cannot invite you to dinner")
print(f"{guests.pop()}, I'm sorry I cannot invite you to dinner")

for guest in guests:
    print(f"{guest}, you are still invited")
print(guests)

del guests[0]
del guests[0]
print(guests)
