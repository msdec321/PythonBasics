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

    if upper_flag and lower_flag and digit_flag:
        print(f'{password} is a strong password!')

    if not upper_flag: print(f'{password} is missing an uppercase letter.')
    if not lower_flag: print(f'{password} is missing a lowercase letter.')
    if not digit_flag: print(f'{password} is missing a digit.')


except AttributeError:
    print('Error: Password must be at least 8 characters.')
