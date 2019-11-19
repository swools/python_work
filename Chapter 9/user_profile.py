def build_profile(first, last, location, age, nickname):
    """Build a dictionary containing everything we know about a user."""
    user_info = dict()
    user_info['first_name'] = first
    user_info['last_name'] = last
    user_info['location'] = location
    user_info['age'] = age
    user_info['nickname'] = last
    return user_info
