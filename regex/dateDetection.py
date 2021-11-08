#! python3

#This is the date detector script.
#This reads a date MM/DD/YYYY and determines if it is valid.
#Valid days range from 0-31. Months from 0-12. Years from 1000-2999
#April, June, September, November have 30 days. January, March, May, July, August, October, December have 31 days. February has 28 days and 29 in leap years (divisible by 4 and 100 except 400).

import re

dateRegex = re.compile(r'''
    ([0][0-9] | [1][0-2])               #Month
    (/)                                 #Seperator
    ([0][1-9] | [1-2][0-9] | [3][0-1])  #Day
    (/)                                 #Seperator
    ([1-2][0-9][0-9][0-9])              #Year
    ''', re.VERBOSE)


date = 'The date is 02/29/1700'

mo = dateRegex.search(date)

thirtyDays = ['04', '06', '09', '11']
thirtyOneDays = ['01', '03', '05', '07', '08', '10', '12']
Feb = ['02']

try:
    if mo.group(1) in thirtyDays:
        if int(mo.group(3))<=30:
            print(f'{mo.group()} is a valid date!')

    if mo.group(1) in thirtyOneDays:
        if int(mo.group(3))<=31:
            print(f'{mo.group()} is a valid date!')

    if mo.group(1) in Feb:
        if int(mo.group(3))<=28:
            print(f'{mo.group()} is a valid date!')

        elif int(mo.group(3))==29 and int(mo.group(5))%4==0:
            if int(mo.group(5))%400==0:
                print(f'{mo.group()} is a valid date!')

            if int(mo.group(5))%100==0 and int(mo.group(5))%400!=0:
                print(f'Not a valid date!')


except:
    print('Not a valid date!')
