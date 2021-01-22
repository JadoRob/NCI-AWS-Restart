import os
from colorama import Fore, Style
from os import system


# Declare variables
stringValue = "This is a string"
intValue = 5
floatValue = 5.99

system('cls')

# output using print
print(Fore.RED + 'some red text')
print(Style.RESET_ALL)
# different ways to print strings using single, double, or triple quotes
print('This is single quotes - \033[1;31;40m"Really?"') # this print is single quotes 
print("This is double quotes inside \033[1;31;40m\"double\" quotes")
print("It's just \033[1;31;40mdouble quotes")
print(''' This is \033[1;31;40mtriple quotes''')
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
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
counter = 1
for day in days:
    print(counter, day)
    counter += 1

emptyDictionary = {}
emptyDictionary['name'] = input('Enter your first name >> ')
emptyDictionary['lname'] = input('Enter your last name >>')
print()

