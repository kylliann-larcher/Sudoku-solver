import time
from tracemalloc import start
from models.sudoku import SudokuGrid
from solvers.backtracking import BacktrakingceSolver
from solvers.brute_force import BruteForceSolver

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
        solver = BruteForceSolver(sudoku)
        if solver.solve():
            sudoku.print_simple_grid()  # Afficher la grille de base
            print("INCROYABLE LE SUDOKU A ETE RESOLU !!!")
    elif solver_choice == "B":
        solver = BacktrakingceSolver(sudoku)
        start_time = time.time()
        if solver.solve():
            print("Sudoku résolu en utilisant le backtracking :")
            sudoku.print_simple_grid()
            elapsed_time = time.time() - start_time
            print(f"{elapsed_time*1000} ms pour finir la grille")
        else:
            print("Aucune solution trouvée.")
    else:
        print("Choix de solveur invalide.")
if __name__ == "__main__":
    main()