import json


def read_favorite_number():
    """Reads the users stored favorite number"""

    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        print(f"We could not find {filename}")
        return None
    else:
        print(f"I know your favorite number! It's {favorite_number}")


read_favorite_number()
