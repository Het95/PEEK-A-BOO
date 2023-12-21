import sys
from grid import *
import os

""" Function that is used for printing title as per given format in the assignment"""
def title():
    print("--------------------------")
    print("|       PEEK-A-BOO       |")
    print("-------------------------- \n")

""" Function to print the matrix as per the given gridsize which is given as command line argument
having one parameter gridSize """
def printgrid(gridSize):
    if gridSize==2:
        print("    [A] [B]")
        print("[0]  X   X")
        print("[1]  X   X \n")
    elif gridSize==4:
        print("    [A] [B] [C] [D]")
        print("[0]  X   X   X   X")
        print("[1]  X   X   X   X")
        print("[2]  X   X   X   X")
        print("[3]  X   X   X   X \n")
    elif gridSize==6:
        print("    [A] [B] [C] [D] [E] [F]")
        print("[0]  X   X   X   X   X   X")
        print("[1]  X   X   X   X   X   X")
        print("[2]  X   X   X   X   X   X")
        print("[3]  X   X   X   X   X   X")
        print("[4]  X   X   X   X   X   X")
        print("[5]  X   X   X   X   X   X \n")

""" Function that shows the menu Option as per given in the assignment on console"""
def display():

    arglist = sys.argv
    gridSize = int(arglist[1])



    title()
    printgrid(gridSize)


    gridObj = gridMatrix()
    gridObj.MatrixCreation(gridSize)
    printFlag = False
    newFlag = False
    while True:

        if newFlag==True:
            title()
            printgrid(gridSize)
            newFlag = False
        print("1. Let me select two elements")
        print("2. Uncover one element for me")
        print("3. I give up - reveal the grid")
        print("4. New game")
        print("5. exit")


        choice = input("Enter your choice: ")

        if choice=='1':

            if printFlag==True:
                continue

            entry1 = input("Enter cell coordinates: ").upper().strip()
            entry2 = input("Enter cell coordinates: ").upper().strip()
            entry1List = list(map(str, entry1))
            entry2List = list(map(str, entry2))
            while True:
                if entry1List[0].isdigit() or entry1List[1].isalpha():
                    print("Enter valid format for column and rows for cell 1")
                    entry1 = input("Enter cell coordinates: ").upper().strip()
                    entry2 = input("Enter cell coordinates: ").upper().strip()
                    entry1List = list(map(str, entry1))
                    entry2List = list(map(str, entry2))
                elif entry2List[0].isdigit() or entry2List[1].isalpha():
                    print("Enter valid format for column and rows for cell 2")
                    entry1 = input("Enter cell coordinates: ").upper().strip()
                    entry2 = input("Enter cell coordinates: ").upper().strip()
                    entry1List = list(map(str, entry1))
                    entry2List = list(map(str, entry2))
                elif int(entry1List[1]) not in range(gridSize) or (ord(entry1List[0]) > (65+gridSize-1) or ord(entry1List[0]) < (65)):
                    print("Input error: coloumn entry is out of range for this grid. Please try again")
                    entry1 = input("Enter cell coordinates: ").upper().strip()
                    entry2 = input("Enter cell coordinates: ").upper().strip()
                    entry1List = list(map(str, entry1))
                    entry2List = list(map(str, entry2))
                elif (int(entry2List[1]) not in range(gridSize)) or (ord(entry2List[0]) > (65+gridSize-1) or ord(entry2List[0]) < (65)):
                    print("Input error: coloumn entry is out of range for this grid. Please try again")
                    entry1 = input("Enter cell coordinates: ").upper().strip()
                    entry2 = input("Enter cell coordinates: ").upper().strip()
                    entry1List = list(map(str, entry1))
                    entry2List = list(map(str, entry2))
                elif entry1==entry2:
                    print("Please Enter different cell coordinates")
                    entry1 = input("Enter cell coordinates: ").upper().strip()
                    entry2 = input("Enter cell coordinates: ").upper().strip()
                    entry1List = list(map(str, entry1))
                    entry2List = list(map(str, entry2))
                else:
                    gridObj.gridSelectTwoElements(gridSize, entry1, entry2)
                    break
            # print()
        elif choice=='2':
            if printFlag==True:
                continue

            element = input("Enter cell coordinates which you want to reveal: ").upper().strip()
            elementList = list(map(str, element))
            while True:
                if elementList[0].isdigit() or elementList[1].isalpha():
                    print("Enter valid format for column and rows for cell")
                    element = input("Enter cell coordinates which you want to reveal: ").upper().strip()
                    elementList = list(map(str, element))
                elif int(elementList[1]) not in range(gridSize) or (ord(elementList[0]) > (65+gridSize-1) or ord(elementList[0]) < (65)):
                    print("Input error: coloumn entry is out of range for this grid. Please try again")
                    element = input("Enter cell coordinates which you want to reveal: ").upper().strip()
                    elementList = list(map(str, element))
                else:
                    gridObj.uncoverElement(gridSize,element)
                    break
        elif choice=='3':
            gridObj.revealgrid(gridSize)
            printFlag = True
        elif choice=='4':
            os.system("clear")
            gridObj = gridMatrix()
            gridObj.MatrixCreation(gridSize)
            newFlag = True
            printFlag = False
        elif choice=='5':
            break
        else:
            print("Enter Valid Input")





if __name__ == '__main__':
    display()

