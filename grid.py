import random
import time
import os


class gridMatrix:

    OutputMatrix = []
    OutputMatrixCopy = []
    flag = False
    actualGuesses = 0
    minimumGuesses = 0
    finalScore = 0
    mySet = set()
    setFlag = False
    scoreFlag = False

    def __init__(self):
        self.OutputMatrix = []
        self.OutputMatrixCopy = []
        self.flag = False
        self.actualGuesses = 0
        self.minimumGuesses = 0
        self.finalScore = 0
        self.mySet = set()
        self.setFlag = False
        self.scoreFlag = False

    """ Function that is used for printing title as per given format in the assignment"""
    def title(self):
        print("--------------------------")
        print("|       PEEK-A-BOO       |")
        print("-------------------------- \n")

    """ Function that is used to add distinct entries to set for calculation of score of player """
    def checkSet(self,val1):
         self.mySet.add(val1)

    """ Function that is used to create the matrix as per the given gridsize parameter"""
    def MatrixCreation(self,gridsize):
        lst = list(range(int((gridsize*gridsize/2))))
        lst = lst * 2
        # print(lst)
        random.shuffle(lst)
        # print(lst)

        for i in range(gridsize):
            row = []
            for j in range(gridsize):
                row.append(lst.pop())
            self.OutputMatrix.append(row)

        for i in range(gridsize):
            row = []
            for j in range(gridsize):
                row.append("X")
            self.OutputMatrixCopy.append(row)

    """ Function that contains all the logic for handling menu Option Select two elements like valid guess or wrong match and hiding the wrong pair along with calculation of final score"""
    def gridSelectTwoElements(self,gridsize,entry1,entry2):


            entry1List = list(map(str, entry1))
            entry2List = list(map(str, entry2))
            col1 = ord(entry1List[0]) - 65
            row1 = int (entry1List[1])

            col2 = ord(entry2List[0]) - 65
            row2 = int(entry2List[1])

            val1 = self.OutputMatrix[row1][col1]
            val2 = self.OutputMatrix[row2][col2]


            self.minimumGuesses = (gridsize*gridsize)/2



            if val1 == val2:
                if (entry1 not in self.mySet) or (entry2 not in self.mySet):
                    self.actualGuesses = self.actualGuesses+1
                    self.scoreFlag = True
                self.title()
                for col in range(gridsize):
                    print("\t[", chr(col + 65), "]", end=" ")
                print()
                print()
                for i in range(gridsize):
                    print("[", str(i), "]",end="\t  ")
                    for j in range(gridsize):
                        if i==row1 and j==col1:
                            self.OutputMatrixCopy[i][j] = self.OutputMatrix[i][j]
                            print(self.OutputMatrix[i][j],end="\t  ")
                        elif i==row2 and j==col2:
                            self.OutputMatrixCopy[i][j] = self.OutputMatrix[i][j]
                            print(self.OutputMatrix[i][j],end="\t  ")
                        else:
                            print(self.OutputMatrixCopy[i][j], end="\t  ")
                    print()
                self.checkSet(entry1)
                self.checkSet(entry2)
                if len(self.mySet) == gridsize*gridsize:
                    print()
                    self.finalScore = (self.minimumGuesses / self.actualGuesses) * 100
                    self.finalScore = round(self.finalScore,2)
                    if self.scoreFlag==True:
                        print()
                        print("Oh Happy Day. You 've won!! You score is:", self.finalScore)
                        print()
                    else:
                        print()
                        print("You cheated - Loser! You 're score is 0!")
                        print()
            else:
                if (entry1 not in self.mySet) or (entry2 not in self.mySet):
                    self.actualGuesses = self.actualGuesses + 1
                    self.scoreFlag = True
                self.title()
                for col in range(gridsize):
                    print("\t[", chr(col + 65), "]", end=" ")
                print()
                print()
                for i in range(gridsize):
                    print("[", str(i), "]",end="\t  ")
                    for j in range(gridsize):
                        if i == row1 and j == col1:
                            print(self.OutputMatrix[i][j], end="\t  ")
                        elif i == row2 and j == col2:
                            print(self.OutputMatrix[i][j], end="\t  ")
                        else:
                            print(self.OutputMatrixCopy[i][j], end="\t  ")
                    print()
                time.sleep(2)
                os.system("clear")
                self.title()
                for col in range(gridsize):
                    print("\t[", chr(col + 65), "]", end=" ")
                print()
                print()
                for i in range(gridsize):
                    print("[", str(i), "]", end="\t  ")
                    for j in range(gridsize):
                        print(self.OutputMatrixCopy[i][j], end="\t  ")
                    print()
                if len(self.mySet) == gridsize*gridsize:
                    print()
                    self.finalScore = (self.minimumGuesses / self.actualGuesses) * 100
                    self.finalScore = round(self.finalScore,2)
                    if self.scoreFlag==True:
                        print()
                        print("Oh Happy Day. You 've won!! You score is:", self.finalScore)
                        print()
                    else:
                        print()
                        print("You cheated - Loser! You 're score is 0!")
                        print()

    """Function that is used to uncover element as per the given element parameter as well as if players chooses only menu option two without making any valid guess along with final score calculation"""
    def uncoverElement(self,gridsize,element):

        elementList = list(map(str, element))
        col = ord(elementList[0]) - 65
        row = int(elementList[1])
        self.minimumGuesses = (gridsize * gridsize) / 2
        # counter = self.checkEntries(gridsize)
        if element not in self.mySet:
            self.actualGuesses = self.actualGuesses + 2
        self.title()
        for column in range(gridsize):
            print("\t[", chr(column + 65), "]", end=" ")
        print()
        print()
        for i in range(gridsize):
            print("[", str(i), "]", end="\t  ")
            for j in range(gridsize):
                if i == row and j == col:
                    self.OutputMatrixCopy[i][j] = self.OutputMatrix[i][j]
                    print(self.OutputMatrix[i][j],end="\t  ")
                else:
                    print(self.OutputMatrixCopy[i][j],end="\t  ")
            print()
        self.checkSet(element)
        if len(self.mySet) == gridsize * gridsize:
            self.finalScore = (self.minimumGuesses / self.actualGuesses) * 100
            if self.finalScore!= 0.0 and self.scoreFlag==True:
                print()
                self.finalScore = round(self.finalScore, 2)
                print("Oh Happy Day. You 've won!! You score is:",self.finalScore)
                print()
            else:
                print()
                print("You cheated - Loser! You 're score is 0!")
                print()


    """ Function to reveal the grid as per menu option 3"""
    def revealgrid(self,gridsize):
        self.title()
        for column in range(gridsize):
            print("\t[", chr(column + 65), "]", end=" ")
        print()
        print()
        for i in range(gridsize):
            print("[", str(i), "]", end="\t  ")
            for j in range(gridsize):
                    print(self.OutputMatrix[i][j], end="\t  ")
            print()



