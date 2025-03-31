# Sudoku Solver

## 📌 Description
Sudoku Solver is a Python program designed to automatically solve Sudoku grids using different algorithmic approaches, including:
- **Brute Force**: A naive approach that tests all possible combinations.
- **Backtracking**: A more efficient recursive technique that intelligently explores possible solutions.

The project is built using **Object-Oriented Programming (OOP)** to ensure a clear and modular structure.

---

## 🚀 Features
✅ Load a Sudoku grid from a file or manual input.  
✅ Automatic solving using **Backtracking** and **Brute Force**.  
✅ Validity check for a move in the grid.  
✅ Clear display of the grid before and after solving.  
✅ Uses **numpy** for efficient matrix manipulation (optional).  

---

## 🔢 Code Structure
The project follows an **OOP-based structure**, making it modular and maintainable:
- `sudoku.py`: Contains the Sudoku board representation and constraints.
- `backtracking.py`: Implements solving algorithms (backtracking).
- `brute_force.py`: Implements solving algorithms (Brute Force).
- `sudoku_graphical_interface.py`: Manages the graphical interface with Pygame.
- `main.py`: Runs the application.

---

## 📂 Project Structure
```
Sudoku-Solver/
│── solver/
│   │── __init__.py
│   │── sudoku.py  # Class representing the Sudoku grid
│   │── brute_force.py  # Solving using Brute Force
│   │── backtracking.py  # Solving using Backtracking
│── tests/
│   │── sudoku.txt  # Unit tests
│── main.py  # Main interface to run the solver
│── README.md  # Project documentation
```

---

## 🛠️ Installation
### 1⃣ Prerequisites
- Python **3.x**
- pip (Python package manager)

### 3⃣ Run the program
```
python main.py
```

---

## 🎯 Usage
1. **Run `main.py`** and enter the Sudoku grid.
2. Select the solving method (**Backtracking** recommended).
3. Observe the generated solution! ✅

---

## 🔧 Tools and Technologies
The project was developed using the following tools and libraries:

- **Python**: Main programming language.
- **Pygame**: Used for graphical visualization of the Sudoku board.
- **Time Library**: Used for measuring execution time of different algorithms.
- **Object-Oriented Programming (OOP)**: Applied to structure the project efficiently.
- **Trello**: Used for project management and task tracking.

---

## 📅 Project Overview
This project is a **Sudoku Solver** implemented in Python using **Pygame** for graphical visualization. The solver is capable of solving Sudoku puzzles using different algorithms, providing an interactive experience for users who wish to visualize the solving process.

---

## 📊 Algorithm Comparison
To evaluate performance, both algorithms were tested on Sudoku puzzles of varying difficulty.

| Algorithm       | Easy Puzzle | Medium Puzzle | Hard Puzzle | Remarks                           |
|----------------|-------------|----------------|--------------|-----------------------------------|
| Brute Force    | ~0.3 sec    | >10 sec        | Timeout      | Inefficient for complex puzzles   |
| Backtracking   | ~0.1 sec    | ~0.3 sec       | ~1 sec       | Much faster and scalable          |

**Conclusion:** The backtracking algorithm is significantly more efficient and reliable than brute force. It avoids unnecessary checks by backtracking as soon as a rule violation is found, making it ideal for solving Sudoku puzzles of all difficulties.

---

## 📊 Development Process
### Project Management
Trello was used to organize the development process into different phases:
- **Planning**: Define project scope and functionalities.
- **Implementation**: Develop algorithms and integrate graphical components.
- **Testing & Optimization**: Measure performance and improve efficiency.
- **Finalization**: Ensure stability and usability.

---

## 📜 License
This project is licensed under the **MIT License**. Feel free to contribute! 🚀

---

## 📩 Contact
👤 **Author**: Kylliann LARCHER  
👤 **Author**: Paul-Emmanuel Buffe  
👤 **Author**: Hippolyte Geslain  
