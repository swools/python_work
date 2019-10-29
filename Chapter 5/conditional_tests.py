favorite_food = "Boneless Wings"
print(favorite_food == "Boneless Wings")

num_string = "10"
print(num_string == 10)

print(int(num_string) == 10)


#strings
string = "This is a string"
print(string == "This is a string")
print(string == "this is a string")

print(string.lower() == "this is a string")
print(string.lower() == "This is a string")

age = 28
print("")
print(age == 28) #True
print(age > 30) #False
print(age < 30) #True
print(age >= 28) #True
print(age <= 27) #False

num = 40
print(num > 30 and num <= 100)

list = ["Pizza", "Wings", "Chicken"]

if "Pizza" in list:
    print(True)

print("")

if "Lasagna" in list:
    print(True)

if "Lasange" not in list:
    print(True)
