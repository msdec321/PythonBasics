#This script checks user input until a valid input is provided.


while True:
    print('Enter your age: ')

    age = input()

    if age.isdecimal():
        break

    print('Please enter a number for your age. (Example: 24): ')


while True:
    print('Please enter your first and last name: ')

    name = input()

    if name.istitle():
        break

    print('Please use correct capitalization. (Example: John Smith): ')
