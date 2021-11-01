#! python3

#This script walks through a folder tree and removes files above a certain size.
#The absolute path of these files are printed to the terminal.

from pathlib import Path
import os, send2trash

for folderName, subfolders, filenames in os.walk('./'):
    p = Path(folderName)

    for filename in filenames:
        if os.path.getsize(p/filename)>50000:
            print(f'Filename in {folderName}: {filename}')

            ##Uncomment following line to delete these files!
            #send2trash.send2trash(filename)

