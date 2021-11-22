#!/usr/bin/python3

#This is the excel to csv script. This script converts all excel files in a specified directory
#  to CSV files (one file per sheet), with convention <excel_filename>_<sheet_name>.csv

import openpyxl, csv, os
from pathlib import Path

p = Path('./excelToCsv/')

for filename in os.listdir(p):

    if not filename.endswith('xlsx'): continue
    wb = openpyxl.load_workbook(p/filename)

    for sheet in wb.sheetnames:

        csvFile = open(p/Path(filename[:-5]+"_"+str(sheet)+".csv"), "w")
        csvWriter = csv.writer(csvFile)
        sh = wb[sheet]

        for row in sh.rows:

            lst=[]
            for cell in row:
                if cell.value != None: lst.append(cell.value)

            csvWriter.writerow(lst)
        csvFile.close()
    wb.save(p/filename)
