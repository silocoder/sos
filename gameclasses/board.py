
from utils.utils import BColors

class Board:
    # Board squares
    square = {'value': '-', 'color': 'black', 'mask': 0b111111}

    # Init the board to empty cells
    def __init__(self, size):
        self.defcolor = BColors.PURPLE
        self.size=size
        row=[ self.square.copy() for i in range(0,size) ]
        self.board=[row.copy() for i in range(1,size)]
        pass


    def get_color_string(self, square):
        return square[value]

    def show(self):
        for row in self.board:
            for col in row:
                print('[',col['value'],col['color'],']',sep='',end='')
            print('\n',sep='',end='')

        # print('[', sep="", end="")
        # print(']\n['.join([']['.join(row) for row in self.board]),sep="",end="]\n")


    # Set the letter with default color on the board if it is not occupied
    def set_letter(self, letter, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] =  self.defcolor + letter + BColors.ENDC
        else:
            raise Exception("Cell is already occupied. Try another one")

