# Number Guessing Game in Python

'''This Python program implements a simple number guessing game using the random module.
The program randomly generates a number between 1 and 100,
and the user is asked to guess the number.'''


import random

number = random.randint(1, 100)
guesses = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    guesses += 1

    if guess > number:
        print("Lower number please")
    elif guess < number:
        print("Higher number please")
    else:
        print(f"You guessed the number {number} correctly in {guesses} attempts!")
        break
