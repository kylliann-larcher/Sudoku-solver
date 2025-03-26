import pygame
import sys
import numpy as np
from pygame.locals import *
from sodoku_terminal import SudokuGrid

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)
DARK_GRAY = (100, 100, 100)

# Define dimensions
WIDTH, HEIGHT = 600, 700  # Increased height for the level selection
GRID_SIZE = 9
GRID_WIDTH = 400
GRID_HEIGHT = 400
CELL_SIZE = GRID_WIDTH // GRID_SIZE
MARGIN_TOP = 200  # Increased top margin for level buttons
MARGIN_LEFT = (WIDTH - GRID_WIDTH) // 2

# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

# Fonts
font = pygame.font.SysFont('Arial', 30)
title_font = pygame.font.SysFont('Arial', 40)
button_font = pygame.font.SysFont('Arial', 24)


def draw_grid():
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

def draw_numbers(grid):
    if grid is None:
        return
        
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 0:
                x = MARGIN_LEFT + j * CELL_SIZE + CELL_SIZE // 2
                y = MARGIN_TOP + i * CELL_SIZE + CELL_SIZE // 2
                
                text = font.render(str(grid[i][j]), True, BLACK)
                text_rect = text.get_rect(center=(x, y))
                window.blit(text, text_rect)

def draw_menu_algo():
    title_menu_ago = title_font.render("NEURALGRID - ALGORITHMS", True, BLACK)
    window.blit(title_menu_ago, (WIDTH // 2 - title_menu_ago.get_width() // 2, 30))
    
    choose_algo = font.render("Choose an Algorithm", True, BLACK)
    window.blit(choose_algo, (WIDTH // 2 - choose_algo.get_width() // 2, 80))

    buttons = []
    algo_button = [
        ("Brute Force Algorithm", 1),
        ("Backtracking Algorithm", 2),
    ]
    
    start_y = 150
    button_width = 300
    button_height = 50
    spacing = 20
    
    for i, (text, algo_id) in enumerate(algo_button):
        button_y = start_y + i * (button_height + spacing)

        button_rect = pygame.Rect(
            WIDTH // 2 - button_width // 2,
            button_y,
            button_width,
            button_height
        )
        
        color = LIGHT_BLUE if algo_id != 0 else (255, 150, 150)
        
        pygame.draw.rect(window, color, button_rect, border_radius=5)
        pygame.draw.rect(window, DARK_GRAY, button_rect, 2, border_radius=5)
        
        text_surf = button_font.render(text, True, BLACK)
        text_rect = text_surf.get_rect(center=button_rect.center)
        window.blit(text_surf, text_rect)
        
        buttons.append((algo_id, button_rect))
    
    return buttons
            
def draw_level_buttons():
    title = title_font.render("Choose a Level", True, BLACK)
    window.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))
    
    levels = [
        ("Easy", (100, 100)),
        ("Intermediate", (250, 100)),
        ("Difficult", (400, 100)),
        ("Expert", (175, 150)),
        ("Legendary", (325, 150))
    ]
    
    buttons = []
    for i, (text, pos) in enumerate(levels, 1):
        button_rect = pygame.Rect(pos[0], pos[1], 150, 40)
        pygame.draw.rect(window, LIGHT_BLUE, button_rect)
        pygame.draw.rect(window, DARK_GRAY, button_rect, 2)
        
        text_surf = button_font.render(text, True, BLACK)
        text_rect = text_surf.get_rect(center=button_rect.center)
        window.blit(text_surf, text_rect)
        
        buttons.append((i, button_rect))
    
    return buttons

def main():
    sudoku = SudokuGrid()
    grid = None
    running = True
    show_grid = False
    show_algo_menu = True
    selected_algo = None
    level_buttons = []

    level_files = {
        1: 'C:/Users/Windows/Desktop/projets/1a/sodoku/Sudoku-solver/grids/sudoku.txt',
        2: 'C:/Users/Windows/Desktop/projets/1a/sodoku/Sudoku-solver/grids/sudoku2.txt',
        3: 'C:/Users/Windows/Desktop/projets/1a/sodoku/Sudoku-solver/grids/sudoku3.txt',
        4: 'C:/Users/Windows/Desktop/projets/1a/sodoku/Sudoku-solver/grids/sudoku4.txt',
        5: 'C:/Users/Windows/Desktop/projets/1a/sodoku/Sudoku-solver/grids/evilsudoku.txt'
    }

    level_messages = {
        1: "EASY LEVEL",
        2: "INTERMEDIATE LEVEL",
        3: "DIFFICULT LEVEL",
        4: "EXPERT LEVEL",
        5: "LEGENDARY LEVEL"
    }

    while running:
        window.fill(WHITE)

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
                    for level, rect in level_buttons:
                        if rect.collidepoint(event.pos):
                            print(level_messages.get(level, ""))

                            file_path = level_files.get(level)
                            if file_path:
                                grid = sudoku.load_grid(file_path)
                                show_grid = True
                                break

                else:
                    back_button = pygame.Rect(20, 20, 100, 40)
                    if back_button.collidepoint(event.pos):
                        show_grid = False
                        grid = None
                        show_algo_menu = True
                        selected_algo = None

        if show_algo_menu:
            algo_buttons = draw_menu_algo()

        elif not show_grid:
            level_buttons = draw_level_buttons()

        else:
            title = title_font.render("Sudoku", True, BLACK)
            window.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))

            draw_grid()
            draw_numbers(grid)

            back_button = pygame.Rect(20, 20, 100, 40)
            pygame.draw.rect(window, LIGHT_BLUE, back_button)
            pygame.draw.rect(window, DARK_GRAY, back_button, 2)
            back_text = button_font.render("Back", True, BLACK)
            window.blit(back_text, (back_button.x + 20, back_button.y + 10))

        pygame.display.update()

    print("\n" + "=" * 35)
    print("   Thank you for playing! Goodbye   ")
    print("=" * 35 + "\n")

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()