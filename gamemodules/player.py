# Abstract class to create players

class Player:
    def print(self):
        print("Player: %s-%s, Score: %s" % (self.name, self.letter, self.score))

    def __init__(self, board, name, letter):
        self.board = board
        self.letter=letter
        self.name=name
        self.score=0

    # Add one to score
    def scored(self):
        self.score+=1

    # play the turn and add letter
    def play(self, row, col):
        try:
            self.board.set_letter(self.letter, row, col)
        except Exception as msg:
            print(msg)