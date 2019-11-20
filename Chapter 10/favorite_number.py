import json


def get_favorite_number():
    """Gets a users favorite number and stores it"""

    favorite_number = input("What is your favorite number? ")
    try:
        favorite_number = int(favorite_number)
    except ValueError:
        print("You did not enter a valid number")
    else:
        filename = 'favorite_number.json'
        with open(filename, 'w') as f:
            json.dump(favorite_number, f)


def get_stored_number():
    """Gets users favorite number if it's already stored"""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite_number


def read_favorite_number():
    """Reads the users stored favorite number if found"""

    favorite_number = get_stored_number()
    if favorite_number:
        print(f"I know your favorite number! It's {favorite_number}")
    else:
        get_favorite_number()


read_favorite_number()
