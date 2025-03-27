from models.sudoku import SudokuGrid
from solvers.backtracking import BacktrakingceSolver

def main():
    sudoku = SudokuGrid()
    # Demander d'abord le niveau et charger la grille
    file_path = sudoku.user_choice()
    if file_path is None:  # Si l'utilisateur a choisi de quitter
        return
    
    sudoku.load_grid(file_path)  # Charger la grille
    
    # Ensuite seulement demander le solveur
    solver_choice = sudoku.choose_solver()

    if solver_choice == "A":
        print("Force brut sélectionné, mais non implémenté dans cet exemple.")
        sudoku.print_simple_grid()  # Afficher la grille de base
        
    elif solver_choice == "B":
        solver = BacktrakingceSolver(sudoku)
        if solver.solve():
            print("Sudoku résolu en utilisant le backtracking :")
            sudoku.print_simple_grid()
        else:
            print("Aucune solution trouvée.")
    else:
        print("Choix de solveur invalide.")
if __name__ == "__main__":
    main()
