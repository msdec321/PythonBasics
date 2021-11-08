#! python3

#This is a phone number and email extractor.
#This script copies text from the clipboard, searches it for phone numbers and emails and pastes them to the clipboard.

import pyperclip, re


phoneRegex = re.compile(r'''(
        ( \d{3} | \(\d{3}\) )?  #Area code, parenthesis or not
        ( \s | - | \. )?        #Seperator (ws, - , or .)
        ( \d{3} )               #Next three digits
        ( \s | - | \. )?        #Seperator
        ( \d{4} )               #Last four digits
        ( \s*(ext|x|ext.)\s*(\d{2,5}) )?  #Extension
        )''', re.VERBOSE)

emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+  #Username
        @
        [a-zA-Z0-9.-]+  #Domain name
        (\.[a-zA-Z]{2,4})  #.something
         )''', re.VERBOSE)


text = pyperclip.paste()

matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])


if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard.')
    print('\n'.join(matches))
