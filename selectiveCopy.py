#! python3

#This is the selective copy script. This script copies the contents of a folder with
#  a specified extension (.txt, .py, .pdf, etc) and copies them to another location.

import shutil, re, os, sys
import pyinputplus as pyip
from pathlib import Path

def copy(ext, folder_in, folder_out):

    p = Path(folder_in)

    for filename in os.listdir('./'+folder_in):
        if ext in filename:
            shutil.copy(p / filename, folder_out)


ext = pyip.inputStr('Input a file extension (.py, .txt, .pdf, etc): ')
folder_in = pyip.inputFilepath('Input an input filepath (it must exist): ')
folder_out = pyip.inputFilepath('Input an output filepath (it must exist): ')

copy(ext, folder_in, folder_out)
