"""
Tic-Tac-Toe with Alpha-Beta Pruning

How to Run:
1. Windows:
   Open Command Prompt or PowerShell and navigate to the directory containing this script.
   Run the command: python tic_tac_toe_alpha_beta.py

2. Linux:
   Open a terminal and navigate to the directory containing this script.
   Run the command: python3 tic_tac_toe_alpha_beta.py
"""

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def evaluate(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return row[0]

    for col in range(len(board[0])):
        if len(set(board[row][col] for row in range(len(board)))) == 1 and board[0][col] != ' ':
            return board[0][col]

    if len(set(board[i][i] for i in range(len(board)))) == 1 and board[0][0] != ' ':
        return board[0][0]

    if len(set(board[i][len(board) - i - 1] for i in range(len(board)))) == 1 and board[0][len(board) - 1] != ' ':
        return board[0][len(board) - 1]

    return None

def is_full(board):
    return all(cell != ' ' for row in board for cell in row)

def is_game_over(board):
    return evaluate(board) or is_full(board)

def get_empty_cells(board):
    return [(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == ' ']

def minimax(board, depth, alpha, beta, maximizing_player):
    result = evaluate(board)

    if result:
        return -1 if maximizing_player else 1 if result == 'X' else -1

    if is_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = minimax(board, depth + 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            board[i][j] = ' '
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = minimax(board, depth + 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            board[i][j] = ' '
            if beta <= alpha:
                break
        return min_eval

def best_move(board):
    best_val = float('-inf')
    best_move = None

    for i, j in get_empty_cells(board):
        board[i][j] = 'X'
        move_val = minimax(board, 0, float('-inf'), float('inf'), False)
        board[i][j] = ' '

        if move_val > best_val:
            best_move = (i, j)
            best_val = move_val

    return best_move

def play_tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'

    while not is_game_over(board):
        print_board(board)

        if player == 'X':
            try:
                i, j = map(int, input("Enter your move (row and column separated by space): ").split())
            except ValueError:
                print("Invalid input. Please enter two space-separated integers.")
                continue

            if 0 <= i < 3 and 0 <= j < 3 and board[i][j] == ' ':
                board[i][j] = player
            else:
                print("Invalid move. Please try again.")
                continue
        else:
            print("Computer's move:")
            i, j = best_move(board)
            board[i][j] = player

        player = 'O' if player == 'X' else 'X'

    print_board(board)
    result = evaluate(board)

    if result:
        print(f"{result} wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_tic_tac_toe()
