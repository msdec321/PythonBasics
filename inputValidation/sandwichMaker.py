#! python3

#This is the sandwich maker script.
# bread: inputMenu(wheat, white, sourdough)
# protein: inputMenu(chicken, turkey, ham, tofu)
# cheese: inputYesNo()
#       : Yes: inputMenu(cheddar, Swiss, mozarella)
# Mayo, Mustard, Lettuce, Tomato: inputYesNo()
#nSandwiches: inputNum(min=1)
#Come up with a cost for eat and display the total price at the end.

import pyinputplus as pyip

print('Welcome to the sandwich maker! How would you like your sandwich made?')

prices = {'wheat': 0.70, 'white': 0.55, 'sourdough': 1.15,
          'chicken': 1.25, 'turkey': 1.50, 'ham': 1.50, 'tofu': 1.20,
          'cheddar': 1.15, 'swiss': 1.25, 'mozarella': 1.20}

totalCost = 0.00

print('Please choose a type of bread: ')
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'])
if bread in prices: totalCost+=prices[bread]

print('Please choose a type of protein: ')
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
if protein in prices: totalCost+=prices[protein]

print('Would you like cheese?')
cheeseYesNo = pyip.inputYesNo()
if cheeseYesNo == 'yes':
    print('Please choose a type of cheese: ')
    cheese = pyip.inputMenu(['cheddar', 'swiss', 'mozarella'])
    if cheese in prices: totalCost+=prices[cheese]

print('Would you like mayo?')
mayoYesNo = pyip.inputYesNo()
if mayoYesNo == 'yes':
    totalCost+=0.35

print('Would you like mustard?')
mustardYesNo = pyip.inputYesNo()
if mustardYesNo == 'yes':
    totalCost+=0.35

print('Would you like lettuce?')
lettuceYesNo = pyip.inputYesNo()
if lettuceYesNo == 'yes':
    totalCost+=0.25

print('Would you like tomato?')
tomatoYesNo = pyip.inputYesNo()
if tomatoYesNo == 'yes':
    totalCost+=0.30

numSandwiches = pyip.inputNum('How many sandwiches would you like? ', min=1)

print('Thank you for your purcase!')
print(f'Your total cost is ${numSandwiches*totalCost}.')
