#!/usr/bin/env python

'''
matplotlib.py - This is a tutorial for using matplotlib.
'''

import matplotlib.pyplot as plt


# How to make a simple scatter plot.

x = [1, 2, 3, 4, 5]
y = [5, 6, 7, 8, 9]

plt.xlabel('x-axis title')  # Labels must be defined before the .show() method
plt.ylabel('y-axis title')
plt.title('My plot title')
plt.scatter(x,y)  # x and y lists must be the same length.
plt.show()


'''
# How to plot two sets of data on the same canvas
x = [1, 2, 3, 4, 5]
y1 = [5, 6, 7, 8, 9]
y2 = [7, 2, 5, 3, 8]

plt.xlabel('x-axis title')
plt.ylabel('y-axis title')
plt.title('My plot title')
plt.scatter(x,y1,label='data 1')  # Must include .legend() method for the labels to show.
plt.scatter(x,y2,label='data 2')
plt.legend()
plt.show()
'''
