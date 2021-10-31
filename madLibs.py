#! python3

#This is the mad libs script. This allows the user to insert into a text file
#  an adjective, noun, adverb, or verb into a predefined text.

import re
import pyinputplus as pyip
from pprint import pprint

def textSub(myString):

    while True:

        if 'ADJECTIVE' in myString:
            textRegex = re.compile(r'ADJECTIVE')
            adj = pyip.inputStr("Enter an adjective: ")
            myString = textRegex.sub(adj, myString,1)

        elif 'NOUN' in myString:
            textRegex = re.compile(r'NOUN')
            noun = pyip.inputStr("Enter an noun: ")
            myString = textRegex.sub(noun, myString,1)

        elif 'VERB' in myString:
            textRegex = re.compile(r'VERB')
            verb = pyip.inputStr("Enter an verb: ")
            myString = textRegex.sub(verb, myString,1)

        elif 'ADVERB' in myString:
            textRegex = re.compile(r'ADVERB')
            adverb = pyip.inputStr("Enter an adverb: ")
            myString = textRegex.sub(adverb, myString,1)

        else: break


    return myString

fileObj = open('panda.txt')
newString = textSub(fileObj.read())
fileObj.close()

fileObj = open('panda.txt', 'w')
fileObj.write(newString)
fileObj.close()
print(newString)
