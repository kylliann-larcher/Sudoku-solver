import numpy as np

class SudokuGrid:
    
    def __init__(self, file_path=None):
        
        self.file_path = file_path
        self.grid = None  # Initialisé à None jusqu'au chargement
        if file_path:
            self.load_grid(file_path)

    def choose_level(self):
        """Affiche le menu des niveaux et retourne le fichier choisi"""
        while True:
            print("""
            === MENU DES NIVEAUX ===
            1. Niveau Facile
            2. Niveau Intermédiaire
            3. Niveau Difficile
            4. Niveau Expert
            5. Niveau Légendaire
            0. Quitter
            """)
            
            choix = input("Veuillez choisir un niveau (0-5) : ").strip()

            match choix: 
                case "1": 
                    return 'C:/Users/Windows/Desktop/projets/1a/sodoku/Sudoku-solver/grids/sudoku.txt'
                case "2": 
                    return 'C:/Users/Windows/Desktop/projets/1a/sodoku/Sudoku-solver/grids/sudoku2.txt'
                case "3": 
                    return 'C:/Users/Windows/Desktop/projets/1a/sodoku/Sudoku-solver/grids/sudoku3.txt'
                case "4": 
                    return 'C:/Users/Windows/Desktop/projets/1a/sodoku/Sudoku-solver/grids/sudoku4.txt'
                case "5": 
                    return 'C:/Users/Windows/Desktop/projets/1a/sodoku/Sudoku-solver/grids/evilsudoku.txt'
                case "0":
                    print("Au revoir")
                    return None
                case _:
                    print("Choix invalide, veuillez réessayer.")


    def load_grid(self, file_path=None):
        """Charge la grille depuis un fichier"""
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
        
        print("+-------+-------+-------+")
        for i, row in enumerate(self.grid):
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
if __name__ == "__main__":
    sudoku = SudokuGrid()
    sudoku.load_grid()  # Demande le niveau interactivement
    if sudoku.grid is not None:
        sudoku.print_simple_grid()
