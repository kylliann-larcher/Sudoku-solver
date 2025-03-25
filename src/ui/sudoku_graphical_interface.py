import pygame
import sys
from sodoku_terminal import SudokuGrid
from algo import Algo

pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)
RED = (255, 0, 0)

# Define dimensions
WIDTH, HEIGHT = 800, 700  
GRID_SIZE = 9
GRID_WIDTH = 450
GRID_HEIGHT = 450
CELL_SIZE = GRID_WIDTH // GRID_SIZE
MARGIN_TOP = 200  
MARGIN_LEFT = (WIDTH - GRID_WIDTH) // 2

# Fonts
font_small = pygame.font.SysFont('Arial', 20)
font_medium = pygame.font.SysFont('Arial', 30)
font_large = pygame.font.SysFont('Arial', 40)

# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NEURALGRID")

# Game states
STATE_MENU = 0
STATE_LEVEL = 1
STATE_ALGO = 2
STATE_GRID = 3

class GameState:
    def __init__(self):
        self.state = STATE_MENU
        self.grid = None
        self.selected_algo = None
        self.selected_level = None
        self.sudoku = SudokuGrid()
        self.algo = Algo()

    def draw_menu(self):
        window.fill(WHITE)
        
        # Title
        title = font_large.render("NEURALGRID", True, BLACK)
        window.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))
        
        # Menu box
        menu_rect = pygame.Rect(WIDTH // 4, 150, WIDTH // 2, 400)
        pygame.draw.rect(window, LIGHT_BLUE, menu_rect, border_radius=10)
        pygame.draw.rect(window, BLACK, menu_rect, 2, border_radius=10)
        
        # Menu options
        options = [
            ("1. Choisir un niveau", 200),
            ("2. Choisir un algorithme", 250),
            ("3. Afficher la grille", 300),
            ("4. Quitter", 350)
        ]
        
        for text, y_pos in options:
            option = font_medium.render(text, True, BLACK)
            window.blit(option, (WIDTH // 2 - option.get_width() // 2, y_pos))
        
        pygame.display.update()

    def draw_level_menu(self):
        window.fill(WHITE)
        
        # Title
        title = font_large.render("MENU DES NIVEAUX", True, BLACK)
        window.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))
        
        # Menu box
        menu_rect = pygame.Rect(WIDTH // 4, 150, WIDTH // 2, 400)
        pygame.draw.rect(window, LIGHT_BLUE, menu_rect, border_radius=10)
        pygame.draw.rect(window, BLACK, menu_rect, 2, border_radius=10)
        
        # Level options
        levels = [
            "1. Niveau Facile",
            "2. Niveau Intermédiaire",
            "3. Niveau Difficile",
            "4. Niveau Expert",
            "5. Niveau Légendaire",
            "0. Retour"
        ]
        
        for i, level in enumerate(levels):
            option = font_medium.render(level, True, BLACK)
            window.blit(option, (WIDTH // 2 - option.get_width() // 2, 200 + i * 50))
        
        pygame.display.update()

    def draw_algo_menu(self):
        window.fill(WHITE)
        
        # Title
        title = font_large.render("CHOIX D'ALGORITHME", True, BLACK)
        window.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))
        
        # Menu box
        menu_rect = pygame.Rect(WIDTH // 4, 150, WIDTH // 2, 300)
        pygame.draw.rect(window, LIGHT_BLUE, menu_rect, border_radius=10)
        pygame.draw.rect(window, BLACK, menu_rect, 2, border_radius=10)
        
        # Algorithm options
        algos = [
            "A. Algorithme Force Brute",
            "B. Algorithme Backtracking",
            "0. Retour"
        ]
        
        for i, algo in enumerate(algos):
            option = font_medium.render(algo, True, BLACK)
            window.blit(option, (WIDTH // 2 - option.get_width() // 2, 200 + i * 50))
        
        pygame.display.update()

    def draw_grid(self):
        if self.grid is None:
            self.state = STATE_MENU
            return
            
        window.fill(WHITE)
        
        # Title
        title = font_large.render("GRILLE DE SUDOKU", True, BLACK)
        window.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))
        
        # Draw cells
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                rect = pygame.Rect(
                    MARGIN_LEFT + j * CELL_SIZE, 
                    MARGIN_TOP + i * CELL_SIZE, 
                    CELL_SIZE, 
                    CELL_SIZE
                )
                pygame.draw.rect(window, WHITE, rect)
                pygame.draw.rect(window, GRAY, rect, 1)
        
        # Draw thick lines for 3x3 subgrids
        for i in range(0, GRID_SIZE + 1, 3):
            pygame.draw.line(
                window, BLACK, 
                (MARGIN_LEFT + i * CELL_SIZE, MARGIN_TOP), 
                (MARGIN_LEFT + i * CELL_SIZE, MARGIN_TOP + GRID_HEIGHT), 
                3
            )
            pygame.draw.line(
                window, BLACK, 
                (MARGIN_LEFT, MARGIN_TOP + i * CELL_SIZE), 
                (MARGIN_LEFT + GRID_WIDTH, MARGIN_TOP + i * CELL_SIZE), 
                3
            )
        
        # Draw numbers
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if i < len(self.grid) and j < len(self.grid[i]) and self.grid[i][j] not in ('0', '_'):
                    x = MARGIN_LEFT + j * CELL_SIZE + CELL_SIZE // 2
                    y = MARGIN_TOP + i * CELL_SIZE + CELL_SIZE // 2
                    text = font_medium.render(str(self.grid[i][j]), True, BLACK)
                    text_rect = text.get_rect(center=(x, y))
                    window.blit(text, text_rect)
        
        # Back button
        back_rect = pygame.Rect(50, 50, 100, 40)
        pygame.draw.rect(window, RED, back_rect, border_radius=5)
        pygame.draw.rect(window, BLACK, back_rect, 2, border_radius=5)
        back_text = font_small.render("Retour", True, WHITE)
        window.blit(back_text, (back_rect.centerx - back_text.get_width() // 2, 
                              back_rect.centery - back_text.get_height() // 2))
        
        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                if self.state == STATE_MENU:
                    self.handle_menu_click(mouse_pos)
                elif self.state == STATE_LEVEL:
                    self.handle_level_click(mouse_pos)
                elif self.state == STATE_ALGO:
                    self.handle_algo_click(mouse_pos)
                elif self.state == STATE_GRID:
                    self.handle_grid_click(mouse_pos)

    def handle_menu_click(self, pos):
        x, y = pos
        
        # Check if click is in menu area
        if WIDTH // 4 <= x <= 3 * WIDTH // 4:
            if 200 <= y <= 240:
                self.state = STATE_LEVEL
            elif 250 <= y <= 290:
                self.state = STATE_ALGO
            elif 300 <= y <= 340:
                if self.selected_level:
                    self.grid = self.sudoku.load_grid(self.selected_level)
                    self.state = STATE_GRID
            elif 350 <= y <= 390:
                pygame.quit()
                sys.exit()

    def handle_level_click(self, pos):
        x, y = pos
        
        # Check if click is in menu area
        if WIDTH // 4 <= x <= 3 * WIDTH // 4:
            if 200 <= y <= 240:
                self.selected_level = 'C:/Users/Windows/Desktop/projets/1a/sodoku/Sudoku-solver/grids/sudoku.txt'
                self.state = STATE_MENU
            elif 250 <= y <= 290:
                self.selected_level = 'C:/Users/Windows/Desktop/projets/1a/sodoku/Sudoku-solver/grids/sudoku2.txt'
                self.state = STATE_MENU
            elif 300 <= y <= 340:
                self.selected_level = 'C:/Users/Windows/Desktop/projets/1a/sodoku/Sudoku-solver/grids/sudoku3.txt'
                self.state = STATE_MENU
            elif 350 <= y <= 390:
                self.selected_level = 'C:/Users/Windows/Desktop/projets/1a/sodoku/Sudoku-solver/grids/sudoku4.txt'
                self.state = STATE_MENU
            elif 400 <= y <= 440:
                self.selected_level = 'C:/Users/Windows/Desktop/projets/1a/sodoku/Sudoku-solver/grids/evilsudoku.txt'
                self.state = STATE_MENU
            elif 450 <= y <= 490:
                self.state = STATE_MENU

    def handle_algo_click(self, pos):
        x, y = pos
        
        # Check if click is in menu area
        if WIDTH // 4 <= x <= 3 * WIDTH // 4:
            if 200 <= y <= 240:
                self.selected_algo = "A"
                self.state = STATE_MENU
            elif 250 <= y <= 290:
                self.selected_algo = "B"
                self.state = STATE_MENU
            elif 300 <= y <= 340:
                self.state = STATE_MENU

    def handle_grid_click(self, pos):
        x, y = pos
        
        # Check if back button is clicked
        if 50 <= x <= 150 and 50 <= y <= 90:
            self.state = STATE_MENU

    def run(self):
        while True:
            self.handle_events()
            
            if self.state == STATE_MENU:
                self.draw_menu()
            elif self.state == STATE_LEVEL:
                self.draw_level_menu()
            elif self.state == STATE_ALGO:
                self.draw_algo_menu()
            elif self.state == STATE_GRID:
                self.draw_grid()

# Run the game
if __name__ == "__main__":
    game = GameState()
    game.run()