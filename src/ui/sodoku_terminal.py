import numpy as np

def load_grid(file_path):
    """Charge la grille Sudoku en structure 3D [[[ligne complète]]]"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    
    # Conversion en structure 3D [[[ligne1], [ligne2], ..., [ligne9]]]
    grid = np.array([
        [list(line) for line in lines]
    ])
    
    return grid

def print_simple_grid(grid):
    """Affiche la grille Sudoku avec formatage"""
    # Convertit la structure 3D en 2D pour l'affichage
    display_grid = grid.reshape(9, 9)
    
    # Affichage formaté
    print("+-------+-------+-------+")
    for i, row in enumerate(display_grid):
        print("|", end=" ")
        for j, num in enumerate(row):
            print(num if num != '_' else '.', end=" ")
            if j in (2, 5):
                print("|", end=" ")
        print("|")
        if i in (2, 5):
            print("+-------+-------+-------+")
    print("+-------+-------+-------+")

# Exemple d'utilisation
grid = load_grid('grids/sudoku.txt')
print("Structure 3D [[[lignes]]]:\n", grid)
print("\nAffichage formaté:")
print_simple_grid(grid)
