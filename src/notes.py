#!/usr/sbin/python
# Allows the terminal to read the notes.py

# Automating my note taking using LaTeX and Vim
import os
import subprocess
import math
import sys


class Notes:
    def __init__(self, folder):
        self.folder = folder


def makeNewFile():
    makeNewFile = input('To make a new file enter 1, if not press 2: ')
    if not(makeNewFile.isdigit()):
        while True:
            input4 = input('Please enter a number: ')
            if input4.isdigit():
                break


def enterNewFile():
    enterOldFile = str(input('To access an old file, type its name: '))
    if enterOldFile.isdigit():
        while True:
            input3 = input(('Please enter a name: '))
            if not(input3.isdigit()):
                break
    # calls AutomateNotes()
    autoMoteNotes()


def printPrompt():
    folderLst = ['calc']
    notesObj = Notes(folderLst)
    print('Automate Notes - Using LaTeX and Vim \n')
    print('Here are your current folders: ' + str(notesObj.folder))

    makeNewFile()
    enterNewFile()


def autoMoteNotes():
    if enterNewFile == str:
        print('test')


# def terminalCommand():
#     # # Command being used.
#     # p1 = Automate('notes', '12')
#     # p1.command = 'notes'

#     # # This is going to take in the argument from running the file
#     # for p1.command in sys.argv:
#     #     print(p1.command)
#     pass


def main():
    printPrompt()


if __name__ == "__main__":
    main()
