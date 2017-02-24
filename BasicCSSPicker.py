########################
# Author: Derric Pullen
# Basic CSS Generator
########################

import sys


def main():

    usrInput = getUserInput()

    if usrInput == 1:
        bgPicker()

    elif usrInput == 2:
        fontPicker()

    elif usrInput == 3:
        tablePicker()

    elif usrInput == 4:
        sys.exit()
        
    else:
        print("There was an error.")

def getUserInput():
    
    print("Welcome to the basic CSS Generator!")
    print("1 - Background Color Picker")
    print("2 - Font Picker")
    print("3 - Table Picker")
    print("4 - Exit" + \n)

    print("Enter a number 1-4." + \n)

    usrInput = input()

    while usrInput not in [1, 2, 3, 4]:
        print(usrInput + " is not valid input. Please input a number 1-4.")
        usrInput = input()

    return usrInput

def bgPicker():

    bgColor = ""
    print("This is the background color picker.")
    print("You may enter 3 integers each between 0-255")
    print("")


def fontPicker():
    print("This is the font picker.")
    print("You can pick from these five fonts.")
    print("1 - Arial")
    print("2 - Comic Sans MS")
    print("3 - Times New Roman")
    print("4 - ")
    print("5 - Sans serif")
    print("")
    print("")
    print("")


def tablePicker():
    
