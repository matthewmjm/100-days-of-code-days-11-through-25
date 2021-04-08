import random
from art import logo
from os import system, name
from time import sleep

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# to clear terminal window
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# to chose a card at random
def deal_card():
    card_index = random.randint(0, 12)
    card_dealt = cards[card_index]
    return card_dealt



you_go = True

#start game
print(logo)
sleep(1)
clear()
play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play_game == 'y':
    my_cards = []
    my_score = 0
    computer_cards = []
    computer_score = 0
    my_cards.append(deal_card())
    my_cards.append(deal_card())
    my_score = sum(my_cards) 
    computer_cards.append(deal_card())
    computer_score = sum(computer_cards)
    print(logo)
    print(f" Your cards: [{my_cards}, current score: {my_score}")
    print(f" Computer's first card: {computer_score}")
    hit_me = input("Type 'y' to get another card, type 'n' to pass: ")