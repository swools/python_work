glossary = {
    'dictionary': 'a collection of key value pairs',
    'list': 'a collection of items in a particular order',
    'if-elif-else': 'shorthand for an if, elif, else statement',
    'string': 'a series of characters. anything inside quotes is considered a string',
    'boolean': 'boolean is a data type that is either True or False'
}

for word in glossary:
    print(f"{word.title()}:\n\t{glossary[word].capitalize()}.\n")

print(f"{glossary.keys()}\n")
print(f"{glossary.values()}\n")
print(f"{glossary.items()}\n")
