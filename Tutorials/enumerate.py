#Instead of for i in range(len(<list>)):, use the built-in enumerate function:

values = [1,2,3,4,5,6,7]

for i,j in enumerate(values):
    print(i, j)   #i is the index, j is the value at that index.


#The index of an arbitrary value can be called using:
print('The index of 4 is: ', values.index(4))


#Not only can you append, but you can also insert values at a specified index:
values.insert(3, 8) #Insert at index 3 the value of 8.
print(values)

#Can also remove specific values.
values.remove(5)  #If repeated in list, only first will be deleted.
print(values)

#To remove a specific index, use the del command instead.
del values[5]
print(values)
