#!/usr/bin/python3

'''
3_bitmapMessage.py - This program uses a multiline string as a bitmap, a 2D image with only two
possible colors for each pixel, to determine how it should display a message from the user. In
this bitmap, space characters represent an empty space, and all other characters are replaced
by characters in the user’s message. The provided bitmap resembles a world map, but you can
change this to any image you’d like. The binary simplicity of the space-or-message-characters
system makes it good for beginners.
'''

import pyinputplus as pyip


bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""


bitmap_as_list = bitmap.split('\n')  #Store the bitmap as a list object.
myString = pyip.inputStr('Input a string for the bitmap: ')
new_map = []

for i, line in enumerate(bitmap_as_list):
    new_line = ""  #Initialize a blank String object.

    k = 0
    for j, char in enumerate(line):  #Fill the string object with either whitespace or the input string characters.
        if char == ' ': new_line += (' ')
        elif char == '*' or char == '.': new_line += (myString[k])

        k += 1
        if k % len(myString) == 0: k = 0

    new_map.append(new_line)

for string in new_map:
    print(string)  #Print the new bitmap line-by-line.
