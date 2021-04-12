#Number Guessing Game
import random
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

THE_NUMBER = random.randint(1, 101)
you_won = False

clear()
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy' or difficulty == 'e':
    attempts = int(10)
    print("\nYou have 10 attempts remaining to guess the number.")
else:
    attempts = int(5)
    print("\nYou have 5 attempts remaining to guess the number.")

while attempts >= 1:
    guess = int(input("Make a guess: "))
    if guess > THE_NUMBER:
        print("Too high.\nGuess again.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining.\n")
    elif guess < THE_NUMBER:
        print("Too low.\nGuess again.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining.\n")
    elif guess == THE_NUMBER:
        print(f"You got it!  The answer was {THE_NUMBER}")
        you_won = True
        attempts = 0

if not you_won:
    print(f"You've run out of guesses, you lose! The answer was {THE_NUMBER}")
