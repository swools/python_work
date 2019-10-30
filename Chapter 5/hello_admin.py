users = []

if users:
    for user in users:
        if user == "admin":
            print(
                f"Hello {user.title()}. Would you like to see a status report")
        else:
            print(f"Hello {user.title()}. Thanks for logging in again")
else:
    print("We need to find some users")
