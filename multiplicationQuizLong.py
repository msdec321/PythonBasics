#! python3

#This is a longer version of the multiplication quiz that does not use pyinputplus.
#Ask 10 questions from 0x0 to 9x9. 
#Display correct for 1 second.
#Three attempts
#Eight second time limit.

import random, time

print('Welcome to the multiplication quiz!')
print('There are ten questions. You have eight seconds to answer each question.')

nQuestions, nCorrectAnswers = 0, 0

for i in range(10):
    a, b = random.randint(0,9), random.randint(0,9)
    print(f'Question: What is {a} times {b}?')

    tries=0
    while True:
        start=time.time()
        answer = input()
        end=time.time()
        if end-start>=8.0:
            print('Sorry, you took too long to answer!')
            break

        if int(answer) == a*b:
            print('Correct!')
            nCorrectAnswers+=1
            time.sleep(1)
            break

        else:
            print('That is incorrect! Try again.')
            tries+=1

        if tries==3:
            print('Next question.')
            break

    nQuestions+=1

print(f'You scored {nCorrectAnswers} out of {nQuestions}!')



