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

def computer_play(computer_score, computer_cards):
    while computer_score < 22:
        computer_cards.append(deal_card())
        computer_score = sum(computer_cards)
    print(f" Computer's final hand: [{computer_cards}, final score: {computer_score}")
    return computer_score, computer_cards

def you_play(my_score, my_cards):
    while my_score < 22:
        my_cards.append(deal_card())
        my_score = sum(my_cards)
        print(f" Your cards: [{my_cards}, current score: {my_score}")
        return my_score, my_cards

#start game
print(logo)
sleep(1)
clear()
my_cards = []
my_score = 0
computer_cards = []
computer_score = 0
play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play_game == 'y':
    my_turn = True
    my_cards.append(deal_card())
    my_cards.append(deal_card())
    my_score = sum(my_cards) 
    computer_cards.append(deal_card())
    computer_score = sum(computer_cards)
    print(logo)
    print(f" Your cards: [{my_cards}, current score: {my_score}")
    print(f" Computer's first card: {computer_score}")
    hit_me = input("Type 'y' to get another card, type 'n' to pass: ")
    if hit_me == 'n':
        computer_play(computer_score, computer_cards)
    else:
        you_play(my_score, my_cards)
print(my_cards, " ", my_score)
print(computer_cards, " ", computer_score)




# print(my_cards)
# print(my_score)
# print(computer_cards)
# print(computer_score)

    #         while computer_score < 22:
    #             computer_score.append(deal_card())
    #             computer_score = sum(computer_cards)
    #         my_turn = False
    #     if hit_me == 'y':
    #         my_cards.append(deal_card())
    #         my_score = sum(my_cards)
    #         print(f" Your cards: [{my_cards}, current score: {my_score}")
    #         print(f" Computer's first card: {computer_score}")
    #         hit_me = input("Type 'y' to get another card, type 'n' to pass: ")
    #         while my_score < 22:
    #             my_cards.append(deal_card())
    #             my_score = sum(my_cards)
    #             print(f" Your cards: [{my_cards}, current score: {my_score}")

    # while my_turn:
    #     if hit_me == 'n':
    #     else:
    #             print(f" Computer's first card: {computer_score}")
    # print('stop')
