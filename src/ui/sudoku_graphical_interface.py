import pygame
import sys
import numpy as np
from pygame.locals import *
import os
import time

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.solvers.brute_force import BruteForceSolver
from src.models.sudoku import SudokuGrid
from src.solvers.backtracking import BacktrakingceSolver

pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (160, 160, 170)
PRIMARY_COLOR = (72, 172, 239)
SECONDARY_COLOR = (255, 94, 87)
HIGHLIGHT_COLOR = (255, 216, 77)
SHADOW_COLOR = (100, 110, 130)
BACKGROUND_COLOR = (30, 40, 60)

# Dimensions
WIDTH, HEIGHT = 600, 700
GRID_SIZE = 9
GRID_WIDTH = 450
GRID_HEIGHT = 450
CELL_SIZE = GRID_WIDTH // GRID_SIZE
MARGIN_TOP = (HEIGHT - GRID_HEIGHT) // 2
MARGIN_LEFT = (WIDTH - GRID_WIDTH) // 2

# Window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NEURALGRID")


# Chemins possibles pour les fichiers de police
current_dir = os.path.dirname(os.path.abspath(__file__))
font_paths = [
    os.path.join(current_dir, 'fonts', 'Poppins-Regular.ttf'),
    os.path.join(current_dir, '..', 'ui', 'fonts', 'Poppins-Regular.ttf'),
    'fonts/Poppins-Regular.ttf'
]

try:
    # Trouver le premier chemin de police qui existe
    font_path = next(path for path in font_paths if os.path.exists(path))
    font = pygame.font.Font(font_path, 30)
    
    # Faire de même pour les autres polices
    title_font_path = font_path.replace('Poppins-Regular.ttf', 'Poppins-Bold.ttf')
    button_font_path = title_font_path
    
    title_font = pygame.font.Font(title_font_path, 40)
    button_font = pygame.font.Font(button_font_path, 24)

except (FileNotFoundError, StopIteration):
    # Fallback si Poppins n'est pas trouvée
    font = pygame.font.SysFont('Arial', 30)
    title_font = pygame.font.SysFont('Arial', 40, bold=True)
    button_font = pygame.font.SysFont('Arial', 24, bold=True)

def draw_grid():
    # Grid background
    grid_rect = pygame.Rect(MARGIN_LEFT, MARGIN_TOP, GRID_WIDTH, GRID_HEIGHT)
    pygame.draw.rect(window, WHITE, grid_rect, border_radius=15)

    # Cells
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            rect = pygame.Rect(
                MARGIN_LEFT + i * CELL_SIZE,
                MARGIN_TOP + j * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )
            pygame.draw.rect(window, WHITE, rect)
            pygame.draw.rect(window, GRAY, rect, 1)

    # Sub-grids
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

def draw_numbers(grid, solved=False, original_grid=None):
    if grid is None:
        return

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 0:
                x = MARGIN_LEFT + j * CELL_SIZE + CELL_SIZE // 2
                y = MARGIN_TOP + i * CELL_SIZE + CELL_SIZE // 2

                # Déterminer la couleur
                if solved and original_grid and original_grid[i][j] == 0:
                    color = (0, 180, 0)  # Vert pour les nombres résolus
                    # Fond légèrement coloré
                    cell_rect = pygame.Rect(
                        MARGIN_LEFT + j * CELL_SIZE + 1,
                        MARGIN_TOP + i * CELL_SIZE + 1,
                        CELL_SIZE - 2,
                        CELL_SIZE - 2
                    )
                    pygame.draw.rect(window, (230, 255, 230), cell_rect)
                else:
                    color = BLACK  # Noir pour les nombres initiaux

                text = font.render(str(grid[i][j]), True, color)
                text_rect = text.get_rect(center=(x, y))
                window.blit(text, text_rect)

