#!/usr/bin/python3

#This is the CSV (comma seperated values) file format tutorial.
#.csv and .json files are standard plaintext formats for storing data. In Python, these can be handled using the "csv" and "json" modules.

#For CSV files, each line is represented as a row in a spreadsheet, and data between commas (,)
#  are represented by columns. Note that CSV entries don't have data types. Everything is a String.

#Note that commas (,) may actually be part of the string and not seperating cells. Because of this pitfall you will want to process csv files using the csv module, not the .split() method.


#Reader objects are used to read data from csv files
import csv
exampleFile = open("example.csv")
exampleReader = csv.reader(exampleFile)
myList = list(exampleReader)
print(myList)        # Data is printed as a list of lists.
print(myList[0][0])  # [row][col]

#Printing the entirety of a list can use a lot of memory, instead you can use a for loop.
for index, row in enumerate(myList):
    print(f"Row {index+1}: {row}")
    #Alternatively:
    #print(f"Row {exampleReader.line_num}: {row}")  #Doesn't get the line number correct..

exampleFile.close()


#Writer objects are used to write data to csv files
outputFile = open("output.csv", "w")
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])  #writerow only takes list arguments
outputWriter.writerow([1, 23, 456, 7.89])
outputWriter.writerow(["Hello, world!", 23, 456, 7.89])  #Note double-quotes ignores the comma
outputFile.close()


#Seperating values with a character other than (,), use a delimiter
outputFile = open("output.csv", "w")
outputWriter = csv.writer(outputFile, delimiter=" ")
outputFile.close()

#To double-space, use a lineterminator
outputFile = open("output.csv", "w")
outputWriter = csv.writer(outputFile, lineterminator="\n\n")
outputFile.close()


#If your file contains Header rows, use dictReader and dictWriter objects
#The first row of your file becomes Keys of a dictionary, rather than a list object.
#You can also manually set the Key names if it's headerless aswell.
exampleFile = open("exampleWithHeader.csv")
exampleDictReader = csv.DictReader(exampleFile)
for row in exampleDictReader:   # "row" is a Dictionary, print the value of the specified Keys
    print(f"{row['Timestamp']}, {row['Fruit']}, {row['Quantity']}")
exampleFile.close()

#DictWriter
outputFile = open("exampleDictWriter.csv", "w")
exampleDictWriter = csv.DictWriter(outputFile, ["name", "date", "food"])
exampleDictWriter.writeheader()
exampleDictWriter.writerow({"name":"Matthew", "date": "11-07-2021", "food":"chicken"})
outputFile.close()
