from user import User

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