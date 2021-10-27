#This is a script on pattern finding without using regular expressions.

def isPhoneNumber(number):
    if len(number)!=12: return False

    for i in range(0,2):
        if not number[i].isdecimal(): return False

    if number[3]!='-': return False

    for i in range(4,6):
        if not number[i].isdecimal(): return False

    if number[7]!='-': return False

    for i in range(8,11):
        if not number[i].isdecimal(): return False

    return True


print('Is 415-664-8132 a phone number?')
print(isPhoneNumber('415-664-8132'))

print('Is moshi moshi a phone number?')
print(isPhoneNumber('moshi moshi'))

message = "Matthew's phone number is 415-664-8132"
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print(f"Matthew's phone number is {chunk}.")

#Pattern findind without regular expressions is long and tedious.

#------------------------

#What about using regular expressions (regex)?
#All regex functions are incorporated into the "re" module.
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  #Note the RAW string.
#The var phoneNumRegex now contails a regular expression object.

#The .search() method used on a regex object can search a string for a pre-defined regex.
#  The .group() method will return the string that matches the regex object.
mo = phoneNumRegex.search('My phone number is 408-659-5969.')    #mo is short for 'match object'
print('Phone number found: ' + mo.group())

#Compare the number of lines it took to complete the same task.
#Regex character classes:
#  \d  - digit
#  \s  - whitespace (space, tab, newline)
#  \w  - alphanumeric
#  \(  - escape characters (. ^ $ * + ? { } [ ] \ | ( ) )
# (capitalized = non-*)

#Adding parentheses to a regex object will create a "group"
phoneNumRegex  = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
#Note that after calling the compiler, you have to redefine the regex object again.
mo = phoneNumRegex.search('My phone number is 408-659-5969.')
#Then you can pull specific groups.
print('First three digits: ' + mo.group(1))
print('Second three digits: ' + mo.group(2))
print('Last four digits: ' + mo.group(3))


#You can define multiple regex objects using the pipe "|". It will always pick out the first occurance in the regex object.
nameRegex  = re.compile(r'Batman|Tina Fey')
mo1 = nameRegex.search('My two favrotie people are Batman and Tina Fey!')
mo2 = nameRegex.search('My two favrotie people are Tina Fey and Batman!')

print('First occurance in mo1: ' + mo1.group())
print('First occurance in mo2: ' + mo2.group())


#You can do optional matching using the question mark ( )?
nameRegex  = re.compile(r'Bat(wo)?man')
mo1 = nameRegex.search('My character is Batman.')
print(mo1.group())

mo2 = nameRegex.search('My character is Batwoman.')
print(mo2.group())


#Matching ZERO or more times with ( )*
nameRegex  = re.compile(r'Bat(wo)*man')
mo1 = nameRegex.search('My character is Batman.')
print(mo1.group())

mo2 = nameRegex.search('My character is Batwowowoman.')
print(mo2.group())


#Matching ONE or more times with ( )+
nameRegex  = re.compile(r'Bat(wo)+man')
mo1 = nameRegex.search('My character is Batwoman.')
print(mo1.group())

mo2 = nameRegex.search('My character is Batwowowoman.')
print(mo2.group())


#Matching specific repetitions with braces ( ){N}
nameRegex  = re.compile(r'Bat(wo){3}man')
mo = nameRegex.search('My character is Batwowowoman.')
print(mo.group())   #Can also do {N,M} and it will tend toward M instances. (greedy vs lazy)


#While the .search() method will find the first instance, the .findall() method will find all instances.
#Note the output is a List object.
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall('Work: 408-882-4123, Cell: 408-659-5969'))


#You can create your own character classes using brackets [ ]
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('This is a sentence written by me.'))

#Or exclusively using the ^ character.
vowelRegex = re.compile(r'[^aeiouAEIOU]')
print(vowelRegex.findall('This is a sentence written by me.'))


#Require string start (^) or end ($) with an expression.
beginsWithHello = re.compile(r'^Hello')
endsWithNumber = re.compile(r'\d$')
print(beginsWithHello.search('Hello world'))
print(endsWithNumber.search('Hello 9'))

#Or both start and end using ^+$
startAndEnd = re.compile(r'^\d+$')
print(startAndEnd.search('12345'))


#The wildcard (.) with the .findall( ) method
myWildcard = re.compile(r'.at')
print(myWildcard.findall('The fat cat sat on my hat.'))

#Match anything using wildcard and * (.*)
matchAll = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = matchAll.search('First Name: Matthew Steven Last Name: Decaro')
print(mo.group(1)) ; print(mo.group(2))

#To match everything AND the newline character, use the re.DOTALL argument
matchAll = re.compile('(.*)', re.DOTALL)
mo = matchAll.search('First Name: Matthew Steven \n Last Name: Decaro')
print(mo.group())


#Normal regex are case sensitive. To be case insensitive, use the re.I argument.
roboCop = re.compile(r'rObOcoP', re.I)
mo = roboCop.search('My favorite character is robocop.')
print(mo.group())


#Regex can not only find, but find and replace via the sub method.
namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.sub('CENSORED', 'Agent Alice talked to Agent Bob this morning.')
print(mo)


#Complicated regular expressions should be spread over multiple lines with re.VERBOSE to improve readability.
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?   #area code
    (\s|-|\.)?           #seperator
    )''', re.VERBOSE)


#re.compile only takes one extra argument. What if you want to use more? Use pipe | ("bitwise operator")
someRegex = re.compile(r'foo', re.IGNORECASE | re.DOTALL)
