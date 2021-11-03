#! python3

#This is the mapIt script, an exercise in web scraping using the webbrowser module.
#This script copies an address from the command line and searches for it on Google Maps.

import webbrowser, sys, re

if len(sys.argv)!=2:
    print('Error: invalid number of arguments. Please specify an address in quotes.')

else:
    addressRegex = re.compile(r'\s')
    address = sys.argv[1]
    address = addressRegex.sub('+', address)
    webbrowser.open('google.com/maps/place/'+address)
