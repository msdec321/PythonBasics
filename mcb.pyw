#! python3

#This is the updatable multi-clipboard script.
#This script uses the shelve module to save new strings without having to edit the script.
#For example, "py3 mcb.pyw save spam" will save the clipboard string to the keyword "spam",
#  and later loaded with "py3 mcb.pyw spam".
#The user can also copy a list of keywords with "py3 mcb.pyw list" to the clipboard.
#It is run as a ".pyw" file rather than a ".py" file.

import shelve, pyperclip, sys
from pprint import pprint

#clipboard = {'spam': 'This is spam!', 'eggs': 'These are eggs!'}

if sys.argv[1]=="list":
    clipboardShelf = shelve.open('clipboard')
    for key in clipboardShelf:
        print('keyword: ', key, ', value: ', clipboardShelf[key])
    clipboardShelf.close()

elif len(sys.argv)==3 and sys.argv[1]=="save" and sys.argv[2].isalnum():
    clipboardShelf = shelve.open('clipboard')
    clipboardShelf[sys.argv[2]] = pyperclip.paste()
    clipboardShelf.close()

elif len(sys.argv)==2:
    clipboardShelf = shelve.open('clipboard')

    if sys.argv[1] in clipboardShelf.keys():
        pyperclip.copy(clipboardShelf[sys.argv[1]])
        print(f'{sys.argv[1]} value copied to clipboard!')
    else:
        print(f'{sys.argv[1]} is not a saved keyword. To save, type python3 mcb.pyw save {sys.argv[1]}.')
    clipboardShelf.close()

else:
    print('Error: Incorrect command line argument.')
    print('Option 1: save <keyword> - saves clipboard to keyword.')
    print('Option 2: <keyword> - copies keyword value to clipboard.')
    print('Option 3: list - copies full list of key-value pairs to clipboard.')
