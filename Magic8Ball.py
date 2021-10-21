#This is a magic 8 ball program!

import random

print('Ask me a yes/no question: ')
response = random.randint(0,8)
input()

def eight_ball(response):
    if response == 0: answer = 'It is decidely so.'
    elif response == 1: answer = 'It is certain.'
    elif response == 2: answer = 'Yes.'
    elif response == 3: answer = 'It is unclear. Try again.'
    elif response == 4: answer = 'Try asking me later.'
    elif response == 5: answer = 'Concentrate and ask again.'
    elif response == 6: answer = 'No.'
    elif response == 7: answer = 'The outcome does not look good.'
    else: answer = 'It is very doubtful.'

    return answer

print(eight_ball(response))
