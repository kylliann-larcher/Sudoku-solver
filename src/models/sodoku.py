class SudokuGrid:
    def __init__(self, grid=None):
        """
        Initializes the Sudoku grid.
        :param grid: A 9x9 list of lists representing the Sudoku puzzle.
        """
        if grid is None:
            self.grid = [[0 for _ in range(9)] for _ in range(9)]
        else:
            self.grid = grid

    def load_from_file(self, filename):
        """
        Loads a Sudoku grid from a text file.
        :param filename: Name of the file containing the grid.
        """
        with open(filename, 'r') as file:
            lines = file.readlines()

        self.grid = [
            [int(char) if char.isdigit() else 0 for char in line.strip()]
            for line in lines
        ]

    def display(self):
        """
        Prints the Sudoku grid in a readable format.
        """
        for i, row in enumerate(self.grid):
            if i % 3 == 0 and i != 0:
                print("-" * 21)  # Horizontal separator

            for j, num in enumerate(row):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")  # Vertical separator
                print(num if num != 0 else ".", end=" ")  # Replace 0 with '.'
            print()

    def is_valid_move(self, row, col, num):
        """
        Checks if a number can be placed in a specific cell.
        :param row: Row index (0-8)
        :param col: Column index (0-8)
        :param num: Number to check (1-9)
        :return: True if valid, False otherwise.
        """
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

sudoku = SudokuGrid()
sudoku.load_from_file("tests/sudoku.txt")
sudoku.display()
print(sudoku.is_valid_move(0, 1, 5))  # Test move validity
