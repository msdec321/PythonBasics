#Try/except statements can be used to continue running code despite an error occuring, so your
#  program will not crash even in the event of a forseeable error.

def spam(divideBy):

    try:
        value = 42. / divideBy

    except ZeroDivisionError:   #Must know exact error name.
        print('Divide by zero error.')

print(spam(10.))
print(spam(5.))
print(spam(0.))
print(spam(15.))
