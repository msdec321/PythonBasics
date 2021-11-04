#! python3

#This is a script that updates an excel sheet.
#This script finds specified produce (garlic, celery, lemon) and updates their prices.


import openpyxl
wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb['Sheet']

priceUpdates = {"Garlic":1.54, "Celery":2.98, "Lemon":1.10}

for cell1, cell2 in zip(list(sheet.columns)[0], list(sheet.columns)[1]):
    if cell1.value in priceUpdates: cell2.value = priceUpdates[cell1.value]

wb.save('produceSales.xlsx')
