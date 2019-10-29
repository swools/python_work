my_foods = ["Pizza", "Boneless Wings", "Pasta"]
friends_foods = my_foods[:]


friends_foods.append("Tacos")
my_foods.append("Chicken Parm")

for food in my_foods:
    print(food)
print("")
for food in friends_foods:
    print(food)
