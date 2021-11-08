#This is a tutorial on using command line arguments in scripts.

import sys


if len(sys.argv) < 2:
    print('Usage: python3 script.py [keyphrase] - description here')
    sys.exit()
    
    
variable1 = sys.argv[1]   # first commandline arg saved to variable1.
