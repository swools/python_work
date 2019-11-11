results = dict()

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    destination = input("If you could visit one place in the world, where would you go? ")
    results[name] = destination

    repeat = input("Would you like to let another person respond? (yes/no)")

    if repeat == "no":
        polling_active = False

for name, destination in results.items():
    print(f"\n{name.title()} would like to visit {destination.title()}.")