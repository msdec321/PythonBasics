#! python3

#This is the "Keep an idiot busy for hours" script.
#This script prompts the user if it wants to keep an idiot busy for hours.
#If "no", quit. If "yes", ask again.

import pyinputplus as pyip

while True:
    prompt = 'Want to keep an idiot busy for hours? '
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        print('Have a good day!')
        break
