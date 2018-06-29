# Board manager class

from gamemodules.colors import BColors
from gamemodules.constants import Constants as Const
import copy

class Board:

    # Init the board to empty cells
    def __init__(self, size):
        self.boardcount=0
        self.size=size
        # Board squares
        self.square = {'value': ' ', 'color': BColors.PURPLE, 'mask': Const.DefaultMask}
        row=[ self.square.copy() for i in range(0,size) ]
        self.board=[copy.deepcopy(row) for i in range(0,size)]

        # Set the boundaries of each square in the board. 0 means that side is at edge of board
        # E.g. A1 would have some of it's sides at the edge of the board
        # AI ignores checking outside of board by knowing which of the sides are on the edge
        for row in range(0,size):
            for col in range(0,size):
                # initialize mask
                mask = Const.DefaultMask
                # set bits to 0
                if col - 1 < 0:
                    mask = mask - (mask & (Const.ML | Const.TL | Const.BL))
                if col + 1 >= size:
                    mask = mask - (mask & (Const.MR | Const.TR | Const.BR))
                if row - 1 < 0:
                    mask = mask - (mask & (Const.TL | Const.TM | Const.TR))
                if row + 1 >= size:
                    mask = mask - (mask & (Const.BL | Const.BM | Const.BR))
                if mask != Const.DefaultMask:
                    self.board[row][col]['mask']= mask

    # Translate string square selectino input to internal board grid coordinates
    # starting at 0,0
    def translate_to_coords(self, coord):
        if len(coord) != 2:
            return (-1,-1)
        row = ord(coord[0]) - ord('A')
        col = int(coord[1]) - 1
        if row in range(0, self.size-1) and col in range(0, self.size-1):
            return [row, col]
        else:
            return (-1,-1)

    # Get the color string of the letter in that square
    def get_color_string(self, square):
        return square['color'].format(square['value'])

    def show(self):
        print('   ',sep='',end='')
        for i in range(0,self.size):
            print(' {} '.format(i+1),sep='',end='')
        print('')
        for row in enumerate(self.board):
            print('{}: '.format(chr(ord('A')+row[0])),sep='',end='')
            for col in row[1]:
                print('[',self.get_color_string(col),']',sep='',end='')
            print('\n',sep='',end='')

    # Set the letter with default color on the board if it is not occupied
    def set_letter(self, letter, row, col):
        if self.board[row][col]['value'] == ' ':
            self.board[row][col]['value'] =  letter
            self.board[row][col]['color'] = BColors.PURPLE
            self.board.boardcount += 1
        else:
            raise Exception("Cell is already occupied. Try another one")
