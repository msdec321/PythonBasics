#This is the Collatz Sequence script.

def collatz(number):
    if number%2==0:
        return number//2
    else:
        return 3*number+1


print('Input a starting integer: ')
while True:

    try:
        value = int(input())
        break

    except ValueError:
        print('Error: Please input an integer: ')


while value!=1:
    value = collatz(value)
    print(value)
