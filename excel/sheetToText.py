#!/usr/bin/python3

#This is the "sheet to text" script. This script takes the contents of a spreadsheet
#  and exports them to a set of text files. Each column should correspond to one file,
#  and each row should correspond to an individual line in the file.

import openpyxl

wb = openpyxl.load_workbook('textToSheet.xlsx')
sheet = wb['Sheet']

for index2, column in enumerate(list(sheet.columns)):
    myFile = open('./textToSheet/text_'+str(index2+1)+'.txt', 'w')

    for index1, row in enumerate(list(sheet.rows)):
        myFile.write(sheet[chr(index2+65)+str(index1+1)].value+'\n')

    myFile.close()

wb.save('textToSheet.xlsx')
