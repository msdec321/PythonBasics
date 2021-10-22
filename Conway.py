#This Conway's game of life!

import time
import random
import numpy as np

N = 10

grid = np.zeros((N,N))

for i in range(N):
    for j in range(N):
        rand = random.randint(1,4)
        if rand==1: grid[i][j] = 1


print('Initial grid:')
print(grid)
print('-------------Next grid----------------')
time.sleep(3)


while True:

    for i in range(len(grid)):
        for j in range(len(grid)):
            try:
                if (grid[i+1][j] and grid[i-1][j])==1:   grid[i][j]=1
                elif (grid[i+1][j] and grid[i][j+1])==1: grid[i][j]=1
                elif (grid[i-1][j] and grid[i][j-1])==1: grid[i][j]=1
                elif (grid[i+1][j] and grid[i][j-1])==1: grid[i][j]=1
                elif (grid[i-1][j] and grid[i][j+1])==1: grid[i][j]=1
                elif (grid[i][j-1] and grid[i][j+1])==1: grid[i][j]=1
                else: grid[i][j]=0

            except IndexError: continue

    for i,j in enumerate(grid):
        print(grid[i])

    print('-------------Next grid----------------')
    time.sleep(3)
