#!/usr/bin/python3
# Allows the terminal to read the notes.py

# Automating my note taking using LaTeX and Vim.
import os
import subprocess
import math
import sys

# Class Notes.

class Notes:
    # Constructor that contains the folder.
    def __init__(self, folder):
        self.folder = folder
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None

# Global list of Folders.
folderLst = []
noteObject = Notes(folderLst)

def createFolder(self):
    while True:
        current_path = os.getcwd()
        print("Your current path is: " + current_path)
        folder_input = input("Create a new folder or continue: ")
        if folder_input == "exit" or folder_input == "done":
            displayFolder(self)
            break    
        else:
            noteObject.folder.append(folder_input)
            
def createDirectory(self):
    for folders in noteObject.folder:
        str(folders)
    home = "~/12222"
    # path = os.path.join(home, folders)
    os.mkdir(home)

def displayFolder(self):
    if not noteObject.folder:
        print("You don't have any folders!")
    else:
        print("Your new folder(s) are: ")
        for index in noteObject.folder:
            print(index)
        createDirectory(self)


def main():
    print("Automate your notes using LaTeX and Vim!")
    print("Commands: 1. Exit 2. Done 3. Cont\n")
    createFolder(folderLst)


# Main function
if __name__ == "__main__":
    main()
