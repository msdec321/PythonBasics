#!/usr/bin/env python3

# bagels.py - In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues. The game offers one of the following hints in response to your guess: “Pico” when your guess has a correct digit in the wrong place, “Fermi” when your guess has a correct digit in the correct place, and “Bagels” if your guess has no correct digits. You have 10 tries to guess the secret number.

import random
import pyinputplus as pyip

num = random.randint(100,999)

for i in range(10):

    guess = pyip.inputNum("Guess a number from 100-999: ", min = 100, max = 999)

    numStr = str(num)
    guessStr = str(guess)

    if guess == num:
        print(f"You win! The number was {num}.")
        break

    for j in range(3):
        if guessStr[j] == numStr[j]: print("Fermi")
        if (guessStr[j] != numStr[j] and (guessStr[j] in numStr)): print("Pico")

    if (guessStr[0] not in numStr) and (guessStr[1] not in numStr) and (guessStr[2] not in numStr): print("Bagel")

    if i == 9:
        print(f'Oh no! You ran out of guesses! The number was {num}.')
