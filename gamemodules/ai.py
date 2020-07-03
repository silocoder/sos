# AIPlayer's brains

from gamemodules.colors import BColors
from gamemodules.constants import Constants as Const
import random

class AI:

    def __init__(self, board, name, letter):
        self.board=board
        self.size=board.size
        self.name=name
        self.letter=letter

        self.size = board.size
        self.sizex2=self.size**2
        pass

    def initAI(self):
        self.headCell = random.randint(0, self.sizex2-1)
        self.tailCell = (self.headCell + 1) % (self.sizex2)
        self.bestScore=[-1, -1, -9999]
        self.bestScoreBlock= [-1, -1, -9999]

    def getButtonLetterAtRow(self,row,col):
        return self.board.board[row][col]['value']
        pass

    def buttonPinAllowedFor(self, pin, i, j):
        return self.board.board[i][j]['mask'] & pin == pin
        pass

    def getScoreForLetterAtRow(self, letter, row, col):
        if letter=='S':
            return self.getScoreForLetterSAtRow(letter, row, col)
        else:
            return self.getScoreForLetterOAtRow(letter, row, col)

    # Gets the best score for letter S at row, col of board
    # // Get the AI score if we place a letter at this position.
    def getScoreForLetterSAtRow(self, letter, row, col):
        # For the letter S Scan all directions for the pins allowed to see what future letters could be used against us.
        score = 0
        dRow = -1
        dCol = -1
        allowed = True
        buttonLetters=[''] * 4
        buttonLetters[3] = ['-', '-', '-']
        tRow = -1
        tCol = -1
        cOTitle = 'O'
        cSTitle = 'S'
        cNoTitle = ' '
        # Go over each pin and test possibilities starting with our letter.
        buttonLetters[0] = letter
        for i in range(0, len(Const.CellSides)):
            # Ask gameModel for the pin to use based on direction
            allowed = self.buttonPinAllowedFor(Const.PinOrder[i][2], row, col)
            if allowed:  # We know there is 2nd button
                dRow = Const.PinOrder[i][0]
                dCol = Const.PinOrder[i][1]
                tRow = row + dRow
                tCol = col + dCol
                if tRow >= 0 and tCol >= 0 and tRow < self.board.size and tCol < self.board.size:
                    buttonLetters[1] = self.getButtonLetterAtRow(tRow, tCol)
                    tRow = tRow + dRow
                    tCol = tCol + dCol
                    # print(i, row, col, tRow, tCol)
                    if tRow>=0 and tRow<self.board.size and tCol>=0 and tCol<self.board.size:
                        buttonLetters[2] = self.getButtonLetterAtRow(tRow, tCol)

            # //		S	S	x	0
            # //		S	O	bl	-2
            # //		S	O	S	8
            # //		S	O	O	0
            # //		S	bl	bl	0
            # //		S	bl	S	-2
            # //		S	bl	O	0
            # // calculate score based on the letters.
            if buttonLetters[1] == cOTitle and buttonLetters[2] == cNoTitle:
                score = score - 2
            elif buttonLetters[1] == cNoTitle and buttonLetters[2] == cSTitle:
                score = score - 2
            elif buttonLetters[1] == cOTitle and buttonLetters[2] == cSTitle:
                score = score + 8

            buttonLetters[1] = '-'
            buttonLetters[2] = '-'

        return score



    # // Get the AI score if we place a letter at this position.
    def getScoreForLetterOAtRow(self, letter, row, col):
        # // For the letter S Scan all directions for the pins allowed to see what future letters could be used against us.
        score = 0
        buttonLetters = [''] * 4
        buttonLetters[3] = ['-', '-', '-']  # // 0=kOTitle

        tRow = -1
        tCol = -1
        cSTitle = 'S'
        cNoTitle = ' '

        # // Go over each pin and test possibilities starting with our letter.
        # // Only do the first 4 pins since we check their opposites
        buttonLetters[0] = letter
        for i in range(0, int(len(Const.CellSides) / 2)):
            # // Ask gameModel for the pin to use based on direction
            tRow = row + Const.PinOrder[i][0]
            tCol = col + Const.PinOrder[i][1]
            if tRow >= 0 and tCol >= 0 and tRow < self.board.size and tCol < self.board.size:
                buttonLetters[0]=self.getButtonLetterAtRow(tRow, tCol)
                tRow=row+Const.PinOrder[i+4][0]
                tCol=col+Const.PinOrder[i+4][1]
                if tRow >= 0 and tCol >= 0 and tRow < self.board.size and tCol < self.board.size:
                    buttonLetters[2] = self.getButtonLetterAtRow(tRow, tCol)

            # //		bl	O	bl	0
            # //		S	O	S	8
            # //		S	O	bl	-2
            # //		O	O	O	0
            # //		O	O	bl	0
            # //		S	O	O	0
            # // calculate score based on the letters.
            if buttonLetters[0] == cSTitle and buttonLetters[2] == cSTitle:
                score = score + 8
            elif buttonLetters[0] == cSTitle and buttonLetters[2] == cNoTitle:
                score = score - 2
            elif buttonLetters[2] == cSTitle and buttonLetters[0] == cNoTitle:
                score = score - 2

            buttonLetters[0] = '-'
            buttonLetters[2] = '-'

        return score

    # AI determines and returns best row column to place the letter
    def getRowCol(self):
        self.initAI()
        resRow=-1
        resCol=-1
        row = -1
        col = -1
        score = 0

        # Which letter is the AI?
        pLetter=['S','O']
        if self.letter=='O':
            pLetter[0]='O'
            pLetter[1]='S'

        while True:  # letter S
            row, col = self.findNextEmptyCellAtRow()
            if [row, col] >= [0, 0]:
                score = self.getScoreForLetterAtRow(pLetter[0], row, col)
                if score > self.bestScore[2]:
                    self.bestScore[2] = score
                    self.bestScore[0] = row
                    self.bestScore[1] = col

            else:
                if score <= 0:  # Now check if we have score <=0 and try to block for the opposite letter.
                    self.headCell = random.randint(0, self.sizex2 - 1)
                    self.tailCell = (self.headCell + 1) % (self.sizex2)
                    while True:  # See if O will score for them. If yes, we block this.
                        row, col = self.findNextEmptyCellAtRow()
                        if [row, col] >= [0, 0]:
                            score = self.getScoreForLetterAtRow(pLetter[1], row, col)
                            if score > self.bestScoreBlock[2]:
                                self.bestScoreBlock[2] = score
                                self.bestScoreBlock[0] = row
                                self.bestScoreBlock[1] = col

                        else:
                            if self.bestScoreBlock[2] > self.bestScore[2]:
                                self.bestScore[2] = self.bestScoreBlock[2]
                                self.bestScore[0] = self.bestScoreBlock[0]
                                self.bestScore[1] = self.bestScoreBlock[1]

                            break

                # // while for the letter O
                # // if score<=0

                break

        # // while for letter S


        if self.bestScore[0] >= 0:
            resRow = self.bestScore[0]
            resCol = self.bestScore[1]
        return (resRow, resCol)
        pass


    # // Find empty one starting at the tail. Return YES if found.
    # // Uses head and tail++. when tail==head then returns NO.
    def findNextEmptyCellAtRow(self):
        row = -1
        col = -1
        if self.tailCell < 0:
            return (-1, -1)
        # // Start at tail
        cellIndex = self.tailCell
        while cellIndex > self.headCell and cellIndex < self.sizex2:
            row = int(cellIndex / self.board.size)
            col = cellIndex % self.board.size
            self.tailCell = (cellIndex + 1) % (self.sizex2)  # Set next pointer
            if self.getButtonLetterAtRow(row, col) == ' ':
                return (row, col)
            cellIndex += 1

        # Start at 0
        cellIndex = self.tailCell
        while cellIndex <= self.headCell:
            row = int(cellIndex / self.board.size)
            col = cellIndex % self.board.size
            if self.headCell == self.tailCell:
                self.tailCell = -1
            else:
                self.tailCell = (cellIndex + 1) % (self.sizex2);  # // Set next pointer

            if self.getButtonLetterAtRow(row, col) == ' ':
                return (row, col)

            cellIndex += 1
        return (-1, -1)