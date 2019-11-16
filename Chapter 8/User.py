class User:
    """ Store information about each user """

    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.location = location.title()
        self.full_name = f"{self.first_name} {self.last_name}"

    def describe_user(self):
        print(
            f"\nFirst Name: {self.first_name}\nLast Name: {self.last_name}\nAge: {self.age}\nLocation: {self.location}")

    def greet_user(self):
        print(f"Welcome, {self.full_name}")


new_user = User('steve', 'wool', 28, 'new jersey')
another_user = User('brittany', 'wool', 29, 'new jersey')

new_user.describe_user()
new_user.greet_user()

another_user.describe_user()
another_user.greet_user()
