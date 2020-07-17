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


class Vim:
    pass


class Automate:

    pass


def printPrompt():
    print('Automate Notes - Using LaTeX and Vim \n')
    print('Here are your current folders: ' + str(notesObj.folder))
    try:
        newFolder = int(
            input('To make a new folder for a class press input 1: '))
        useFolder = str(
            input('To access your previous files just type the name: '))
    except ValueError:
        print('Oops! that is not a valid input')

    # Calling autoMateNotes function


def autoMateNotes():
    if printPrompt().newFolder == 1:
        print('test')
    else:
        sys.exit()


def terminalCommand():
    # Command being used.
    p1 = Automate('notes', '12')
    p1.command = 'notes'

    # This is going to take in the argument from running the file
    for p1.command in sys.argv:
        print(p1.command)


def main():
    printPrompt()
    autoMateNotes()


if __name__ == "__main__":
    main()
