#! python3

#This is the coin toss debugger. The script started with bugs and debugging was performed on it.

import random, logging
logging.basicConfig(filename='coinTossLog.txt', level=logging.DEBUG, format=' %(asctime)s -  %(levelname) s -  %(message)s')
logging.debug('Start of program')


guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug(f'User guess: {guess}')

toss = random.randint(0, 1) # 0 is tails, 1 is heads

#Bug fix
if toss == 0: toss='tails'
else: toss='heads'
logging.debug(f'Coin toss: {toss}')

if toss == guess:
    print('You got it!')

else:
    print('Nope! Guess again!')
    guesss = input()
    logging.debug(f'User guess: {guess}')

    if toss == guess:
        print('You got it!')

    else:
        print('Nope. You are really bad at this game.')

logging.debug('End of program.')
