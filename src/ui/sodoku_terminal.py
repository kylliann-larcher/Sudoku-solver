def load_grid(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
        return [
            [
                [list(line[i:i+3]) for i in range(0, 9, 3)]
                for line in lines[bloc_i:bloc_i+3]
            ]
            for bloc_i in range(0, 9, 3)
        ]

def print_simple_grid(grid):

    # Convert load_grid() in flat grid
    flat_grid = []
    for big_block in grid:
        for line in zip(*big_block):
            flat_grid.append([cell for part in line for cell in part])
    
    # Display grid
    print("+-------+-------+-------+")
    for i, row in enumerate(flat_grid):
        print("|", end=" ")
        for j, num in enumerate(row):
            print(num if num != '_' else '.', end=" ")
            if j in (2, 5):
                print("|", end=" ")
        print("|")
        if i in (2, 5):
            print("+-------+-------+-------+")
    print("+-------+-------+-------+")



grid = load_grid('grids/sudoku.txt')
print(grid)
print_simple_grid(grid)
