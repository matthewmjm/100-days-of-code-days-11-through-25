# # https://replit.com/@appbrewery/higher-lower-final?embed=1&output=1#main.py
# print("Compare A: ")
# print("Against B: ")
# input("Who has more followers? Type 'A' or 'B': ")
# print("You are right!  Current score: 1.")
# print("Sorry, that's wrong.  Final Score: 2")

import random
from art import logo
from os import system, name
from time import sleep

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()
print(logo)