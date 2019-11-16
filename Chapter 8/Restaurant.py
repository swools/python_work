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


my_restaurant = Restaurant('il portos', 'italian')

print(my_restaurant.numbered_served)
my_restaurant.numbered_served = 5
print(my_restaurant.numbered_served)

my_restaurant.set_number_served(10)
print(my_restaurant.numbered_served)

my_restaurant.increment_number_served(10)
print(my_restaurant.numbered_served)


# your_restaurant = Restaurant('don jose\'s', 'mexican')
# third_restaurant = Restaurant('krave', 'american')
# print(my_restaurant.name.title())
# print(my_restaurant.type.title())

# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

# my_restaurant.describe_restaurant()
# your_restaurant.describe_restaurant()
# third_restaurant.describe_restaurant()
