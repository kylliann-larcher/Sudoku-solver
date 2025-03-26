from models.sudoku import SudokuGrid
from solvers.backtracking import BacktrakingceSolver

def main():
    sudoku = SudokuGrid()
    solver_choice = sudoku.choose_solver()

    if solver_choice == "A":
        # Ajoutez ici l'appel au solveur
        print("Force brut sélectionné, mais non implémenté dans cet exemple.")
        
        
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
