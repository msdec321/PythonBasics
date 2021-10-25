#! python3

#This is the bullet point adder script.
#Copy a list of items to the clipboard and add a * and whitespace to the front.

import pyperclip

'''
This is the first item.
This is the second item.
This is the third item.
'''

def bulletPoint(List):

    splitList = List.split('\n')
    splitList[0] = f"* {splitList[0]}"
    newList = '\n* '.join(splitList)
    return newList


myList = pyperclip.paste()
print(myList)

bulletList = bulletPoint(myList)

print(bulletList)
