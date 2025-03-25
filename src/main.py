from models.sudoku import SudokuGrid
from solvers.brute_force import BruteForceSolver

# Load Sudoku Grid
sudoku = SudokuGrid()
sudoku.load_from_file("tests/sudoku.txt")
sudoku.display()
print(sudoku.is_valid_move(0, 1, 5))  # Test move validity
# Solve using Brute Force
solver = BruteForceSolver(sudoku)
if solver.solve():
    print("Sudoku solved using brute force:")
    sudoku.display()
else:
    print("No solution found.")
