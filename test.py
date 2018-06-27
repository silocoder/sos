# import sys
# print(dir())
# print(',\n'.join(sys.path) )
print("\033[91m{}\033[00m".format('XXXXX'))

from gameclasses.board import Board
from gameclasses.player import Player
from utils.utils import dump
from utils.utils import BColors

board=Board(10)
human=Player('Costas', 'O')
computer=Player('Computer','S')

human.play(board, 2, 2)
computer.play(board, 3, 2)
human.play(board, 2, 2)

board.show()

human.print()
human.scored()
human.print()

dump(human)
dump(Player)


