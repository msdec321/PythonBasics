#! python3

#This script will detect if a password is strong or not.
#A strong password has at least 8 characters, both upper and lowercase and at least 1 digit.

import re

passRegex = re.compile(r'[a-zA-Z0-9]{8}')

password = "heLh3112"

upper_flag=0 ; lower_flag=0 ; digit_flag=0

try:
    mo = passRegex.search(password)
    mo.group()

    for i in range(len(password)):
        if password[i].isupper(): upper_flag=1
        if password[i].islower(): lower_flag=1
        if password[i].isdecimal(): digit_flag=1

    if upper_flag==1 and lower_flag==1 and digit_flag==1:
        print(f'{password} is a strong password!')

    if upper_flag==0: print(f'{password} is missing an uppercase letter.')
    if lower_flag==0: print(f'{password} is missing a lowercase letter.')
    if digit_flag==0: print(f'{password} is missing a digit.')


except AttributeError:
    print('Error: Password must be at least 8 characters.')
