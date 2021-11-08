#!/usr/bin/python3

#This is the CSV Header row remover script.
#This script takes all csv files in a specified directory and removed the first row.
  #(Note: copy the full contents of the CSV file, skipping the first line, and past it to a new file of the same name.)

import csv, os
from pathlib import Path

p = Path('./removeCsvHeader/')

for filename in os.listdir('./removeCsvHeader/'):
    if not filename.endswith('csv'):
        continue

    readFile = open(p/filename)
    csvReader = csv.reader(readFile)
    List = list(csvReader)
    readFile.close()

    writeFile = open(p/filename, 'w')
    csvWriter = csv.writer(writeFile)

    for index, row in enumerate(List):
        if index==0:
            continue
        else:
            csvWriter.writerow(row)

    writeFile.close()
