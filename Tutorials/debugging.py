#! python3

#This is a tutorial on debugging.

#Two features to catch bugs early are "logging" and "assertions".


#You can raise an exception error manually using the "raise" statement.

#raise Exception ('This is an error message.')


#When python crashes, the crash message is called the "Traceback".
#The traceback can also be stored as a string, which is used by the traceback module.
import traceback
try:
    raise Exception ('This is an error message.')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback was written to errorInfo.txt')



#An "assertion" is a sanity check to make sure your program isn't doing something horribly wrong, performed using the "assert" statement.
#If an assert statement returns False, the program stops via assertionError. If True, the statement does nothing.
ages = [25, 26, 29, 42, 15, 21, 53]
ages.reverse()
#assert ages[0]<=ages[-1]



#The "logging" module helps create a record of printout statements. It will specify any variables
# that you've defined and their values at that point.
import logging
#Uncomment this line to disable logging.
#logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname) s -  %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1

    for i in range(1, n+1):
        total *= i
        logging.debug(f'i is {i}, total is {total}.')
    logging.debug('End of factorial (%s%%) % (n)')

    return total

print(factorial(5))
logging.debug('End of program.')


#When using printouts to debug, you'll need to remove the print statements when done debugging.
#Logging has five levels: DEBUG, INFO, WARNlNG, ERROR, CRITICAL

#To output logging to a text file (to keep terminal from cluttering, remove basicConfig line above):
logging.basicConfig(filename='myLoggingFile.txt', level=logging.DEBUG, format=' %(asctime)s -  %(levelname) s -  %(message)s')
