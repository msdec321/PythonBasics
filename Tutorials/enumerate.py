#Instead of for i in range(len(<list>)):, use the built-in enumerate function:

values = [1,2,3]

for i,j in enumerate(values):
    print(i), print(j)   #i is the index, j is the value at that index.
