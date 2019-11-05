favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python',}

people = ['jen', 'steve', 'edward', 'joe', 'brittany']

for person in people:
    if person in favorite_languages:
        print(f"\n{person.title()}, thank you for taking the poll")
    else:
        print(f"\n{person.title()}, please take the poll")