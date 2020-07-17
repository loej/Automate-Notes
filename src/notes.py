#!/usr/sbin/python
# Allows the terminal to read the notes.py

# Automating my note taking using LaTeX and Vim
import os
import subprocess
import math
import sys

# Class notes.


class Notes:
    # Constructor that contains the folder.
    def __init__(self, folder):
        self.folder = folder


# Global list of directories.
folderLst = ['calc']

# Initial input value to create folder or continue program.


def inputValueInt():
    makeNewFile = input('Create a folder or continue: ')
    if not(makeNewFile.isdigit()):
        while True:
            checkforNumber = input('Please enter a number: ')
            if checkforNumber.isdigit():
                break
            return makeNewFile

# Input value to search for a new folder.


def inputValueString():
    enterOldFile = str(input('Access created files: '))
    if enterOldFile.isdigit():
        while True:
            checkforString = input(('Please enter a name: '))
            if not(checkforString.isdigit()):
                break
            return enterOldFile
    # calls AutomateNotes()
    autoMoteNotes(enterOldFile)

# Displays prompt and options for the user.


def printPrompt():
    notesObj = Notes(folderLst)
    # print('\n')
    print('Automate Your Notes Using LaTeX and Vim \n ')
    # print('<----------------------------------->')
    print('Options:\n + To create a new folder enter 1, to continue press 2. \n + To open an existing file enter its name. \n')
    print('Current Folders: \n' + str(notesObj.folder) + '\n')

    inputValueInt()
    inputValueString()

# Automates notes using terminal and import os.


def autoMoteNotes(x):
    # objectNotes = Notes(folderLst)
    # for h in range(len(objectNotes.folder)):
    #     print(h)
    if not(x.isdigit()):
        print('success')
    path = os.getcwd()
    print('the path is: %s' % path)


def main():
    printPrompt()


# Main function
if __name__ == "__main__":
    main()
