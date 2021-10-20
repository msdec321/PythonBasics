#This is the main guessing game script.
import random

N, guess = 100, -1

#Computer picks a random number from 0 to N.
cpu = random.randint(0,N)

while guess!=cpu:
    print('Guess a number from 1 to ', str(N)+': ')

    #User inputs a guess.
    guess = int(input())

    #Loops through guesses until user is correct.
    if guess<cpu: print(f'The number is larger than ', str(guess)+'!')
    elif guess>cpu: print(f'The number is smaller than ', str(guess)+'!')
    else: print(f'The number is ', str(guess)+'!')
