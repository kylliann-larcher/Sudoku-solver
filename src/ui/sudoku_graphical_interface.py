import pygame
import sys
import numpy as np
from pygame.locals import *
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.models.sudoku import SudokuGrid
from src.solvers.backtracking import BacktrakingceSolver
from src.solvers.brute_force import BruteForceSolver

# Initialize Pygame
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
pygame.display.set_caption("Sudoku")

# Fonts
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
    window.blit(choose_algo, (WIDTH // 2 - choose_algo.get_width() // 2, 80))

    buttons = []
    algo_button = [
        ("Brute Force Algorithm", 1),
        ("Backtracking Algorithm", 2),
    ]

    button_width = 300
    button_height = 50
    spacing = 20
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
    button_width = 200
    button_height = 40
    spacing = 20
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
    original_grid = None  # Pour stocker la grille originale

    level_files = {
        1: 'grids/sudoku.txt',
        2: 'grids/sudoku2.txt',
        3: 'grids/sudoku3.txt',
        4: 'grids/sudoku4.txt',
        5: 'grids/evilsudoku.txt'
    }

    level_messages = {
        1: "EASY LEVEL",
        2: "INTERMEDIATE LEVEL",
        3: "DIFFICULT LEVEL",
        4: "EXPERT LEVEL",
        5: "LEGENDARY LEVEL"
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
                                original_grid = [row[:] for row in grid]  # Copie de la grille originale
                                show_grid = True
                                solved = False
                                break

                else:
                    # Bouton Back
                    back_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 60, 100, 40)
                    if back_button.collidepoint(event.pos):
                        show_grid = False
                        grid = None
                        show_algo_menu = True
                        selected_algo = None
                        solved = False

                    # Bouton Solve (uniquement pour backtracking)
                    if selected_algo == 2:
                        solve_button = pygame.Rect(WIDTH // 2 - 150, HEIGHT - 60, 100, 40)
                        if solve_button.collidepoint(event.pos) and not solved:
                            solver = BacktrakingceSolver(sudoku)
                            if solver.solve():
                                grid = sudoku.grid
                                solved = True
                            else:
                                print("Aucune solution trouvée")
                    
                    if selected_algo == 1:
                        solve_button = pygame.Rect(WIDTH // 2 - 150, HEIGHT - 60, 100, 40)
                        if solve_button.collidepoint(event.pos) and not solved:
                            solver = BruteForceSolver(sudoku)
                            if solver.solveGraph():
                                grid = sudoku.grid
                                solved = True
                            else:
                                print("Aucune solution trouvée")

        # Affichage
        if show_algo_menu:
            algo_buttons = draw_menu_algo()
        elif not show_grid:
            level_buttons = draw_level_buttons()
        else:
            # Titre
            title = title_font.render("Sudoku", True, WHITE)
            window.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))

            # Affichage de la grille
            draw_grid()
            draw_numbers(grid, solved, original_grid)

            # Bouton Back
            back_button = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 60, 100, 40)
            pygame.draw.rect(window, PRIMARY_COLOR, back_button, border_radius=10)
            pygame.draw.rect(window, SHADOW_COLOR, back_button, 3, border_radius=10)
            back_text = button_font.render("Back", True, WHITE)
            window.blit(back_text, (back_button.centerx - back_text.get_width() // 2, 
                                   back_button.centery - back_text.get_height() // 2))

            # Bouton Solve (uniquement pour backtracking et si pas déjà résolu)
            if selected_algo == 2 and not solved:
                solve_button = pygame.Rect(WIDTH // 2 - 150, HEIGHT - 60, 100, 40)
                pygame.draw.rect(window, SECONDARY_COLOR, solve_button, border_radius=10)
                pygame.draw.rect(window, SHADOW_COLOR, solve_button, 3, border_radius=10)
                solve_text = button_font.render("Solve", True, WHITE)
                window.blit(solve_text, (solve_button.centerx - solve_text.get_width() // 2,
                                        solve_button.centery - solve_text.get_height() // 2))

            if selected_algo == 1 and not solved:
                solve_button = pygame.Rect(WIDTH // 2 - 150, HEIGHT - 60, 100, 40)
                pygame.draw.rect(window, SECONDARY_COLOR, solve_button, border_radius=10)
                pygame.draw.rect(window, SHADOW_COLOR, solve_button, 3, border_radius=10)
                solve_text = button_font.render("Solve", True, WHITE)
                window.blit(solve_text, (solve_button.centerx - solve_text.get_width() // 2,
                                        solve_button.centery - solve_text.get_height() // 2))

            # Message si résolu
            if solved:
                solved_text = font.render("Solved!", True, (0, 200, 0))
                window.blit(solved_text, (WIDTH // 2 - solved_text.get_width() // 2, HEIGHT - 110))

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
