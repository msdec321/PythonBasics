#! python3

#This is the gap filler script. This script searches a directory for similarly named
#files (text_1.txt, text_2.txt...) and checks if there is a gap in the numbering (1,3,4...),
#and renames files appropriately to fill the gap.

import re, os, shutil
from pathlib import Path

def myFunction(myPath):

    fileRegex = re.compile(r'(.*[^\.])(\.)(.*[^\.])')
    myList = os.listdir(p)
    myList.sort()

    for filename in myList:
        mo = fileRegex.search(filename)
        temp = mo.group(1)[:-2]

        i=1
        for filenames in myList:

            mo = fileRegex.search(filenames)

            if temp == mo.group(1)[:-2]:
                if (mo.group(1)[:-1]+str(i)+mo.group(2)+mo.group(3) in myList):
                    i+=1
                    continue

                elif filenames==mo.group(1)[-1:]+str(i)+mo.group(2)+mo.group(3):
                    break

                else:
                    shutil.move(p/filenames, './temp/'+mo.group(1)[:-1]+str(i)+mo.group(2)+mo.group(3))
                    myList[i-1] = mo.group(1)[:-1]+str(i)+mo.group(2)+mo.group(3)
                    break

p = Path('./temp')
myFunction(p)
