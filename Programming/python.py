import os
from colorama import Fore, Style
from os import system
from os import system, mkdir, listdir, getcwd, getenv, getlogin
#Notes taken for AWS Restart course, from Professor Dunieski Otano 

# Declare variables
stringValue = "This is a string"
intValue = 5
floatValue = 5.99

system('clear')

# output using print
def printFunction():
    print(Fore.RED + 'some red text')
    print(Style.RESET_ALL)
    # different ways to print strings using single, double, or triple quotes
    print('This is single quotes - "Really?"') # this print is single quotes 
    print("This is double quotes inside \"double\" quotes")
    print("It's just double quotes")
    print(''' This is triple quotes''')
    print(Style.RESET_ALL)



# Functions 
def showDataType():
    print(f'The stringValue variable is of type {type(stringValue)}')
    print('The stringValue variable is of type {}'.format(type(stringValue)))

def my_function():
  print("Hello from a function") 

def myName():
    print("My name is Rob")

def greeting():
    print("Hello World!")


# Lists, Dictionaries, 
def myCollections():
    myDictionary = {
        'Integer': 4,
        'Float': 3.6,
        'String': 'This is a dictionary in Python',
        'Boolean': True,
        'FirstName': 'Pushpa',
        'Lastname': 'Munagala',
        'Age': 25
    }

    #add another key and value 
    #myDictionary = {'phone': 1234567890}

    print(myDictionary)
    # ways to print a value of a dictionary using the key
    print(f"First Element => {myDictionary['Integer']}")
    print(f"First Element => {myDictionary.get('Integer')}")
    keys = myDictionary.keys()
    print(keys)
    print()

    # print the key and value (2 different syntax)
    for key in myDictionary:
        print(myDictionary[key])
        print(myDictionary.get(key))
    print()

    for key, value in myDictionary.items():
        print(f"'{key}': {value}")
    print()

# Loops
def myLoops():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    counter = 1
    for day in days:
        print(counter, day)
        counter += 1

    emptyDictionary = {}
    emptyDictionary['name'] = input('Enter your first name >> ')
    emptyDictionary['lname'] = input('Enter your last name >>')
    print()

#Exceptions
def catchExeption():
    num1 = int(input('Enter a number >> '))
    num2 = int(input('Enter another number >> '))

    try:
        division = round(num1 / num2, 2)
        print('division = {}'.format(division))
    except ZeroDivisionError: print(f'Division by {num2} is not allowed')


#os-module library
def osModule():
    print(' ')
    print('Here is a list of the directory: ')
    directories = listdir()
    print(directories)
    print(' ')
    print('This is the working directory: ')
    cwd = getcwd()
    print(cwd)
    print(' ')
    print('Here is a list of directories and files including permissions: ')
    listOfDirectoriesAndFiles = system('ls -lah')
    print(listOfDirectoriesAndFiles)

#checks
#convert to uppercase and compare to 'Y' to verify input.
choice = str(input("")).upper()
if choice == "Y":
    print('You entered yes.')
else:
    print('Invalid input.')

#Execute functions here
osModule()