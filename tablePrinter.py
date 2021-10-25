#! python3

#This is the table printer script. It takes a list of strings and outputs a nice table.

def printTable(myList):

    for i in range(len(myList)):
        for j in range(len(myList[i])):

            #Determine longest word in the list, adjust whitespace of each smaller word.
            longest = len(max(myList[i], key=len))
            for k in range(longest - len(myList[i][j])):
                myList[i][j] = " " + myList[i][j]

    #Flip rows/columns for new data structure using new lists.
    for j in range(len(myList[0])):

        newList = []
        for i in range(len(myList)):
            newList.append(myList[i][j])

        #Print the new lists
        print('  '.join(newList))



#Original list
List = [['apples', 'bananas', 'cherries', 'donuts'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['one', 'two', 'three', 'four']]



printTable(List)
