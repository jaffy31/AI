"""
Tic-Tac-Toe Solver in Python

Question:
Write a Python program to solve the Tic-Tac-Toe problem.

How to Run:
1. Windows:
   Open Command Prompt or PowerShell and navigate to the directory containing this script.
   Run the command: python tic_tac_toe_solver.py

2. Linux:
   Open a terminal and navigate to the directory containing this script.
   Run the command: python3 tic_tac_toe_solver.py
"""

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == 'X' for j in range(3)) or all(board[j][i] == 'X' for j in range(3)):
            return 'X'
        if all(board[i][j] == 'O' for j in range(3)) or all(board[j][i] == 'O' for j in range(3)):
            return 'O'

    # Check diagonals
    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2 - i] == 'X' for i in range(3)):
        return 'X'
    if all(board[i][i] == 'O' for i in range(3)) or all(board[i][2 - i] == 'O' for i in range(3)):
        return 'O'

    return None

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def tic_tac_toe_solver():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while True:
        print_board(board)
        row = int(input(f"Enter the row for player {player} (0, 1, 2): "))
        col = int(input(f"Enter the column for player {player} (0, 1, 2): "))

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = player
            winner = check_winner(board)

            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            player = 'O' if player == 'X' else 'X'
        else:
            print("Invalid move. Please try again.")

if __name__ == "__main__":
    tic_tac_toe_solver()
