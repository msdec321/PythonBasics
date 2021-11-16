#!/usr/bin/python3

'''
towerofHanoi.py - The Tower of Hanoi is a simple puzzle game. Five disks of increasing
radius are stacked on one of three poles. The player must move pieces of the tower to
another pole one at a time, however the player cannot place a large disk on top of
a smaller disk.

     ||           ||           ||
    @_1@          ||           ||
   @@_2@@         ||           ||
  @@@_3@@@        ||           ||
 @@@@_4@@@@       ||           ||
@@@@@_5@@@@@      ||           ||

     A            B            C
'''

import sys
import pyinputplus as pyip

N_DISKS = pyip.inputNum("Enter number of disks (min = 5): ", min = 5)

TOWER = ''
DISKS, DISK_OPTIONS, TOWER_OPTIONS = [], [], []

#-----------------------------------

# Set the disk and tower ASCII art based on N_DISKS

for i in range(N_DISKS):
    DISKS.append('')
    TOWER += ' '

TOWER += '||'

for i in range(N_DISKS):
    TOWER += ' '
    for j in range(i):
        DISKS[j] += ' '

for i in range(N_DISKS + 1):
    for j in range(i, 0, -1):
        DISKS[-j] += '@'

for i in range(N_DISKS):
    DISKS[i] += '_' + str(i + 1)

for i in range(N_DISKS + 1):
    for j in range(i, 0, -1):
        DISKS[-j] += '@'

for i in range(N_DISKS):
    for j in range(i):
        DISKS[j] += ' '

#-----------------------------------

# Set the disk and tower options based on N_DISKS
for i in range(N_DISKS):
    DISK_OPTIONS.append(str(i + 1))

for i in range(N_DISKS - 2):
    TOWER_OPTIONS.append(chr(i + 65))


LINES=[]  # This 2D matrix will draw the ASCII art.

# Fill the matrix
for i in range(len(DISK_OPTIONS) + 2):
    LINES.append([])

    for j in range(len(TOWER_OPTIONS)):
        if i == 0: LINES[0].append(TOWER)

        if i != 0 and j == 0 and i!=len(DISK_OPTIONS) + 1:
            LINES[i].append(DISKS[i - 1])

        if i != 0 and j != 0 and i != len(DISK_OPTIONS) + 1:
            LINES[i].append(TOWER)


# Draw the ASCII art
for index, item in enumerate(LINES):
    print(" ".join(LINES[index]))

# This function finds where each disk is located via their index. Use this to check winning/losing configurations.
def index_finder(DISK):
    DISK_INDEX = ''

    for i in range(len(DISK_OPTIONS) + 1):
        for j in range(len(TOWER_OPTIONS)):
            if LINES[i][j] == DISK:
                DISK_INDEX += str(i)
                DISK_INDEX += str(j)

    return DISK_INDEX


# Main game loop
while True:

    # Choose which tower to move a disk to.
    while True:
        disk_choice = input("Choose a disc and tower number (ex. 1a, 2b, 3c..): ")

        if disk_choice[0] not in DISK_OPTIONS or disk_choice[1].upper() not in TOWER_OPTIONS or len(disk_choice) != 2:
            print("Error: Please choose a valid disk/tower combination: ")

        else: break

    # Convert tower choice to an integer index
    for i in range(len(TOWER_OPTIONS)):
        if   disk_choice[1].upper() == chr(65 + i): tower_choice = i

    i = 0
    flag_1 = 0  # Checks if the disk you chose was removed from its original tower.
    flag_2 = 0  # Checks if the disk you chose was placed on its new tower. Ends the next loop

    # Loop to move the disk.
    while True:

        for j in range(len(TOWER_OPTIONS)):

            # If ||, continue through loop.
            if j == tower_choice and i == len(DISK_OPTIONS) and flag_1 == 1:
                LINES[i][j] = temp
                flag_2 = 1
                break

            # If this is where the the player wants to move the disk to, replace || with the disk (temp).
            try:
                if j == tower_choice and LINES[i + 1][j] != TOWER and flag_1 == 1:
                    LINES[i][j] = temp
                    flag_2 = 1
                    break

            except IndexError:
                pass

            if LINES[i][j] == TOWER:
                continue

            # If this is the disk the player is moving, save it into a temp variable and replace the disk with ||.
            if disk_choice[0] in LINES[i][j] and flag_1 == 0:
                temp = LINES[i][j]
                flag_1 = 1
                LINES[i][j] = TOWER
                i = 0

        # When the disk is successfully moved, break out of the loop.
        if flag_2 == 1:
            break

        i += 1

    DISK_INDEX = []  # Holds disk locations to check for winning/losing configuration.

    for i in range(len(DISK_OPTIONS)):
        DISK_INDEX.append(index_finder(DISKS[i]))

    # Display the current configuration
    for index, item in enumerate(LINES):
        print(" ".join(LINES[index]))

    # Check for losing configurations (larger disk on top of small disk)
    larger = 1
    for i in range(0, len(DISK_OPTIONS) - 1):
        for j in range(larger, len(DISK_OPTIONS) - 1):

            if DISK_INDEX[i][1] == DISK_INDEX[j][1] and DISK_INDEX[i][0] > DISK_INDEX[j][0]:
                print('Invalid configuration. Smaller disk below larger disk. You lose!')
                sys.exit()

        larger += 1

    # Check for winning configuration (All disks on a new tower, in order from small disk to large disk)
    check = 0
    for i in range(len(DISK_OPTIONS) - 1):
        if DISK_INDEX[i][1] == DISK_INDEX[i + 1][1] != str(0):
            check += 1

    if check == len(DISK_OPTIONS) - 1:
        print('Winning configuration!! Thank you for playing!')
        sys.exit()


