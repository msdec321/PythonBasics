#! python3

#This is the blank row inserter script.
#This script takes 3 argumments: a starting row number, a number of blank rows, and a filename (.xlsx). This adds a number of blank rows N after a specified row number M to a spreadsheet.

import openpyxl, sys

if len(sys.argv)<3:
    print('Error: Expected 3 arguments: M - starting row number, N - number of blank rows, filename.')
    sys.exit()

elif not sys.argv[1].isdecimal() or not sys.argv[2].isdecimal():
    print('Error: Improper formatted arguments: M (int), N (int), string.')
    sys.exit()

M = int(sys.argv[1])    #Starting row (inserts below this row)
N = int(sys.argv[2])    #Number of blank rows to insert
wb = openpyxl.load_workbook(sys.argv[3])
sheet = wb['Sheet']

#Copy-paste rows from bottum-up to row number M.
for i in range(len(list(sheet.rows)), M, -1):
    for j in range(len(list(sheet.columns))):
        sheet[chr(j+65)+str(i+N)].value = sheet[chr(j+65)+str(i)].value

#Delete rows M to M+N
for i in range(M+1,M+N+1):
    for j in range(len(list(sheet.columns))):
        sheet[chr(j+65)+str(i)].value = ""

#Save updated workbook
wb.save(sys.argv[3])
