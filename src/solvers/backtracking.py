from ..models.sudoku import SudokuGrid

class SudokuSolver:
    def __init__(self,sudokuGrid):
        self.grid = sudokuGrid

    def solving(self):
            
    def backtrack(self):



if __name__ == "__main__":
    sudoku = SudokuGrid()
    sudoku.load_from_file("tests/sudoku.txt")
    sudoku.display()