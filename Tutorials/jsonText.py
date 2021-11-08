#!/usr/bin/python3

#This is the  JSON (JavaScript Object Notation) file format tutorial. JavaScript knowledge is not needed to work with JSON files.
#.csv and .json files are standard plaintext formats for storing data. In Python, these can be handled using the "csv" and "json" modules.

import json

#Reading with .loads()   Can store: string, int, float, bool, list, dict, None
jsonString = '{"name":"Sophie", "isCat":true, "miceCaught":0, "felineIQ":0}'
jsonAsPython = json.loads(jsonString)
print(jsonAsPython)

#Writing with .dumps()
pyDict = {"name":"Sophie", "isCat":True, "miceCaught":0, "felineIQ":0}
jsonString = json.dumps(pyDict)
print(jsonString)
