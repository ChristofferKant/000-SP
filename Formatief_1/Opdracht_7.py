"""Bron Introduction to Computing Using Python Second Edition blz. 186, 187 & 193"""

# Poging 1, set is unorderded, not random
""" 
def random_number(n):
    numbers = set()
    for number in range(1, n):
        numbers.add(number)
        random = numbers.pop()

    while True:
        guess = int(input("Guess a number: "))
        if guess < random:
            print("Too low")
        elif guess > random:
            print("Too high")
        else:
            print("Bingo!")
            break  """

import random
def random_number(n):
    rando = random.randrange(1, n)
    while True:
        guess = int(input("Guess a number: "))
        if guess < rando:
            print("Too low")
        elif guess > rando:
            print("Too high")
        else:
            print("Bingo!")
            break

random_number(100)