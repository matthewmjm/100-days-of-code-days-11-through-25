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
        my_turn = False
        while computer_score < 21 and computer_score < my_score:
            computer_cards.append(deal_card())
            computer_score = sum(computer_cards)
    else:
        while my_turn:
            my_cards.append(deal_card())
            my_score = sum(my_cards)
            print(f" Your cards: [{my_cards}, current score: {my_score}")
            print(f" Computer's first card: {computer_score}")
            if my_score > 21:
                my_turn = False
            else: 
                hit_me = input("Type 'y' to get another card, type 'n' to pass: ")
                if hit_me != 'y':
                    while computer_score < 21 and computer_score < my_score:
                        computer_cards.append(deal_card())
                        computer_score = sum(computer_cards)
                    my_turn = False
    if my_score > 21 and computer_score < 22:
        print(f"\n Your final hand: {my_cards}, final score: {my_score}")
        print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
        print("You went over.  You lose! 😭")
    elif my_score < 22 and computer_score > 21:
        print(f"\n Your final hand: {my_cards}, final score: {my_score}")
        print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
        print("Opponent went over.  You win! 😁")
    elif my_score < 22 and my_score > computer_score:
        print(f"\n Your final hand: {my_cards}, final score: {my_score}")
        print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
        print("You win 😃")
    elif computer_score < 22 and computer_score > my_score:
        print(f"\n Your final hand: {my_cards}, final score: {my_score}")
        print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
        print("You lose 😤")
    else:
        print(f"\n Your final hand: {my_cards}, final score: {my_score}")
        print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
        print("It is a draw! 🙃")




# def me_over():
#     print(f"\n Your final hand: {my_cards}, final score: {my_score}")
#     print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
#     print("You went over.  You lose! 😭")

# def computer_over():
#     print(f"\n Your final hand: {my_cards}, final score: {my_score}")
#     print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
#     print("Opponent went over.  You win! 😁")

# def draw():
#     print(f"\n Your final hand: {my_cards}, final score: {my_score}")
#     print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
#     print("Opponent went over.  You win! 😁")



# print(my_cards)
# print(my_score)
# print(f" Your final hand: {my_cards}, final score: {my_score}")
# print(computer_cards)
# print(computer_score)
# print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")