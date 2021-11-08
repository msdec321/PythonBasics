#! python3

#This is the multiplication quiz script

import pyinputplus as pyip
import random, time

nQuestions, nCorrectAnswers = 0, 0

print('This is the multplation quiz. You have five seconds for each problem.')

for i in range(10):
    a, b = random.randint(1,10), random.randint(1,10)
    print(f'Question: what is {a} times {b}? ')
    try:
        answer = pyip.inputNum(timeout=5)

        if answer == a*b:
            print(f'{answer} is correct!')
            nCorrectAnswers+=1
        else:
            print(f'{answer} is incorrect')

    except pyip.TimeoutException:
        print('Sorry, you ran out of time!')

    nQuestions+=1

print(f'The quiz is over. You scored {nCorrectAnswers} out of {nQuestions}!')
