#! python3

#This script reads data from an excel workbook.
#This script will: count number of tracts per county, count total pop per county.
#Store these results in a data structure and output to a .py file via pprint.

import openpyxl, pprint
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']

census_data=[]
tracts=0 ; pop=0
county_temp=''

for cell1, cell2, cell3 in zip(list(sheet.columns)[1], list(sheet.columns)[2], list(sheet.columns)[3]):

    if cell2.value==county_temp:
        tracts+=1
        pop+=cell3.value

    else:
        print(f'Number of tracts in county {cell2.value}, {cell1.value}: {tracts}')
        print(f'Population of county {cell2.value}: {pop}')
        print('----Next county----')

        census_data.append({"County": cell2.value+", "+cell1.value, "Tracts":tracts, "Population":pop})

        tracts=1
        pop=cell3.value
        county_temp=cell2.value

fileObj = open('census_data.py', 'w')
fileObj.write('data' + pprint.pformat(census_data) + '\n')
fileObj.close()
