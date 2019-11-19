from random import choice

lottery = [1, 2, 3, 4, 5, 6, 7, 9, 10, 'A', 'B', 'C', 'D', 'E']
my_ticket = ['A', 3, 'E', 4]
counter = 0
results = list()

while my_ticket != results:
    results = []
    
    for i in range(1, 5):
        results.append(choice(lottery))
        counter += 1
print(f"{results} is the winning ticket! The loop had to run {counter} times in order to win!")
