#Write a Python program to simulate the 4-Queens problem.

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True

def print_solution(board):
    for row in range(len(board)):
        line = ""
        for col in range(len(board)):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def solve_four_queens(board, row):
    if row == len(board):
        print("Solution:")
        print_solution(board)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solve_four_queens(board, row + 1)
            board[row] = -1 

if __name__ == "__main__":
    board_size = 4
    initial_board = [-1] * board_size 
    solve_four_queens(initial_board, 0)
