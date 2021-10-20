import random

#Create a list of strings for options 'Rock', 'Paper', 'Scissors'
choices = ['rock', 'paper', 'scissors']

#Have the computer randomly pick one.
cpu = random.randint(0,2)

#Loop through the game until a winner is decided.
while True:
    print('Choose rock, paper, or scissors: ')
    user = input()

    if user==choices[cpu]:
        print('The computer chose ', str(choices[cpu])+', the game is a Draw.')

    elif (user=='rock' and cpu==2) or (user=='paper' and cpu==0) or (user=='scissors' and cpu==1):
        print('The computer chose ', str(choices[cpu])+', you win!')
        break

    else:
        print('The computer chose ', str(choices[cpu])+', you lose!')
        break
