SOS Python game (Work in Progress)
==================================

This is a game whose logic I translated from Objective-C I had developed for the iPhone.

The game of SOS is similar to tic tac toe except that one player gets to use the letter S and another player gets to use the letter O and place them onto a free square on the board.

If when an S or an O is placed and any of the adjacant letters form SOS you score a point. Sometimes it is possible to have mutliple SOS combinations when you place a letter so you score a point for each one.

The Human player chooses the letter S or O and goes first by placing his letter in any square on the board. The Computer AI then determines where to place its letter. As the board fills up the Human and the Computer try to either block the opponent from making an SOS or they actually see an opportunity to put their letter down and form SOS.

The game is written in Python and the output is to the terminal. Every time the player plays, the Computer also plays. When the board is filled, there is a winner.

What is missing
===============
Player scoring is not implemented yet but there is a placeholder class called Referee. Although the AI will detect and place its own letter on the board in a sensible square, and challenge the player, the Referee module needs to be implemented and determine that in fact an SOS has been formed and thereby award the player a point.

So after every player move, the Referee needs to be involved to see if an SOS is done.

Sample Board on Terminal
========================
```
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
```

Code:
=====

The sosstart.py starts up the application.
player.py is an abstract class. It is inherited both by human player and ai player.
the ai.py contains all the logic to determine where to put its letter. It uses its internal scoring system to determine what is the best play. The idea it first finds a random empty cell. It then 'plays' it. Checks whether it will help the opponent or help the AI. Once the best internal score is found, it chooses that as its move.

I tried to avoid using outside modules where possible to make it easy to copy and use. Feel free to use it in anyway you like. 
