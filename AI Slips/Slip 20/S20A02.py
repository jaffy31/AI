import math

def minimax(nums, depth, is_maximizing, start, end):
    """
    Mini-Max function for a number-picking game.
    
    Args:
        nums: List of numbers in the game.
        depth: Current depth of the recursion.
        is_maximizing: Boolean, True if the current player is maximizing.
        start: Starting index of the list.
        end: Ending index of the list.

    Returns:
        The optimal score for the current player.
    """
    # Base case: no numbers left to pick
    if start > end:
        return 0

    if is_maximizing:
        # Maximizing player
        pick_start = nums[start] + minimax(nums, depth + 1, False, start + 1, end)
        pick_end = nums[end] + minimax(nums, depth + 1, False, start, end - 1)
        return max(pick_start, pick_end)
    else:
        # Minimizing player
        pick_start = minimax(nums, depth + 1, True, start + 1, end)
        pick_end = minimax(nums, depth + 1, True, start, end - 1)
        return min(pick_start, pick_end)

def find_best_move(nums):
    """
    Find the best move for the maximizing player (Player 1).
    
    Args:
        nums: List of numbers in the game.

    Returns:
        The optimal score and the indices of the chosen move.
    """
    best_score = -math.inf
    best_move = None

    for i in [0, len(nums) - 1]:
        # Simulate picking the first or last number
        current_score = nums[i] + minimax(nums, 1, False, (i + 1) if i == 0 else 0, (len(nums) - 2) if i == len(nums) - 1 else len(nums) - 1)
        if current_score > best_score:
            best_score = current_score
            best_move = i

    return best_score, best_move

# Example game
nums = [3, 9, 1, 2]

print("Initial List:", nums)
optimal_score, move = find_best_move(nums)
print(f"Optimal Score for Player 1: {optimal_score}")
print(f"Best Move: Pick number {nums[move]} at index {move}")
