#! python3

#This is the multiplication table script. It takes a number N from the command line
#  and produces an NxN excel sheet multiplication table. 
#  Row 1 and Column 1 are labels and should be bolded.
#  Note: Only works up to N=24

import openpyxl, sys
from openpyxl.styles import Font
import pyinputplus as pyip



if len(sys.argv)!=2 or not sys.argv[1].isdecimal():
    print('Error: Please input an integer argument.')
    sys.exit()

elif int(sys.argv[1])>24:
    print('Error: Integer argument must be less than 25.')
    sys.exit()

N = sys.argv[1]

#Create the workbook and sheet
wb = openpyxl.Workbook()
sheet = wb['Sheet']

#Set the first row/column
boldFont = Font(bold=True)
for i in range(int(N)):
    sheet['A'+str(i+2)]=i+1
    sheet['A'+str(i+2)].font = boldFont
    sheet[chr(i+66)+'1']=i+1
    sheet[chr(i+66)+'1'].font = boldFont

#Fill the table
for i in range(int(N)):
    for j in range(int(N)):
        sheet[chr(j+66)+str(i+2)].value = sheet[chr(j+66)+str(1)].value * sheet[chr(65)+str(i+2)].value

#Save the workbook
wb.save('multiTable.xlsx')
