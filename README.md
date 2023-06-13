# SudokuSolver
This is a program that solves sudoku puzzles using reccursion and backtracking.

## How it works
The unsolved puzzle is to be entered row wise with 0's representing empty spaces. The program verifies that the entered values are valid and then solves the puzzle. 

It is a 9x9 sudoku puzzle, which is represented as a list of lists. The code contains multiple user defined functions that check if the values entered are valid and then solves the puzzle by putting the most appropriate numbers from 1 to 9 in each empty cell(0) until no valid value can be entered, then it backtracks to the previous empty cell and changes its value to the next most feasible value. 

## How to run
    python sudoku.py
