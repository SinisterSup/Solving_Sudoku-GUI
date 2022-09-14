# Solving_Sudoku-GUI
![PyGame][1] ![Python][2] ![License][3]

#### A Sudoku game with Solver Backtracking algorithm developed using Python and PyGame 
Every time the program is executed, a random, solvable board is created and the user can attempt to solve it by clicking on the cells.     
Entering a number into a cell will be entered as a tentative value.      
Once the the user is sure that the inputted number is the correct entry, pressing the enter key will attempt to input the number onto the board.      
Correct answers will be permanently displayed while incorrect answers will be removed.      
Likewise, values can be removed by pressing on the backspace or delete keys.     

If at any point the player decides to solve the board, the spacebar can be pressed.     
This will commence a visual that demonstrates how the backtracking algorithm
is being applied in order to solve the board.

## Controls
| Keys              | Actions                                                        |
|-------------------|----------------------------------------------------------------|
| `Left Click`      |Enters a value into that cell                                   |
| `Backspace/Delete`| Deletes the number in that cell                                |
| `Space`           | Solves the board via a backtracking algorithm visualizer       |
| `h`               | Gives user a hint. Displays a random correct value on the board|

## Run in Gitpod
You can also alternatively run Sudoku-GUI-Solver in Gitpod, a free online dev environment for GitHub:
