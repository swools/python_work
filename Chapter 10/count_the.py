def count_the(list):
    for file in list:
        try:
            with open(file, 'r') as f:
                contents = f.read()
        except FileNotFoundError:
            print(f"{file} could not be found")
        else:
            thes = contents.lower().count('the ')
            print(f"The word 'the' appears {thes} times in {file}")


books = ['dracula.txt', 'hounds_of_baskerville.txt',
         'count_of_monte_cristo.txt']

count_the(books)
