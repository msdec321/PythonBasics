#!/usr/bin/env python3

'''
4_blackjack.py - Blackjack, also known as 21, is a card game where players try to get as close to 21 points as
possible without going over. This program uses images drawn with text characters, called ASCII art. American Standard
Code for Information Interchange (ASCII) is a mapping of text characters to numeric codes that computers used before
Unicode replaced it.
'''

import pyinputplus as pyip
import random, time, sys

print("""
    Rules:
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      In case of a tie, the bet is returned to the player.
      The dealer stops hitting at 17.
      """)

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

money = 5000
CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'J', 'Q', 'K']
SUITS = [HEARTS, DIAMONDS, SPADES, CLUBS]


def print_card(card_num, card_face: chr, card_total: int) -> int:

    card_line1 = ''
    card_line2 = ''
    card_line3 = ''
    card_line4 = ''

    #Draw the card ASCII.
    for i, item in enumerate(card_num):
        card_line1 += ' ____    '

        if card_num[-i]!=10:
            card_line2 += '|' + str(card_num[-i]) + '   |   '
        else:
            card_line2 += '|' + str(card_num[-i]) + '  |   '

        card_line3 += '| ' + card_face[-i] + '  |   '

        if card_num[-i]!=10:
            card_line4 += '|___' + str(card_num[-i]) + '|   '
        else:
            card_line4 += '|__' + str(card_num[-i]) + '|   '

    card = [card_line1, card_line2, card_line3, card_line4]

    #Print the card ASCII to the shell.
    for line in card:
        print(line)

    if   card_num[-1] in ['J', 'Q', 'K']: card_total += 10  #Face cards are 10 points.
    elif card_num[-1] == 'A':  #Ace is worth either 1 or 11 points.
        if card_total + 11 > 21: card_total += 1
        else: card_total += 11
    else: card_total += card_num[-1]
    return card_total


print(f'Money: {money}')

bet = pyip.inputNum(f'How much do you bet? (1-{money}) ', min = 1, max = money)
print(f'Bet: {bet}')

#Main game loop
while True:
    i = 0

    player_card_num = []
    player_card_face = []
    player_total = 0

    dealer_card_num = []
    dealer_card_face = []
    dealer_total = 0

    cards_played = []

    dealer_flag = 0
    player_flag = 0

    while True:

        #Pick a unique card from the deck.
        while True:
            card_num = random.choice(CARDS)
            card_face = random.choice(SUITS)
            card = str(random.choice(CARDS))+"of"+random.choice(SUITS)

            if card not in cards_played:
                cards_played.append(card)
                break

        #Dealer's turn
        if i % 2 == 0 and dealer_flag == 0:
            print("Dealer's turn")

            dealer_card_num.append(card_num)
            dealer_card_face.append(card_face)

            dealer_total = print_card(dealer_card_num, dealer_card_face, dealer_total)
            print(f'Dealer score: {dealer_total}')

            if dealer_total == 21:
                print(f"Dealer's total: {dealer_total}. You lose!")
                money -= bet
                break

            elif dealer_total > 21:
                print(f"Dealer's total: {dealer_total}. Dealer busted! You win!!")
                money += 2*bet
                break

            if dealer_total >= 17:
                dealer_flag = 1
                i += 1
                continue

            i += 1
            time.sleep(2)

        #Player's turn
        elif i % 2 != 0 and player_flag == 0:
            print("Player's turn")

            player_card_num.append(card_num)
            player_card_face.append(card_face)

            player_total = print_card(player_card_num, player_card_face, player_total)
            print(f'Player score: {player_total}')

            if player_total == 21:
                print(f"Player's total: {player_total}. You win!!")
                money += 2 * bet
                break

            elif player_total > 21:
                print(f"Player total: {player_total}. Player busted! You lose!")
                money -= bet
                break

            print('(H)it or (S)tay?')
            choice = input()

            if choice == 'H':
                i += 1
                continue

            else:
                player_flag = 1
                i += 1
                continue

        else: i+=1

        #If Player and Dealer choose to Stay, compare scores
        if dealer_flag == 1 and player_flag == 1:
            if dealer_total > player_total:
                print(f"Dealer's total: {dealer_total}. Player's total: {player_total}. You lose!")
                money -= bet

            elif dealer_total < player_total:
                print(f"Dealer's total: {dealer_total}. Player's total: {player_total}. You win!!")
                money += 2 * bet

            else:
                print(f"Dealer's total: {dealer_total}. Player's total: {player_total}. It's a tie!")

            break



    print(f'Money: {money}')

    if money == 0:
        print('You ran out of money! Thanks for playing!')
        sys.exit()

    choice = pyip.inputYesNo(f'Play again? (y/n): ')
    if choice.lower() == 'yes':
        bet = pyip.inputNum(f'How much do you bet? (1-{money}) ', min = 1, max = money)
        print(f'Bet: {bet}')
        continue
    else:
        print('Thanks for playing!')
        sys.exit()



