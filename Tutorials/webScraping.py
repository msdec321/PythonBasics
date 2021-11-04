#! python3

'''
This is the web scraping tutorial.
Web scraping is using a program to download and process information from the Web.
There are several useful web scraping modules:
    webbrowser - Opens a browser to a specified webpage.
    requests - Downloads files and webpages from the internet.
    bs4 - Parses HTML (The format webpages are written in)
    selenium - Launches and controls a web browser. (Fill in forms and simulate mouse clicks)
'''

#To open a webpage
import webbrowser
#webbrowser.open('https://google.com')


#Downloading files
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
#Check that the request is good (True)
print(res.status_code==requests.codes.ok)
#To print the entirey of the text file..
#print(res.text)

#You can write it to a local file, but you must write it as a binary file to maintain unicode.
playFile = open("romeoAndJuliet.txt", "wb")
for chunk in res.iter_content(100000):
        playFile.write(chunk)

playFile.close()


#There is a large section on HTML that I've skipped over.

#Webpage interactions (clicking, logins, etc) with selenium
import selenium   #More likely to work long-term than requests. Many sites deliberately try to prevent web scraping of data.
from selenium import webdriver

#Open a webbrowser using selenium
browser = webdriver.Firefox()

#Finding elements
browser.get("https://inventwithpython.com")
try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' % (elem.tag_name))

except:
    print('Was not able to find an element with that class name.')

#Clicking the browser
browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Read Online for Free')
type(linkElem)
linkElem.click() # follows the "Read Online for Free" link


#Filling in fields automatically
browser.get('https://login.metafilter.com')
userElem = browser.find_element_by_id('user_name')
userElem.send_keys('your_real_username_here')

passwordElem = browser.find_element_by_id('user_pass')
passwordElem.send_keys('your_real_password_here')
passwordElem.submit()
