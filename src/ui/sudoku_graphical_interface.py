import pygame
import sys

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)

# Define dimensions
WIDTH, HEIGHT = 600, 600  # Window size
GRID_SIZE = 9  # Size of the Sudoku grid (9x9)
GRID_WIDTH = 400  # Reduced grid width
GRID_HEIGHT = 400  # Reduced grid height
CELL_SIZE = GRID_WIDTH // GRID_SIZE  # Cell size
MARGIN_TOP = 100  # Top margin
MARGIN_LEFT = (WIDTH - GRID_WIDTH) // 2  # Left margin to center the grid

# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

# Font for the numbers
font = pygame.font.SysFont('Arial', 30)  # Slightly smaller font

# Function to draw the grid
def draw_grid():
    # Draw cells
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            # Rectangle for each cell
            rect = pygame.Rect(
                MARGIN_LEFT + i * CELL_SIZE, 
                MARGIN_TOP + j * CELL_SIZE, 
                CELL_SIZE, 
                CELL_SIZE
            )
            # Draw with thin border
            pygame.draw.rect(window, WHITE, rect)
            pygame.draw.rect(window, GRAY, rect, 1)
    
    # Draw the 3x3 subgrid lines (thicker)
    for i in range(0, GRID_SIZE + 1, 3):
        # Vertical lines
        pygame.draw.line(
            window, BLACK, 
            (MARGIN_LEFT + i * CELL_SIZE, MARGIN_TOP), 
            (MARGIN_LEFT + i * CELL_SIZE, MARGIN_TOP + GRID_HEIGHT), 
            3
        )
        # Horizontal lines
        pygame.draw.line(
            window, BLACK, 
            (MARGIN_LEFT, MARGIN_TOP + i * CELL_SIZE), 
            (MARGIN_LEFT + GRID_WIDTH, MARGIN_TOP + i * CELL_SIZE), 
            3
        )

# Function to draw the numbers in the grid
def draw_numbers(grid):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            # Check if cell is not empty and indices are within range
            if i < len(grid) and j < len(grid[i]) and grid[i][j] != 0:
                # Calculate the center position of the number
                x = MARGIN_LEFT + j * CELL_SIZE + CELL_SIZE // 2
                y = MARGIN_TOP + i * CELL_SIZE + CELL_SIZE // 2
                
                # Create the text
                text = font.render(str(grid[i][j]), True, BLACK)
                # Center the text in the cell
                text_rect = text.get_rect(center=(x, y))
                # Draw the text
                window.blit(text, text_rect)

example_grid = [
    [7, 2, 9, '_', '_', '_', 3, '_', '_'],
    ['_', '_', 1, '_', 6, '_', 8, '_', '_'],
    ['_', '_', '_', '_', 4, '_', '_', 6, '_'],
    [9, 6, '_', '_', '_', 4, 1, '_', 8],
    ['_', 4, 8, 7, '_', 5, '_', 9, 6],
    ['_', '_', 5, 6, '_', 8, '_', '_', 3],
    ['_', '_', '_', 4, '_', 2, '_', 1, '_'],
    [8, 5, '_', '_', 6, '_', 3, 2, 7],
    [1, '_', '_', 8, 5, '_', '_', '_', '_']
]


# Main game loop
def main():
    running = True
    
    while running:
        window.fill(WHITE)
        
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Draw the title
        title_font = pygame.font.SysFont('Arial', 40)
        title = title_font.render("Sudoku", True, BLACK)
        window.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))
        
        # Draw the grid
        draw_grid()
        
        # Draw the numbers
        draw_numbers(example_grid)
        
        # Update the display
        pygame.display.update()
    
    pygame.quit()
    sys.exit()

# Run the game if this file is executed directly
if __name__ == "__main__":
    main()