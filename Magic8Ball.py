#This is a magic 8 ball program!

import random

print('Ask me a yes/no question: ')
input()

response = ['It is decidely so.', 'It is certain.', 'Yes.', 'It is unclear. Try again.',
            'Try asking me later.', 'Concentrate and ask again.', 'No.',
            'The outcome does not look good.', 'It is very doubtful.']

print(response[random.randint(0,8)])
