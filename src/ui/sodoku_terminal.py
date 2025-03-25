import numpy as np

class SudokuGrid:
    
    def __init__(self, file_path=None):
        
        self.file_path = file_path
        self.grid = None  # Initialisé à None jusqu'au chargement
        if file_path:
            self.load_grid(file_path)

    def choose_level(self):
    
        while True:
            print("\n" + "═" * 32)
            print(" " * 9 + "MENU DES NIVEAUX")
            print("═" * 32)
            print("╔══════════════════════════════╗")
            print("║  1. Niveau Facile            ║")
            print("║  2. Niveau Intermédiaire     ║")
            print("║  3. Niveau Difficile         ║")
            print("║  4. Niveau Expert            ║")
            print("║  5. Niveau Légendaire        ║")
            print("║                              ║")
            print("║  0. Quitter                  ║")
            print("╚══════════════════════════════╝")
            print("═" * 32)
            
            choice = input("Veuillez choisir un niveau (0-5) : ").strip()

            match choice: 
                case "1": 
                    print("\n>>>>>>>>>>>>> NIVEAU FACILE <<<<<<<<<<<<<")
                    return 'C:/Users/Windows/Desktop/projets/1a/sodoku/Sudoku-solver/grids/sudoku.txt'
                case "2": 
                    print("\n>>>>>>>>>> NIVEAU INTERMEDIAIRE <<<<<<<<<<")
                    return 'C:/Users/Windows/Desktop/projets/1a/sodoku/Sudoku-solver/grids/sudoku2.txt'
                case "3": 
                    print("\n>>>>>>>>>>>>> NIVEAU DIFFICILE <<<<<<<<<<<<")
                    return 'C:/Users/Windows/Desktop/projets/1a/sodoku/Sudoku-solver/grids/sudoku3.txt'
                case "4": 
                    print("\n>>>>>>>>>>>>> NIVEAU EXPERT <<<<<<<<<<<<<<")
                    return 'C:/Users/Windows/Desktop/projets/1a/sodoku/Sudoku-solver/grids/sudoku4.txt'
                case "5": 
                    print("\n>>>>>>>>>> NIVEAU LEGENDAIRE <<<<<<<<<<<<")
                    return 'C:/Users/Windows/Desktop/projets/1a/sodoku/Sudoku-solver/grids/evilsudoku.txt'
                case "0":
                    print("\n" + "═" * 35)
                    print("   Merci d'avoir joué ! Au revoir   ")
                    print("═" * 35 + "\n")
                    return None
                case _:
                    print("\n⚠ Choix invalide! Veuillez entrer un nombre entre 0 et 5.")

    def load_grid(self, file_path=None):

        if not file_path:
            file_path = self.choose_level()
            if not file_path:  # Si l'utilisateur a choisi de quitter
                return None

        self.file_path = file_path
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = [line.strip() for line in f if line.strip()]
            
            # Conversion en tableau numpy 2D (9x9)
            self.grid = np.array([list(line) for line in lines])
            return self.grid
            
        except FileNotFoundError:
            print(f"Erreur: Fichier {file_path} introuvable")
            return None

    def print_simple_grid(self):

        if self.grid is None:
            print("Aucune grille chargée.")
            return
        
        # En-tête avec lettres pour les colonnes
        print("    A   B   C    D   E   F  G   H   I")
        print("  ╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗")
    
        for i, row in enumerate(self.grid):
            # Numéro de ligne à gauche
            print(f"{i+1} ║", end="")
            
            for j, num in enumerate(row):
                # Contenu de la case (centre)
                content = num if num not in ('0', '_') else ' '
                print(f" {content} ", end="")
                
                # Séparateurs verticaux
                if j in (2, 5):
                    print("║", end="")
                elif j < 8:
                    print("│", end="")
            
            # Numéro de ligne à droite
            print(f"║ {i+1}")
            
            # Séparateurs horizontaux
            if i in (2, 5):
                print("  ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣")
            elif i < 8:
                print("  ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")
        
        # Pied de grille
        print("  ╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")

# Exemple d'utilisation
if __name__ == "__main__":

    sudoku = SudokuGrid()
    grid = sudoku.load_grid()

    display_grid=sudoku.print_simple_grid()
    print(display_grid)

