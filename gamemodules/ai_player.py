#AI player class

from gamemodules.player import Player
from gamemodules.ai import AI

class AIPlayer(Player):

    def __init__(self, board, name,letter):
        self.board=board
        # Player(name,letter)
        super(AIPlayer, self).__init__(self.board, name, letter)
        # Initialize AI
        self.ai = AI(self.board, name, letter)
        pass

    def play(self, row, col):
        row, col = self.ai.getRowCol()
        super(AIPlayer, self).play(row, col)
        pass