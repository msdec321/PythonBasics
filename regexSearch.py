#! python3

#This is the regex search script.
#This script opens all ".txt" files in a given directory and searches for a specified
#  line of text using regex. The results are printed to the terminal.

import re, sys, os
from pathlib import Path

def search(myString):

    for filename in os.listdir('./'):
        if '.txt' in filename:
            stringRegex = re.compile(myString)

            fileObj = open(filename)
            mo = stringRegex.search(fileObj.read())

            if mo:
                print(f'"{myString}" found in: {filename}.')

            fileObj.close()



if len(sys.argv)<2:
    print('Error: Enter a string to search.')

elif len(sys.argv)>2:
    print('Error: Too many arguments. Please type the string in quotes.')

else:
    search(sys.argv[1])
