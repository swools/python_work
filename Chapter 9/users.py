class User:
    """ Store information about each user """

    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location.title()
        self.full_name = f"{self.first_name} {self.last_name}"
        self.login_attempts = 0

    def describe_user(self):
        print(
            f"\nFirst Name: {self.first_name}\nLast Name: {self.last_name}\nAge: {self.age}\nLocation: {self.location}")

    def greet_user(self):
        print(f"Welcome, {self.full_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges:
    """Store list of a users privileges"""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print(f"{privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        """Initialize attributes of the parent class"""
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()
        




# admin = Admin('steve', 'wool', 28, 'new jersey')
# print(f"\n{admin.full_name} is an admin and has the following privileges")
# admin.privileges.show_privileges()





