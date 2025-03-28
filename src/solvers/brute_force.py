import time
from turtle import st
from pygame.locals import *
from itertools import product
import os
import pygame

pygame.init()


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

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NEURALGRID")

current_dir = os.path.dirname(os.path.abspath(__file__))
font_paths = [
    os.path.join(current_dir, 'fonts', 'Poppins-Regular.ttf'),
    os.path.join(current_dir, '..', 'ui', 'fonts', 'Poppins-Regular.ttf'),
    'fonts/Poppins-Regular.ttf']
font_path = next(path for path in font_paths if os.path.exists(path))
font = pygame.font.Font(font_path, 30)
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

class BruteForceSolver:
    def __init__(self,sudokuGrid):
        self.grid = sudokuGrid.grid
        self.solutions_tried = 0
        self.elapsed_time = 0

    def solve(self):

        return self.BruteForce(self.grid)

    def solveGraph(self,window,bgColor):

        return self.BruteForceGraph(self.grid,window,bgColor)

    def find_empty_cases(self,grid):
        empty_cases = []
        for row in range(9):
            for col in range(9):
                if grid[row, col] == 0:
                    
                    empty_cases.append((row,col))
        return empty_cases
    
    def is_valid_move(self, row, col, num):
        if num in self.grid[row]:
                return False

        if num in [self.grid[i][col] for i in range(9)]:
            return False

        start_row, start_col = (row // 3) * 3, (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False

        return True

    def BruteForce(self, grid):
        empty_cases = self.find_empty_cases(self.grid)

        if not empty_cases:  # If there are no empty cells, the grid is solved
            return True
        start_time = time.time()
        # Generate all possibilities for the empty cases
        for combinaison in product(range(1, 10), repeat=len(empty_cases)):
            elapsed_time = time.time() - start_time
            self.solutions_tried += 1
            print(f"\r {self.solutions_tried} {self.numberOfPossibilties()} {elapsed_time:6f}      {self.timeNeededToSolve()}",end="")
            pygame.display.flip()
            # Try each possibility
            for (row, col), chiffre in zip(empty_cases, combinaison):
                if not self.is_valid_move(row, col, chiffre):
                    break
                grid[row, col] = chiffre

            else:
                return True
            for row, col in empty_cases:
                grid[row , col] = 0

        return False

    def BruteForceGraph(self, grid,window,bgColor):
        empty_cases = self.find_empty_cases(self.grid)

        if not empty_cases:  # If there are no empty cells, the grid is solved
            return True
        start_time = time.time()
        # Generate all possibilities for the empty cases
        for combinaison in product(range(1, 10), repeat=len(empty_cases)):
            self.elapsed_time = (time.time() - start_time)
            self.solutions_tried += 1
            self.draw_grid()
            self.draw_numbers(self.grid)
            self.draw_info(window,self.elapsed_time,self.solutions_tried)
            pygame.display.flip()
            # Try each possibility
            for (row, col), chiffre in zip(empty_cases, combinaison):
                if not self.is_valid_move(row, col, chiffre):
                    break
                grid[row, col] = chiffre
            else:
                return True
            for row, col in empty_cases:
                grid[row, col] = 0

        return False

    def numberOfPossibilties(self):
        numberOfEmptyCases = len(self.find_empty_cases(self.grid))
        return 9**(81-numberOfEmptyCases)

    def timeNeededToSolve(self):
        return (self.numberOfPossibilties() * 10**-6)//31536000

    def draw_info(self,window, temps_ecoule, solutions_essayees):
        title = title_font.render("Sudoku", True, WHITE)
        window.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))
        info_rect = pygame.Rect(10, HEIGHT - 100, WIDTH - 20, 80)  # Adjust dimensions as needed
        # Clear the area by filling it with the background color
        pygame.draw.rect(window, BACKGROUND_COLOR, info_rect)
        elapsed_time_text = font.render(f"Elapsed Time: {temps_ecoule:.2f} s", True, WHITE)
        window.blit(elapsed_time_text, (10, 600))

        # Draw solutions tried
        solutions_tried_text = font.render(f"Solutions Tried: {solutions_essayees}", True, WHITE)
        window.blit(solutions_tried_text, (10, 640))  # Offset for the second line

    def draw_grid(self):
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

    def draw_numbers(self,grid, solved=False, original_grid=None):
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

if __name__ == "__main__":
    pass