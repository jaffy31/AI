from collections import deque

class PuzzleState:
    def __init__(self, board, parent=None):
        self.board = board
        self.parent = parent

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(tuple(map(tuple, self.board)))  # Convert list of lists to tuple of tuples for immutability

def get_neighbors(state):
    neighbors = []
    x, y = next((i, j) for i, row in enumerate(state.board) for j, val in enumerate(row) if val == 0)
    
    # Directions (right, left, down, up)
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:  # Check bounds
            # Create a new board by swapping the empty space (0)
            new_board = [row[:] for row in state.board]  # Create a copy of the board
            new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
            neighbors.append(PuzzleState(new_board, parent=state))  # Add the new state to neighbors
    
    return neighbors

def reconstruct_path(goal_state):
    path = []
    while goal_state:
        path.append(goal_state.board)
        goal_state = goal_state.parent
    return path[::-1]  # Reverse to get the path from start to goal

def solve_puzzle(initial_state):
    visited = set()  # Set to keep track of visited states
    queue = deque([initial_state])  # BFS queue

    while queue:
        current_state = queue.popleft()

        # Check if the current state is the goal state
        if current_state.board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            return reconstruct_path(current_state)

        # Mark the current state as visited
        visited.add(hash(current_state))

        # Explore neighbors
        for neighbor in get_neighbors(current_state):
            if hash(neighbor) not in visited:
                queue.append(neighbor)

    return None  # No solution found

if __name__ == "__main__":
    # Set an unsolved initial state (you can try different ones)
    initial_board = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]  # A scrambled state
    initial_state = PuzzleState(initial_board)

    solution_path = solve_puzzle(initial_state)

    if solution_path:
        print("Solution Found:")
        for step, board in enumerate(solution_path):
            print(f"Step {step + 1}:")
            for row in board:
                print(row)
            print("------")
    else:
        print("No solution found.")

