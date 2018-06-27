
from utils.utils import BColors
class Player:
    def print(self):
        print("Player: %s-%s, Score: %s" % (self.name, self.letter, self.score))

    def __init__(self, name, letter):
        self.letter=letter
        self.name=name
        self.score=0
        pass

    # Add one to score
    def scored(self):
        self.score+=1
        pass

    # play the turn and add letter
    def play(self, board, row, col):
        try:
            board.set_letter(self.letter, row, col)
        except Exception as msg:
            print(msg)