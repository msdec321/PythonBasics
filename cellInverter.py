#! python3

#This is the spreadsheet inversion script. This takes a spreadsheet with rows-cols NxM
#  and inverts the spreadsheet to MxN.

import openpyxl

wb = openpyxl.load_workbook('myWorkbook.xlsx')
wb.create_sheet('inverted_sheet')
sheet1 = wb['Sheet1']
sheet2 = wb['inverted_sheet']

for i in range(1, len(list(sheet1.columns))+1):
    for j in range(1, len(list(sheet1.rows))+1):
        sheet2[chr(j+64)+str(i)].value = sheet1[chr(i+64)+str(j)].value

wb.save('myWorkbook.xlsx')
