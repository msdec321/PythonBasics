#This is a tutorial on handling string objects in various ways.

#To use ' in a string, use double-quotes. Ex. Alice's cat.
print("That is Alice's cat.")

#To use both ' and " in a string, use escape characters (\).
print('That is Alice\'s cat')

#To newline, use \n.
print('Hello there!\nHow are you?\nI\'m fine!')

#To ignore escape characters, use a raw string. Useful for printing URLs.
print(r'Hello there!\nHow are you?')

#Multistrings. ''' To have newlines, whitespace etc be part of the string.
print('''This is
a multi string
sentence.''')


#Slicing strings.
#String objects use indexing the same way lists do.
myString = "Hello world!"
print(myString[4])
print(myString[4:8])
print("Hello" not in myString)

#String interpolation. Instead of writing out:
print(myString + ", is a string that I wrote!")
#We can write an interpolation:
print('%s, is a string that I wrote!' % (myString))

#Python 3.6 also introduces f-strings:
print(f'{myString}, is a string that I wrote!')


#String methods
#.upper() and .lower() for all upper/lowercase
print(myString.upper()) ; print(myString.lower())
#.isupper() and .islower() can check if the string is all upper/lowercase.
print(myString.isupper())

#There are other true/false methods:
#.isalpha() : True if string only letters.
#.isalnum() : True if string only letters and numbers.
#.isdecimal() : True if only numbers.
#.isspace() : True if only space, tab, newline.
#.istitle() : True if Uppercase followed by lowercase word. (Title)

#Can check if string starts/ends with a sub-string.
print(myString.startswith('Hell'))
print(myString.endswith('x'))

#The .join() method can be used to combine a list of strings
myList = ['cats', 'dogs', 'and rats']
print(', '.join(myList)) #What .join is called with is inserted between each string.

#The .split() method does the opposite. Take string, outputs list. Splits at whitespace.
print('My name is Matthew.'.split())
#Can also split at newline via .split('\n')

#You can split strings at specific characters using the .partition() method
print('My name is Matthew.'.partition('i'))

#Remove whitespace in a string with .strip(), .rstrip(), .lstrip() methods
#  or strip specific characters .strip('ams') removes a, m, and s characters.


#You can also copy-paste text using the pyperclip module.
import pyperclip
pyperclip.copy('Hello')
print(pyperclip.paste())
