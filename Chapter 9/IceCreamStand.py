class Restaurant:
    """Modeling a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine"""
        self.name = restaurant_name
        self.type = cuisine_type
        self.numbered_served = 0

    def describe_restaurant(self):
        """Print a statement about what kind of food the restaurant serves"""
        print(
            f"The restaurant, {self.name.title()}, serves {self.type.title()} food")

    def open_restaurant(self):
        """"Inform people that the restaurant is open"""
        print(f"{self.name.title()} is now open!")

    def set_number_served(self, num):
        self.numbered_served = num

    def increment_number_served(self, inc):
        self.numbered_served += inc


class IceCreamStand(Restaurant):
    """Represent available ice cream flavors"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class"""
        super().__init__(restaurant_name, cuisine_type)

        self.flavors = ['Coffee', 'Mint Chocolate Chip', 'Chocolate', 'Vanilla', 'Black Raspberry']

    def print_flavors(self):
        for flavor in self.flavors:
            print(f"\n{flavor}")


ice_cream = IceCreamStand('Scoops', 'Ice Cream')
ice_cream.print_flavors()

print(ice_cream.name)
print(ice_cream.type)