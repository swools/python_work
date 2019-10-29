toppings = ["Buffalo Chicken", "Cherry Peppers", "Pepperoni"]

# for topping in toppings:
#     print(f"I like {topping} pizza.")

# print("I really like pizza!")

friend_pizza = toppings[:]

friend_pizza.append("Ham")

print("My favorite pizzas are")
for pizza in toppings:
    print(pizza)

print("\nMy Friends favorite pizzas are")
for pizza in friend_pizza:
    print(pizza)
