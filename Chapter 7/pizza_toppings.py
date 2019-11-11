prompt = "What would you like on your pizza? "


active = True
while active:
    topping = input(prompt)

    if topping == "quit":
        active = False
    else:
        print(f"Adding {topping} to your pizza")