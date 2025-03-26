import numpy as np

class SudokuGrid:
    
    def __init__(self):
        file_path = self.user_choice()
        if file_path:
            self.load_grid(file_path)  # Charge la grille
        else:
            print(" File not found ")

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
            return choice

    def user_choice(self):
        choice = self.choose_level()
        match choice: 
                case "1": 
                    print("\n>>>>>>>>>>>>> NIVEAU FACILE <<<<<<<<<<<<<")
                    return 'grids/sudoku.txt'
                case "2": 
                    print("\n>>>>>>>>>> NIVEAU INTERMEDIAIRE <<<<<<<<<<")
                    return 'grids/sudoku2.txt'
                case "3": 
                    print("\n>>>>>>>>>>>>> NIVEAU DIFFICILE <<<<<<<<<<<<")
                    return 'grids/sudoku3.txt'
                case "4": 
                    print("\n>>>>>>>>>>>>> NIVEAU EXPERT <<<<<<<<<<<<<<")
                    return 'grids/sudoku4.txt'
                case "5": 
                    print("\n>>>>>>>>>> NIVEAU LEGENDAIRE <<<<<<<<<<<<")
                    return 'grids/evilsudoku.txt'
                case "0":
                    print("\n" + "═" * 35)
                    print("   Merci d'avoir joué ! Au revoir   ")
                    print("═" * 35 + "\n")
                    return None
                case _:
                    print("\n⚠ Choix invalide! Veuillez entrer un nombre entre 0 et 5.")


    def load_grid(self, file_path):
        if not file_path:
            if not file_path:  # Si l'utilisateur a choisi de quitter
                return None
        self.file_path = file_path
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = [line.strip() for line in f if line.strip()]
            
            # Conversion en tableau numpy 2D (9x9)
            self.grid = np.array([[int(num) if num != '_' else 0 for num in line] for line in lines])
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
                content = num if num not in (0, '_') else ' '
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

    def choose_solver(self):
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


            choice_s = input("Veuillez choisir un algorithme (A ou B): ").strip().upper()

            match choice_s:
                case "A":
                    print("\n" + "═" * 32)
                    print("      FORCE BRUTE sélectionnée   ")
                    print("═" * 32)
                    self.print_simple_grid()
                    return "A"

                case "B":
                    print("\n" + "═" * 32)
                    print("      BACKTRACKING sélectionné    ")
                    print("═" * 32)
                    self.print_simple_grid()
                    return "B"

                case _:
                    print("\n⚠ Choix invalide! Veuillez choisir A ou B.")
                    print("═" * 32)
