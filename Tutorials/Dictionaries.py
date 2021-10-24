#This is a tutorial on using the dictionary data type.

#An index to a List is as a key to a Dictionary. A key with an associated value is a key-value pair.
#A dictionary is a data structure initialized with curly braces {}

myCat = {'size': 'fat', 'color': 'grey', 'disposition': 'moody'}
#The keys are size, color and disposition. The values are fat, grey, and moody.

#Like you can print a speicifc index of a List, you can print a specific key of a dictionary:
print(myCat['size'])  #keys are not necessarily integers, as indexes are for lists.
                      #Dictionaries are unordered.

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 3', 'Carol': 'Oct 12'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()

    if name == '': break


    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)

    else:
        print('That person is not in the dictionary.')
        print('What is their birthday?')

        bday = input()
        birthdays[name] = bday

        print('Birthday database updated!')


#The .values() method:
for v in birthdays.values():
    print(v)

#The .keys() method:
for k in birthdays.keys():
    print(k)

#The .items() method:
for i in birthdays.items():
    print(i)

#The .get() method   arg 1 uses the value IF IT EXISTS, else uses arg 2.
print('Alices birthday is ' + birthdays.get('Alice', 'Nov 24') +'.')
print('Alices birthday is ' + birthdays.get('David', 'Nov 24') +'.')

#The .setdefault() method
#Instead of adding a key if it doesn't already exist, can use the setdefault method.
#This is similar to appending to a list.
birthdays.setdefault('species', 'humans')


#To print the contents of a dictionary on their own lines, use the pprint (pretty print) module:
from pprint import pprint
pprint(birthdays, width=20)
