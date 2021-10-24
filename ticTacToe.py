#This is a tic tac toe game using dictionaries

import random

board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
         'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
         'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '}

#Print initial board.
print(' ' + board['top-L'] + ' | ' + board['top-M'] + ' | ' + board['top-R'] )
print(' ' + board['mid-L'] + ' | ' + board['mid-M'] + ' | ' + board['mid-R'] )
print(' ' + board['bot-L'] + ' | ' + board['bot-M'] + ' | ' + board['bot-R'] )

#Choose starting player at random.
flag=random.randint(0,1)
while True:

    if flag:
        print('Player X choose (top-L, top-M, ..., bot_R): ')
        choice = input()
        if board[choice] == ' ':
            board[choice] = 'X'
            flag=0
        else: print('Error: That position has already been used. Please choose again.')

    else:
        print('Player O choose (top-L, top-M, ..., bot_R): ')
        choice = input()
        if board[choice] == ' ':
            board[choice] = 'O'
            flag=1
        else: print('Error: That position has already been used. Please choose again.')

    #Display current board.
    print(' ' + board['top-L'] + ' | ' + board['top-M'] + ' | ' + board['top-R'] )
    print(' ' + board['mid-L'] + ' | ' + board['mid-M'] + ' | ' + board['mid-R'] )
    print(' ' + board['bot-L'] + ' | ' + board['bot-M'] + ' | ' + board['bot-R'] )

    #Check for board for a win or draw.
    if ((board['top-L']==board['top-M']==board['top-R']=='X') or
        (board['top-L']==board['top-M']==board['top-R']=='X') or
        (board['bot-L']==board['bot-M']==board['bot-R']=='X') or
        (board['top-L']==board['mid-L']==board['bot-L']=='X') or
        (board['top-R']==board['mid-R']==board['bot-R']=='X') or
        (board['top-R']==board['mid-M']==board['bot-L']=='X') or
        (board['mid-L']==board['mid-M']==board['mid-R']=='X') or
        (board['top-M']==board['mid-M']==board['bot-M']=='X')):
            print('Player X wins!')
            break

    if ((board['top-L']==board['top-M']==board['top-R']=='O') or
        (board['top-L']==board['top-M']==board['top-R']=='O') or
        (board['bot-L']==board['bot-M']==board['bot-R']=='O') or
        (board['top-L']==board['mid-L']==board['bot-L']=='O') or
        (board['top-R']==board['mid-R']==board['bot-R']=='O') or
        (board['top-R']==board['mid-M']==board['bot-L']=='O') or
        (board['mid-L']==board['mid-M']==board['mid-R']=='O') or
        (board['top-M']==board['mid-M']==board['bot-M']=='O')):
            print('Player O wins!')
            break

    if ((board['top-L']!=' ' and board['top-M']!=' ' and board['top-R']!=' ' and
         board['mid-L']!=' ' and board['mid-M']!=' ' and board['mid-R']!=' ' and
         board['bot-L']!=' ' and board['bot-M']!=' ' and board['bot-R']!=' ')):
            print('The game is a draw!')
            break
