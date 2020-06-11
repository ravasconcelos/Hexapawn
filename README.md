# Hexapawn – Intelligent Agent

Rodolfo Vasconcelos

SCS 3547 – Intelligent Agents & Reinforcement Learning

UNIVERSITY OF TORONTO - SCHOOL OF CONTINUING STUDIES

Instructor: Larry Simon

## About the game

Hexapawn is a deterministic two-player game played on a rectangular 3×3 board. Each player begins with 3 pawns, one for each square in the row closest to them. The goal of each player is to advance one of their pawns to the opposite end of the board or to prevent the other player from moving.

This project stored in GitHub: https://github.com/ravasconcelos/Hexapawn

* Wikipedia: https://en.wikipedia.org/wiki/Hexapawn
* Graphical game example: https://www.greenfoot.org/scenarios/23788

## About the Project

This code uses the minmax agent implemented in the book "Deep Learning and the Game of Go" and it is based in the Tic-Tac-Toe implementation.

* GitHub: https://github.com/maxpumperla/deep_learning_and_the_game_of_go/ 
* Book: https://www.amazon.ca/Deep-Learning-Game-Max-Pumperla/dp/1617295329

It is possible to execute the project from Jupyter Notebook or from Python classes:
* Notebook: https://github.com/ravasconcelos/Hexapawn/tree/master/notebook
* Classes: https://github.com/ravasconcelos/Hexapawn/tree/master/python_classes/hex

## How to Play:

1. The board will be printed as below:

![](https://raw.githubusercontent.com/ravasconcelos/Hexapawn/master/img/board.png)
2. The 'O's are the Bot pawns
3. The 'X's are your pawns
4. In order to move your pawn, you have to enter a command stating the square which the pawn currently is and the which square it will move to. For example:

![](https://raw.githubusercontent.com/ravasconcelos/Hexapawn/master/img/moving.png)

The command B3B3 moved the X from center botton to center middle 

5. Remember that the pawn may be moved one square forward, or it may capture a pawn one square diagonally ahead of it. A pawn may not be moved forward if there is a pawn in the next square.
6. A player loses if he/she has no legal moves or the other player reaches the end of the board with a pawn.

Full game example:

![](https://raw.githubusercontent.com/ravasconcelos/Hexapawn/master/img/full_game.png)
  

**Good luck and enjoy!**
