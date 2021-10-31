#! python3

#This script changes the dates of filenames in a specified directory from American-
#  style dates (MM-DD-YYYY) to European style (DD-MM-YYYY).

import re, shutil, os
from pathlib import Path

def dateFlip(filename):

    dateRegex = re.compile(r'(\d\d)-(\d\d)-(\d\d\d\d)')
    mo = dateRegex.search(str(filename))
    mm = mo.group(1)
    dd = mo.group(2)
    yy = mo.group(3)

    shutil.move(filename, p/f'{dd}-{mm}-{yy}.txt')

p = Path('./dates/')

for filename in os.listdir(p):
    dateFlip(p/filename)
