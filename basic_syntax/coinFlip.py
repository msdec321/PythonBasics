#This is the coin flip streak script!

#Flip a coin 100 times and fill a lists of "H" for heads and "T" for tails.
#   Then, check if there is a streak of 6 heads or 6 tails in a row.
#   Loop this process 10,000 times and find out what the percentage of this occuring is.

import random

N, M = 100, 10000
total_streaks=0

for k in range(M):

    flips = []
    streak_flag=0

    for i in range(N):

        flip = random.randint(0,1)

        if flip==0: flips.append('H')
        else: flips.append('T')


    streak_count=0
    for i,j in enumerate(flips):
        try:
            if flips[i]=='H' and flips[i+1]=='H': streak_count+=1
            elif flips[i]=='T' and flips[i+1]=='T': streak_count+=1
            else: streak_count=0

            if streak_count>=6:
                #print('Theres a streak of six in a row!')
                streak_flag=1

        except IndexError: continue

    if streak_flag==1: total_streaks+=1
    if k%1000==0: print('Rounds processed: ', k)


print('The percentage of streaks per round is: ', float(total_streaks)/float(M))

