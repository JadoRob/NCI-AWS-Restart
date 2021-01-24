import os
from colorama import Fore, Style
from os import system

# adds a new user to the system untin confirm == 'N'
def new_user():
    confirm = "N"
    while confirm != "Y":
        username = str(input("Please enter the name of the user you want to add: "))
        print("Add the user '" + username + "'? (Y/N)")
        confirm = str(input("")).upper()
        os.system("sudo adduser " + username)

# Create functions to delete user and add to groups