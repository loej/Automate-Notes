#!/usr/sbin/python
# Allows the terminal to read the python file

# Automating my note taking using LaTeX and Vim
import os
import subprocess
import math
import sys


class Notes:
    # Prints the welcoming prompt in terminal.
    pass


class Vim:
    pass


class Automate:

    def __init__(self, command, location):
        self.command = command
        self.location = location


def printPrompt():
    print('test')


def terminalCommand():
    # Command being used.
    p1 = Automate('notes', '12')
    p1.command = 'notes'

    # This is going to take in the argument from running the file
    for p1.command in sys.argv:
        print(p1.command)
    print('hello')


def main():
    printPrompt()
    terminalCommand()


if __name__ == "__main__":
    main()
