class BruteForceSolver:
    def __init__(self, sudoku_grid):
        self.grid = sudoku_grid.grid  # Work directly on the SudokuGrid object's grid

    def solve(self):
        return self._brute_force_helper(0, 0)

    def _brute_force_helper(self, row, col):
        #Recursive function to brute force the solution.
        #:param row: Current row index.
        #:param col: Current column index.
        #:return: True if solved, False otherwise.
        
        if row == 9:  # If we reach row 9, the grid is solved
            return True

        if col == 9:  # If we reach the end of a row, go to the next row
            return self._brute_force_helper(row + 1, 0)

        if self.grid[row][col] != 0:  # Skip already filled cells
            return self._brute_force_helper(row, col + 1)

        for num in range(1, 10):  # Try numbers from 1 to 9
            if self._is_valid_move(row, col, num):
                self.grid[row][col] = num  # Place the number

                if self._brute_force_helper(row, col + 1):  # Recursively solve the next cell
                    return True

                self.grid[row][col] = 0  # Undo the move (backtrack)

        return False  # No solution found from this state

    def _is_valid_move(self, row, col, num):
        #Checks if a number can be placed in a specific cell (same logic as SudokuGrid).
        #:param row: Row index (0-8).
        #:param col: Column index (0-8).
        #:param num: Number to check (1-9).
        #:return: True if valid, False otherwise.
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False

        start_row, start_col = (row // 3) * 3, (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False

        return True
