# Scoring the players' class

class Referee:

    def __init__(self, board):
        self.board=board
        pass

    def getScore(self, player):
        player.score += 1
        return player.score
        pass