class SudokuGrid:
    def __init__(self, grid=None):
        if grid is None:
            self.grid = [[0 for _ in range(9)] for _ in range(9)]
        else:
            self.grid = grid

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()

        self.grid = [
            [int(char) if char.isdigit() else 0 for char in line.strip()]
            for line in lines
        ]

    def display(self):
        for i, row in enumerate(self.grid):
            if i % 3 == 0 and i != 0:
                print("-" * 21)  # Horizontal separator

            for j, num in enumerate(row):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")  # Vertical separator
                print(num if num != 0 else ".", end=" ")  # Replace 0 with '.'
            print()

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



