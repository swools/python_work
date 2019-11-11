sandwiches = ["Pastrami", "Italian Combo", "Buffalo Chicken", "Ham and Cheese", "Chicken Cutlet", "Pastrami", "Pastrami"]
finished_sandwiches = list()

print("We have run out of Pastrami\n")

while "Pastrami" in sandwiches:
    sandwiches.remove("Pastrami")

while sandwiches:
    sandwich = sandwiches.pop()
    print(f"I made your {sandwich}.")
    finished_sandwiches.append(sandwich)

print("The following sandwiches have been made...\n")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich}")
