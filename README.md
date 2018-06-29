SOS Python game (Work in Progress). 
This is a game whose logic I translated from Objective-C. 

The game of SOS is similar to tic tac toe except that one player gets to use the letter S and another player gets to use the letter O and place them onto a free square on the board.

If when an S or an O is placed and any of the adjacant letters form SOS you score a point. Sometimes it is possible to have mutliple SOS combinations when you place a letter so you score a point for each one.

The Human player chooses the letter S or O and goes first by placing his letter in any square on the board. The Computer AI then determines where to place its letter. As the board fills up the Human and the Computer try to either block the opponent from making an SOS or they actually see an opportunity to put their letter down and form SOS.

The game is written in Python and the output is to the terminal. Every time the player plays, the Computer also plays. When the board is filled, there is a winner.

What is missing:
Player scoring is not implemented yet but there is a placeholder. Although the AI will detect and place its letter on the board and challenge the player, the Referee module needs to be implemented and determin that in fact an SOS has been formed and thereby the player will get a point(s).

Sample Board on Terminal
========================
Hello Human. I am Computer Let's play SOS !
Please choose the letter S or O (Humans play first haha!): S
Human you will play letter S, and I will play letter O. 


Enter Board square as Row Letter and Col Number (E.g. B6): e4
    1  2  3  4  5  6 
A: [ ][ ][ ][ ][ ][ ]
B: [S][ ][ ][S][ ][ ]
C: [ ][S][ ][ ][ ][ ]
D: [ ][O][O][ ][ ][ ]
E: [ ][S][O][S][ ][ ]
F: [O][ ][O][ ][ ][ ]
