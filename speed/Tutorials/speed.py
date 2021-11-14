#!/usr/bin/python3

'''
speed.py - This is the speed performance tutorial. Often programmers care about how fast 
their programs run and how to optimize runtime speed. The modules "timeit" and "cProfile"
measure how fast code runs and where optimizations can be made, respectively.
A commond question to ask is: as the data increases, how does the rate of runtime of my code
scale? Linear, quadratic, logarithmic, ...? This is "Big-O" notation.
A good rule of thumb is to first make your code work, then make it fast.
'''

#Print the time it takes to run a simple operation, like generating a random number.
import timeit
print(timeit.timeit('random.randint(0,100)', 'import random', number=10000))


#timeit is good for small snippets, but cProfile is better for while programs.
import cProfile
#TODO: Add a cProfile example here.


'''
Big-O Orders (from shortest to longest):
O(1) - Constant time, such as boolean checks
O(log n) - logarithmic time, such as a binary search algorithm
O(n) - Linear time, such as a regular search algorithm
O(n log n) - N-Log-N time, such as sorting alphabetically
O(n**2) - Polynomial time, such as looping through an array of N items N times
O(2**n) - Exponential time, such as every combination (but not permutating) of N items
O(n!) - Factorial time, such as permutating N items

It's often useful to think about how long a procedure will take in the -worst case scenario-


Common functions: (s=sequence, m=map/dict)
s[i] reading and s[i] value assignment - O(1)
m[key] reading and m[key] = value assignment - O(1)
len(s) - O(1)
len(m) - O(1)
s.append(i) - O(1)
m.add(value) - O(1)
value in m - O(1)

s.insert(i, value) - O(n)
s.remove(value) - O(n)   - Inserting/removing requires shifting values in the sequence.
s.reverse() - O(n)
value in s - O(n)
for value in s: - O(n)
for key in m: - O(n)

s.sort - O(n log n)
'''
