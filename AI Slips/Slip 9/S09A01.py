"""
8-Puzzle Solver using A* Algorithm

Question:
Write a Python program to solve the 8-puzzle problem using the A* algorithm.

How to Run:
1. Windows:
   Open Command Prompt or PowerShell and navigate to the directory containing this script.
   Run the command: python 8_puzzle_solver.py

2. Linux:
   Open a terminal and navigate to the directory containing this script.
   Run the command: python3 8_puzzle_solver.py
"""

import heapq

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def find_blank(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def is_goal_state(board):
    return board == [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

def get_neighbors(board):
    i, j = find_blank(board)
    neighbors = []

    if i > 0:
        neighbors.append((i - 1, j))
    if i < 2:
        neighbors.append((i + 1, j))
    if j > 0:
        neighbors.append((i, j - 1))
    if j < 2:
        neighbors.append((i, j + 1))

    return neighbors

def calculate_heuristic(board):
    # Manhattan distance heuristic
    heuristic = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                goal_row, goal_col = divmod(board[i][j], 3)
                heuristic += abs(i - goal_row) + abs(j - goal_col)
    return heuristic

def a_star(initial_board):
    heap = [(calculate_heuristic(initial_board), 0, initial_board)]
    visited = set()

    while heap:
        _, cost, current_board = heapq.heappop(heap)
        visited.add(tuple(map(tuple, current_board)))

        if is_goal_state(current_board):
            return cost, current_board

        blank_row, blank_col = find_blank(current_board)
        for neighbor_row, neighbor_col in get_neighbors(current_board):
            new_board = [row[:] for row in current_board]
            new_board[blank_row][blank_col], new_board[neighbor_row][neighbor_col] = new_board[neighbor_row][neighbor_col], new_board[blank_row][blank_col]
            if tuple(map(tuple, new_board)) not in visited:
                heapq.heappush(heap, (cost + 1 + calculate_heuristic(new_board), cost + 1, new_board))

if __name__ == "__main__":
    initial_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]  # Change this to your initial state
    print("Initial State:")
    print_board(initial_state)

    steps, final_state = a_star(initial_state)

    print("\nFinal State:")
    print_board(final_state)

    print(f"\nNumber of steps to reach the goal: {steps}")