def draw_menu_algo():
    title_menu = title_font.render("NEURALGRID - ALGORITHMS", True, WHITE)
    window.blit(title_menu, (WIDTH // 2 - title_menu.get_width() // 2, 30))

    choose_algo = font.render("Choose an Algorithm", True, WHITE)
    window.blit(choose_algo, (WIDTH // 2 - choose_algo.get_width() // 2, 140))

    buttons = []
    algo_button = [
        ("Brute Force Algorithm", 1),
        ("Backtracking Algorithm", 2),
    ]

    button_width = 400
    button_height = 50
    spacing = 50
    total_height = len(algo_button) * (button_height + spacing) - spacing
    start_y = (HEIGHT - total_height) // 2

    for i, (text, algo_id) in enumerate(algo_button):
        button_y = start_y + i * (button_height + spacing)

        button_rect = pygame.Rect(
            WIDTH // 2 - button_width // 2,
            button_y,
            button_width,
            button_height
        )

        color = PRIMARY_COLOR if algo_id != 0 else SECONDARY_COLOR

        pygame.draw.rect(window, color, button_rect, border_radius=10)
        pygame.draw.rect(window, SHADOW_COLOR, button_rect, 3, border_radius=10)

        text_surf = button_font.render(text, True, WHITE)
        text_rect = text_surf.get_rect(center=button_rect.center)
        window.blit(text_surf, text_rect)

        buttons.append((algo_id, button_rect))

    return buttons

def draw_level_buttons():
    title = title_font.render("Choose a Level", True, WHITE)
    window.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))

    levels = [
        ("Easy", 1),
        ("Intermediate", 2),
        ("Difficult", 3),
        ("Expert", 4),
        ("Legendary", 5)
    ]

    buttons = []
    button_width = 300
    button_height = 40
    spacing = 30
    total_height = len(levels) * (button_height + spacing) - spacing
    start_y = (HEIGHT - total_height) // 2

    for i, (text, level_id) in enumerate(levels):
        button_y = start_y + i * (button_height + spacing)
        button_rect = pygame.Rect(
            WIDTH // 2 - button_width // 2,
            button_y,
            button_width,
            button_height
        )

        pygame.draw.rect(window, SECONDARY_COLOR, button_rect, border_radius=10)
        pygame.draw.rect(window, SHADOW_COLOR, button_rect, 3, border_radius=10)

        text_surf = button_font.render(text, True, WHITE)
        text_rect = text_surf.get_rect(center=button_rect.center)
        window.blit(text_surf, text_rect)

        buttons.append((level_id, button_rect))

    return buttons
def main():
    sudoku = SudokuGrid()
    grid = None
    running = True
    show_grid = False
    show_algo_menu = True
    selected_algo = None
    level_buttons = []
    solved = False
    original_grid = None
    start_time = 0
    solving_time = 0
    is_solving = False

    level_files = {
        1: 'grids/sudoku.txt',
        2: 'grids/sudoku2.txt',
        3: 'grids/sudoku3.txt',
        4: 'grids/sudoku4.txt',
        5: 'grids/evilsudoku.txt'
    }

    while running:
        window.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == MOUSEBUTTONDOWN:
                if show_algo_menu:
                    algo_buttons = draw_menu_algo()
                    for algo_id, rect in algo_buttons:
                        if rect.collidepoint(event.pos):
                            selected_algo = algo_id
                            show_algo_menu = False
                            break

                elif not show_grid:
                    level_buttons = draw_level_buttons()
                    for level, rect in level_buttons:
                        if rect.collidepoint(event.pos):
                            file_path = level_files.get(level)
                            if file_path:
                                grid = sudoku.load_grid(file_path)
                                original_grid = [row[:] for row in grid]
                                show_grid = True
                                solved = False
                                is_solving = False
                                break

                else:
                    # Bouton Back
                    back_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 60, 200, 40)
                    if back_button.collidepoint(event.pos):
                        show_grid = False
                        grid = None
                        show_algo_menu = True
                        solved = False
                        is_solving = False

                    # Bouton Solve
                    solve_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 110, 200, 40)
                    if solve_button.collidepoint(event.pos) and selected_algo == 1 and not solved and not is_solving:
                        solver = BruteForceSolver(sudoku)
                        is_solving = True
                        # Solve the grid with graphical updates
                        while not solver.BruteForceGraph(grid, window,BACKGROUND_COLOR):
                            pygame.display.flip()

                        is_solving = False
                        solved = True
                        solving_time = time.time() - start_time  # Total solving time


                    if solve_button.collidepoint(event.pos) and selected_algo == 2 and not solved and not is_solving:
                        solver = BacktrakingceSolver(sudoku)
                        start_time = time.time_ns()
                        is_solving = True
                        if solver.solve():
                            solving_time = (time.time_ns() - start_time) / 1e6  # ms
                            grid = sudoku.grid
                            solved = True
                        is_solving = False

        if show_algo_menu:
            algo_buttons = draw_menu_algo()
        elif not show_grid:
            level_buttons = draw_level_buttons()
        else:
            # Affichage du titre
            title = title_font.render("Sudoku", True, WHITE)
            window.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))

            # Affichage de la grille
            draw_grid()
            draw_numbers(grid, solved, original_grid)

            # Bouton Back
            back_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 60, 200, 40)
            pygame.draw.rect(window, PRIMARY_COLOR, back_button, border_radius=10)
            back_text = button_font.render("Back", True, WHITE)
            window.blit(back_text, (back_button.centerx - back_text.get_width() // 2, 
                                  back_button.centery - back_text.get_height() // 2))
            

            if selected_algo == 1 and not solved and not is_solving:
                solve_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 110, 200, 40)
                pygame.draw.rect(window, SECONDARY_COLOR, solve_button, border_radius=10)
                solve_text = button_font.render("Solve", True, WHITE)
                window.blit(solve_text, (solve_button.centerx - solve_text.get_width() // 2,
                                        solve_button.centery - solve_text.get_height() // 2))
                

            # Bouton Solve (seulement pour l'algorithme 2 et si pas déjà résolu)
            if selected_algo == 2 and not solved and not is_solving:
                solve_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 110, 200, 40)
                pygame.draw.rect(window, SECONDARY_COLOR, solve_button, border_radius=10)
                solve_text = button_font.render("Solve", True, WHITE)
                window.blit(solve_text, (solve_button.centerx - solve_text.get_width() // 2,
                                       solve_button.centery - solve_text.get_height() // 2))
                


            # Affichage du chronomètre
            timer_y = MARGIN_TOP + GRID_HEIGHT + 10
            
            if is_solving:
                current_time = (time.time_ns() - start_time) / 1e6
                timer_text = font.render(f"Solving... {current_time:.1f} ms", True, WHITE)
                window.blit(timer_text, (WIDTH // 2 - timer_text.get_width() // 2, timer_y))
            elif solved:
                timer_text = font.render(f"Solved in {solving_time:.2f} ms", True, (0, 200, 0))
                window.blit(timer_text, (WIDTH // 2 - timer_text.get_width() // 2, timer_y))

        pygame.display.update()

    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    main()