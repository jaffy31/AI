"""
8-Queens Problem Solver

How to Run:
1. Windows:
   Open Command Prompt or PowerShell and navigate to the directory containing this script.
   Run the command: python eight_queens_solver.py

2. Linux:
   Open a terminal and navigate to the directory containing this script.
   Run the command: python3 eight_queens_solver.py
"""

def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def print_solution(board):
    for row in range(8):
        line = ""
        for col in range(8):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def solve_eight_queens(board, row):
    if row == 8:
        # All queens are placed successfully
        print_solution(board)
        return

    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col
            solve_eight_queens(board, row + 1)
            board[row] = -1  # Backtrack

if __name__ == "__main__":
    initial_board = [-1] * 8  # Initialize the board with -1 indicating no queen in a row

    print("Solutions to the 8-Queens Problem:")
    solve_eight_queens(initial_board, 0)
