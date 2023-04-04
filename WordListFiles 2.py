import os
from os import system, name
import time

#Global variables
filename = input('Please enter the name of your txt file')
filePath = os.path.normcase("./word-lists/{0}".format(filename+'.txt'))
filestate = os.path.isfile(filePath)
words = []

#Functions 
def filenamechange():
    global filename
    filename = input('Please enter the name of your txt file')
    global filePath
    filePath = os.path.normcase("./word-lists/{0}".format(filename+'.txt'))
    global filestate
    filestate = os.path.isfile(filePath)

def clearScreen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def displayLine(char="=", lineLength=10, endChar="*"):
    print(endChar + char * (lineLength - (len(endChar) * 2)) + endChar)

#Show choices (Purely cosmetic)
def displaybox(menuWidth=60, menuLines=[]):
    clearScreen()
    insideWidth = menuWidth - 4
    displayLine("-", menuWidth, "+")
    for aMenuLine in menuLines:
        print("| {1:{0}} |".format(insideWidth, aMenuLine))
    displayLine("-", menuWidth, "+")

#Imports words from the file
def existingwords():
    filer = open(filePath, 'r')
    for item in filer:
        words.append(item.strip('\n'))
    filer.close()

#Reads words from words list
def readwords():
    temp = []
    count = 0
    for item in words:
        temp.append(item.strip('\n'))
        count += 1
        if count == 4:
            print(temp)
            temp = []
            count = 0
    print(temp)

#Validate that the min max numbers are integers
def validation(num):
    while True:
        try:
            word1 = int(num)
            return word1
        except ValueError:
            num = input("Please enter a valid number")

#THIS PART FIXED?? 15/03/2023
#Add new words function
def addwords():
    readwords()
    minlength = input("Please enter a minimum word length")
    minlength = validation(minlength)
    maxlength = input("Please enter a maximum word length")
    maxlength = validation(maxlength)
    
    while True:
        newword = input("Enter any words you would like to add. Enter nothing to exit")
        if newword == "":
            print("Word adding module exited")
            break
        elif len(newword) > int(maxlength):
            print("This word exceeds the designated max word length of", maxlength)
        elif len(newword) < int(minlength):
            print("This word is shorter than the designated minimum word length of", minlength)
        else:
            words.append(newword)
            readwords()
            print(newword, "successfully added")
        

#remove words function
def removewords():
    readwords()
    delword = input('Enter any word you would like to delete. Enter nothing to exit')
    if delword == '':
        return
    while True:
        if delword not in words:
            delword = input('Enter any word you would like to delete. They have to be from the list. Enter nothing to exit')   
        if delword == '':
            break
        if delword != '':
            words.remove(delword)
            readwords()
            print(delword, "has been successfully removed")
        
            
#Open file
def openfile():
    if filestate:
        print('The file','"'+filename+'"','has been found. This is its contents:')
        existingwords()    
        readwords()
        time.sleep(3) 
    else:
        name = input("That file does not exist. Would you like to create a new one with the same name? Y/N")
        if name.lower() == 'y':
            filePath = os.path.normcase("./word-lists/{0}".format(filename+'.txt'))
            filew = open(filePath, 'w')
            print('File with the name','"'+filename+'"','has been created')
            filew.close()
        else:
            newname = input("Please enter the new file's name")
            filePath = os.path.normcase("./word-lists/{0}".format(newname+'.txt'))
            filew = open(filePath, 'w')
            print('File with the name','"'+newname+'"','has been created')
            filew.close()

#Choicetree
def choicetree():
    choice = input("Please chose an option")
    options = ['0','1','2','3']
    while choice not in options:
        choice = input("Please choose an option")
    if choice == '0':
        clearScreen()
        return 'quit'
    elif choice == '1':
        clearScreen()
        addwords()
    elif choice == '2':
        clearScreen()
        removewords()
    elif choice == '3':
        clearScreen()
        filenamechange()
        global words
        words = []
        openfile()

def writing():
    filew = open(filePath, 'w')
    for item in words:
        filew.write(item + '\n')
    filew.close()


#Where the program starts
openfile()
while True:
    writing()
    choices = [
        "Please chose an option",
        "",
        "1) Add words to file",
        "2) Remove words from file",
        "3) Open new file",
        ""
        "0) Quit"]
    displaybox(60, choices)
    decision = choicetree()
    if decision == 'quit':
        break
writing()
print("Writing to file has finished")
print("Program exited")
