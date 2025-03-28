import time
from turtle import st
import numpy as np
from itertools import product
class BruteForceSolver:
    def __init__(self,sudokuGrid):
        self.grid = sudokuGrid.grid
        self.solutions_tried = 0

    def solve(self):

        return self.BruteForce(self.grid)

    def solveGraph(self):

        return self.BruteForceGraph(self.grid)

    def find_empty_cases(self,grid):
        empty_cases = []
        for row in range(9):
            for col in range(9):
                if grid[row, col] == 0:
                    
                    empty_cases.append((row,col))
        return empty_cases
    
    def is_valid_move(self, row, col, num):
        if num in self.grid[row]:
                return False

        if num in [self.grid[i][col] for i in range(9)]:
            return False

        start_row, start_col = (row // 3) * 3, (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False

        return True

    def BruteForce(self, grid):
        empty_cases = self.find_empty_cases(self.grid)

        if not empty_cases:  # If there are no empty cells, the grid is solved
            return True
        start_time = time.time()
        # Generate all possibilities for the empty cases
        for combinaison in product(range(1, 10), repeat=len(empty_cases)):
            elapsed_time = time.time() - start_time
            self.solutions_tried += 1
            print(f"\r {self.solutions_tried} {self.numberOfPossibilties()} {elapsed_time:6f}      {self.timeNeededToSolve()}",end="")
            # Try each possibility
            for (row, col), chiffre in zip(empty_cases, combinaison):
                if not self.is_valid_move(row, col, chiffre):
                    break
                grid[row, col] = chiffre

            else:
                return True
            for row, col in empty_cases:
                grid[row , col] = 0

        return False

    def BruteForceGraph(self, grid):
        empty_cases = self.find_empty_cases(self.grid)

        if not empty_cases:  # If there are no empty cells, the grid is solved
            return True
        start_time = time.time()
        # Generate all possibilities for the empty cases
        for combinaison in product(range(1, 10), repeat=len(empty_cases)):
            elapsed_time = time.time() - start_time
            self.solutions_tried += 1
            print(f"\r {self.solutions_tried} {self.numberOfPossibilties()} {elapsed_time:6f}      {self.timeNeededToSolve()}",end="")
            
            # Try each possibility
            for (row, col), chiffre in zip(empty_cases, combinaison):
                if not self.is_valid_move(row, col, chiffre):
                    break
                grid[row, col] = chiffre
            else:
                return True
            for row, col in empty_cases:
                grid[row, col] = 0

        return False

    def numberOfPossibilties(self):
        numberOfEmptyCases = len(self.find_empty_cases(self.grid))
        return 9**(81-numberOfEmptyCases)

    def timeNeededToSolve(self):
        return (self.numberOfPossibilties() * 10**-6)//31536000

if __name__ == "__main__":
    pass