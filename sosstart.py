# Start the game

from gamemodules.board import Board
from gamemodules.human_player import HumanPlayer
from gamemodules.ai_player import AIPlayer
from gamemodules.referee import Referee

from gamemodules.colors import BColors
from utils.utils import dump

# Initialize board, AI and players info
def getPlayerInfo():
    sosLetters=('S','O')
    aiName='Computer'
    humanName = 'Human'
    hLetter=''
    print(BColors.BLUE.format(f"Hello. I am {aiName} Let's play SOS !"))
    while hLetter not in sosLetters:
        hLetter = input (BColors.BLUE.format("Please choose the letter S or O (Humans play first haha!): ")).upper()
        if hLetter=='S':
            aiLetter= 'O'
        elif hLetter=='O':
            aiLetter= 'S'
        else:
            pass

    print(f"{humanName} you will play letter {hLetter}, and I will play letter {aiLetter}. ")
    return (hLetter, humanName, aiLetter, aiName)

##################### Main Game Start ##################################

hLetter, humanName, aiLetter, aiName = getPlayerInfo()
# Create the play board
board = Board(4)

# Create human player
human = HumanPlayer(board, humanName, hLetter)

# Create computer player
ai = AIPlayer(board, aiName, aiLetter)

# Initialize score calculator for players
referee = Referee(board)

########### Game Loop ###############
while True:
    # Show board
    board.show()
    if board.boardcount == board.size ** 2:
        print(f"Game over! {human.name}'s score is {human.score}, {ai.name}'s score is {ai.score}")
        quit = input("Press q to quit").upper()
        if quit == 'Q':
            exit()
        else:
            continue

    row,col=(-1,-1)
    while (row,col) <(0,0) or (row,col) > (board.size-1,board.size-1):
        coord = input('\nEnter Board square as Row Letter and Col Number (E.g. B6): ').upper()
        row, col = board.translate_to_coords(coord)


    # Human moves and get score
    human.play(row, col)
    human.score=referee.getScore(human)

    #AI moves and get score
    ai.play(row, col)
    ai.score=referee.getScore(ai)

