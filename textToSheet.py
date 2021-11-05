#! python3

#This is the "text to sheet" script. This script takes the contents of SEVERAL text files
#  and exports them to a spreadsheet, one line of text per row.
#  The first column corresponds to the first text file, the second file to the second column, etc.

import openpyxl, os
from pathlib import Path

wb = openpyxl.Workbook()
sheet = wb['Sheet']
p = Path('./textToSheet/')

#For some reason os.listdir does not sort automatically, so do it:
lst = os.listdir(p)
lst.sort()

for index1, filename in enumerate(lst):
    myFile = open(p/filename)

    for index2, line in enumerate(myFile.readlines()):
        line = line[:-1] #Remove the newline character at the end of each string
        sheet[chr(index1+65)+str(index2+1)] = line

    myFile.close()

wb.save("textToSheet.xlsx")
