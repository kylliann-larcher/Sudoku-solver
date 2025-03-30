# Sudoku Solver

## Project Overview
This project is a **Sudoku Solver** implemented in Python using **Pygame** for graphical visualization. The solver is capable of solving Sudoku puzzles using different algorithms, providing an interactive experience for users who wish to visualize the solving process.

The main objectives of this project are:
- Implement a Sudoku solving algorithm.
- Provide a user-friendly graphical interface.
- Optimize execution time and compare different solving strategies.

## Algorithms Used
Two main approaches were considered for solving Sudoku:
1. **Backtracking Algorithm**
   - A brute-force approach that recursively attempts to fill the board.
   - Checks constraints at each step and backtracks when a conflict occurs.
   - Guarantees a solution if the puzzle is valid but can be slow for complex grids.

2. **Constraint Propagation with AC-3 (Arc Consistency Algorithm)**
   - Reduces the number of possibilities before applying backtracking.
   - Improves efficiency by enforcing consistency in the grid constraints.

Both approaches were tested and compared in terms of execution time and efficiency.

## Tools and Technologies
The project was developed using the following tools and libraries:

- **Python**: Main programming language.
- **Pygame**: Used for graphical visualization of the Sudoku board.
- **Time Library**: Used for measuring execution time of different algorithms.
- **Object-Oriented Programming (OOP)**: Applied to structure the project efficiently.
- **Trello**: Used for project management and task tracking.

## Development Process
### Project Management
Trello was used to organize the development process into different phases:
- **Planning**: Define project scope and functionalities.
- **Implementation**: Develop algorithms and integrate graphical components.
- **Testing & Optimization**: Measure performance and improve efficiency.
- **Finalization**: Ensure stability and usability.

### Code Structure
The project follows an **OOP-based structure**, making it modular and maintainable:
- `sudoku.py`: Contains the Sudoku board representation and constraints.
- `backtracking.py`: Implements solving algorithms (backtracking).
- `brute_force.py`: Implements solving algorithms (Brute Force).
- `sudoku_graphical_interface.py`: Manages the graphical interface with Pygame.
- `main.py`: Runs the application.
