#This is the character picture grid game!

import numpy as np

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'o', 'o', '.', '.', '.'],
        ['o', 'o', 'o', 'o', '.', '.'],
        ['o', 'o', 'o', 'o', 'o', '.'],
        ['.', 'o', 'o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'o', 'o', '.'],
        ['o', 'o', 'o', 'o', '.', '.'],
        ['.', 'o', 'o', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

new_grid=[]

#Create a new grid with the opposite size.
for i in range(len(grid[0])):
    new_grid.append([])
    for j in range(len(grid)):
        new_grid[i].append('')

#Rotate the original grid by 90 degrees by assigning the i-th index of the
#  original grid to the j-th index of the new one, and vice-versa.
for i in range(len(new_grid)):
    for j in range(len(new_grid[0])):
        new_grid[i][j] = grid[j][i]


#Print the rotated grid!
for i in range(len(new_grid)):
    print(new_grid[i])
