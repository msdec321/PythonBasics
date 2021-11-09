#!/usr/bin/python3

'''
2_birthdayParadox.py - The Birthday Paradox, also called the Birthday Problem, is the surprisingly
high probability that two people will have the same birthday even in a small group of people.
In a group of 70 people, there’s a 99.9 percent chance of two people having a matching birthday.
But even in a group as small as 23 people, there’s a 50 percent chance of a matching birthday.
This program performs several probability experiments to determine the percentages for groups of
different sizes. We call these types of experiments, in which we conduct multiple random trials to
understand the likely outcomes, Monte Carlo experiments.

#Input a number of birthdays N, and do this M times. Check how often there is a pair of matching
birthdays, and calculate the probability that there is a matching birthday given N birthdays.
'''

import random
import pyinputplus as pyip

months = {"Jan":31, "Feb":29, "Mar":31, "Apr":30, "May":31, "Jun":30, "Jul":31, "Aug":31, "Sep":30, "Oct":31, "Nov":30, "Dec":31}


def main():

    match_count=0
    total_count=0

    N = pyip.inputNum("Enter a number of birthdays: ", min=1)
    M = pyip.inputNum("Enter a number of simulations (min=100): ", min=100)

    for i in range(M):

        bdays = []

        for i in range(N):
            bdays.append(birthdayPicker(months))

        if findMatch(bdays):
            match_count+=1

        total_count+=1

    print(f'The frequency of a matching birthdays in {M} simulations given {N} people is {match_count} times.')
    print(f'The probability of a matching birthday occuring given {N} people is {float(match_count)/float(total_count)}.')



def birthdayPicker(months):
    month = random.choice(list(months.keys()))
    day = random.randint(1, months[month])
    return str(month+" "+str(day))


def findMatch(bdays):
    bdays.sort()
    for index, item in enumerate(bdays):
        try:
            if bdays[index]==bdays[index+1]:
                return True
        except IndexError:
            continue

    return False


if __name__ == '__main__':
	main()

