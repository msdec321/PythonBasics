#This script will initialize an arbitrary number of variables via user input.

varNames = []

while True:
	print('Enter the name of variable ' + str(len(varNames) + 1) + ' (Or enter nothing to stop.): ')
	
	name = input()
	if name == '': break
	
	varNames = varNames + [name]
	
print('The variable names are:')

for name in varNames:
	print(' ' + name)


#Multiple assignment trick or 'tuple unpacking'
cat = ['fat', 'grey', 'loud']
size, color, disposition = cat
