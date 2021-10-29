#! python3

#This is a tutorial on validating inputs from the user.

#Writing input validation from scratch is long and tedious, but made easier
#   using the PyInputPlus module.

import pyinputplus as pyip

'''
List of built-in functions:
inputStr()
inputNum() - Ensures user enters a number (int or float)
  inputInt()
  inputFloat()
inputChoice() -Ensures user enters a provided choice
inputMenu() - Provides a menu with numbered or lettered options
inputDatetime() -Ensures user enters a date and time
inputYesNo() - Ensures user enters "yes" or "no"
inputBool() - Takes "True" or "False"
inputEmail() - Ensures user enters a valid email address
inputFilepath() - Ensures user enters a valid file path (and can check if exists)
inputPassword() -
'''

#Min, max, gthan, lthan arguments
pyip.inputNum('Enter num gthan 3:', min=4)  #greaterThan=4, lessThan=4...

#By default blank input isn't allowed unless set to true.
pyip.inputNum('Enter num or blank: ', blank=True)

#Limit (number of attempts before giving up), timeout (seconds), default arguments
pyip.inputNum('Enter num, two tries: ', limit=2)
pyip.inputNum('Enter num, ten seconds: ', timeout=10)

#Pyip also supports regular expressions with allowRegexes or blockRegexes
pyip.inputNum('Enter num as Roman numerals (IXXLCDM): ', allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
pyip.inputNum("Enter num that doesn't end in an even number: ", blockRegexes=[r'[02468]$'])


#Custom validation functions via inputCustom()
#For example, input a set of numbers that adds up to ten.
#inputCustom also supports the other pyip method arguments.
def addsToTen(numbers):
    numbersList = list(numbers)
    for i,digit in enumerate(numbers):
        numbersList[i] = int(digit)
    if sum(numbersList)!=10:
        raise Exception(f'The digits must add up to ten, not {sum(numbersList)}.')

    return int(numbers)

response = pyip.inputCustom(addsToTen)


















