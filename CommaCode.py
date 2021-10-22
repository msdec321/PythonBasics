#This is the Comma Code script!

import sys

def convert(List):

    try:
        for i in range(len(List)-1):
            List[i] = List[i]+', '

        List[-1] = "and " + List[-1]
        return List

    except IndexError:
        print('Empty list. Please provide a list!')
        sys.exit()

myList = ['apples', 'bananas', 'tofu', 'cats']
myList = convert(myList)

string = ''
for index, item in enumerate(myList):
        string += item

print(string)
