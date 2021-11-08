#! python3

#This script converts a given string to pig latin.
#If a word begins with a vowel, the phrase "yay" is added to the end of it.
#If a word begins with a consonant or "ch" or "gr", it is moved to the end of it
#   followed by "ay".

def pigLatinConverter(myString):

    print(f"Original string: '{myString}'")
    splitString = myString.split(' ')
    vowels = ('a', 'e', 'i', 'o', 'u')

    for i, word in enumerate(splitString):

        if word[0] in vowels:
            splitString[i] = splitString[i]+"yay"
            continue

        for j in range(len(splitString[i])):

            if splitString[i][0] in vowels:
                splitString[i] = splitString[i]+"ay"
                break

            splitString[i] += splitString[i][0].lower()
            splitString[i] = splitString[i][1:]


    return ' '.join(splitString)



myString = "This is a sentence written by me"
pigString = pigLatinConverter(myString)

print(f"Pig string: '{pigString}'")
