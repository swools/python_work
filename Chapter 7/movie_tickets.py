# < 3 ticket is free
# < 13 ticket is $10
# else ticket is $15

prompt = "How old are you? "

while True:
    age = input(prompt)
    try:
        int(age)
        if int(age) < 3:
            cost = "Free"
        elif int(age) <= 12:
            cost = "$12"
        elif int(age) > 12:
            cost = "$15"
        print(f"Your ticket will be {cost}")
    except:
        if age == "quit":
            break
        else:
            print("Invalid input. Please enter a number.")


    