#! python3

#This is a tutorial on reading and writing to files.

#If you want your data to persist after running your program, you must write it to a file.
#Files have a filename and a path.

#Path syntax is different for Windows (\) vs Linux (/). To make the same, use pathlib module:
#(pathlib was introduced in Python3.6 to replace the old os.path functions)

from pathlib import Path

#If Path is passed strings, it will use the correct seperators.
Path('usr', 'git', 'SmallProjects', 'Tutorials')


#How to display multiple files
myFiles = ['Dictionaries.py', 'richText.py', 'Strings.py']
for filename in myFiles:
    print(Path(r'/usr/git/SmallProjects', filename))


#Current working directory
print(Path.cwd())

#Home directory
print(Path.home())

#Shorthand: (.) - means current directory. (..) - means parent directory.


#Creating new directories
import os
#os.makedirs('./newFolder')

#To get the absolute path from a relative path:
print(Path.cwd() / Path('./'))


#Filesize (in kb)
print(os.path.getsize('Dictionaries.py')/1000.)

#ls
print(os.listdir('./'))


#Boolean path methods:
#   p.exists() - True if path exists
#   p.is_file() - True if a file
#   p.is_dir()  - True if a directory


#Reading a file with Path
from pathlib import Path
p = Path('Tuples.py')
#Set path to a variable, then read its contents (as a String object)
print(p.read_text())

#Write (or overwrite) a plaintext file. (Works for .txt and .py)
p = Path('text.txt')
p.write_text('Hello world! \nThis is a text file!')
print(p.read_text())


#Open, read/write, and close
#As of Py3.6, open only accepts Path objects. Fils are open in read mode by default.
myFile = open(Path('text.txt'))
#Reading
print(myFile.read())
myFile.close()

#To write, you must open a file in write ('w') mode.
myFile = open('text.txt', 'w')
myFile.write('\nThis is a new line.')
myFile.close()


#Variables can be saved to binary shelf files using the "shelve" module.
import shelve
#As of Py3.7, shelve takes a string file name, not a Path object.
shelfFile = shelve.open('mydata')
cats = ['Ace', 'Benny', 'Cindy']
A = 25.0
#Note that objects and variables gets saved as dictionary key-value pairs.
shelfFile['cats'] = cats
shelfFile['A'] = A
shelfFile.close()

#To later retreive/reopen the data
shelfFile = shelve.open('mydata')
print(shelfFile['cats'])
print(shelfFile['A'])
shelfFile.close()


#Saving variables with pprint to a python file rather than a db file
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Scratchy', 'desc': 'fuzzy'}]
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

#To later retrieve/reopen:
import myCats
print(myCats.cats)
print(myCats.cats[0])


#Plaintext files are easier to work with, but cannot save complex objects like Path.
#  For most applications the shelve module is better to use.
