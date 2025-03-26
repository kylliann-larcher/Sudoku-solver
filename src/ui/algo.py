from sodoku_terminal import SudokuGrid

class Algo:

    def __init__(self, choice=None):  # Corrected the constructor method
        self.choice = choice

    def choose_algo(self):
        while True:
            print("\n" + "═" * 32)
            print(" " * 5 + "NEURALGRID - ALGORITHMES")
            print("═" * 32)
            print("╔══════════════════════════════╗")
            print("║                              ║")
            print("║  A. Algorithme Force Brute   ║")
            print("║                              ║")
            print("║  B. Algorithme Backtracking  ║")
            print("║                              ║")
            print("╚══════════════════════════════╝")
            print("═" * 32)

            choice = input("Veuillez choisir un algorithme (A ou B): ").strip().upper()

            match choice:
                case "A":
                    print("\n" + "═" * 32)
                    print("      FORCE BRUTE sélectionnée   ")
                    print("═" * 32)
                    sudoku = SudokuGrid()
                    grid = sudoku.load_grid()
                    return sudoku.print_simple_grid()

                case "B":
                    print("\n" + "═" * 32)
                    print("      BACKTRACKING sélectionné    ")
                    print("═" * 32)
                    sudoku = SudokuGrid()
                    grid = sudoku.load_grid()
                    return sudoku.print_simple_grid()
                case _:
                    print("\n⚠ Choix invalide! Veuillez choisir A ou B.")
                    print("═" * 32)

# Initialize Algo with a default choice if needed
algo = Algo()

# Call the method to choose the algorithm
interface = algo.choose_algo()
print(interface)
