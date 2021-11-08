#! python3

#This script will strip a string of specified character using regex.
#If no characters are specified, it will strip whitespace from the beginning and end of the string.

import re

def strip(char, context):
    if char=='':
        regex_sub = re.compile(r'^\s+|\s+$')
        stripContext = regex_sub.sub("", context)
        return stripContext

    else:
        regex_sub = re.compile(char)
        stripContext = regex_sub.sub("",context)
        return stripContext


print('Character to remove: ')
var = input()
myString = '   This is a sentence.'
print(myString)
print(strip(var, myString))


