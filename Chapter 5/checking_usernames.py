current_users = ["steve wool", "mike lloyd",
                 "joe wool", "matt kelly", "jesse franks"]
current_users_lower = [user.lower() for user in current_users]

new_users = ["michelle kelly", "aaron kelly",
             "brittany wool", "steve wool", "Joe Wool"]

for user in new_users:
    if user.lower() in current_users_lower:
        print("Username is taken. Please choose a new username")
    else:
        print("That username is available")
