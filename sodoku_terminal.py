def print_grid_1(grid):
   

    print("    A   B   C   D   E   F   G   H   I")
    print("  ╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗")
    
    # Parcours chaque ligne (i = 0 à 8)
for i in range(9):
    # Affiche le numéro de ligne (1-9) et la bordure gauche
    print(f"{i+1} ║", end="")
    
    # Parcours chaque colonne (j = 0 à 8)
    for j in range(9):
        # Récupère la valeur de la case
        num = grid[i][j]
        # Affiche '.' si case vide, sinon le chiffre
        content = '.' if num == '_' else str(num)
        print(f" {content} ", end="")
        
        # Gestion des séparateurs verticaux :
        if j in (2, 5):  # Double barre après les colonnes 2 et 5 (bordures de bloc)
            print("║", end="")
        elif j != 8:     # Simple barre entre les colonnes
            print("│", end="")
    
    # Barre verticale de fin de ligne
    print("║")
        
    if i in (2, 5):
        print("  ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣")
    elif i != 8:
        print("  ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")
    
    print("  ╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")



grid_example = [
    [5, 3, '_', '_', 7, '_', '_', '_', '_'],
    [6, '_', '_', 1, 9, 5, '_', '_', '_'],
    ['_', 9, 8, '_', '_', '_', '_', 6, '_'],
    [8, '_', '_', '_', 6, '_', '_', '_', 3],
    [4, '_', '_', 8, '_', 3, '_', '_', 1],
    [7, '_', '_', '_', 2, '_', '_', '_', 6],
    ['_', 6, '_', '_', '_', '_', 2, 8, '_'],
    ['_', '_', '_', 4, 1, 9, '_', '_', 5],
    ['_', '_', '_', '_', 8, '_', '_', 7, 9]
]

print_grid_1(grid_example)

grid_1 = [
    [7, 2, 9, '_', '_', '_', 3, '_', '_'],
    ['_', '_', 1, '_', 6, '_', 8, '_', '_'],
    ['_', '_', '_', '_', 4, '_', '_', 6, '_'],
    [9, 6, '_', '_', '_', 4, 1, '_', 8],
    ['_', 4, 8, 7, '_', 5, '_', 9, 6],
    ['_', '_', 5, 6, '_', 8, '_', '_', 3],
    ['_', '_', '_', 4, '_', 2, '_', 1, '_'],
    [8, 5, '_', '_', 6, '_', 3, 2, 7],
    [1, '_', '_', 8, 5, '_', '_', '_', '_']
]

print("Sudoku:")
print_grid_1(grid_1)