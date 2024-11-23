
from itertools import permutations

def is_valid_assignment(assignment):
    s, e, n, d, m, o, r, y = assignment['S'], assignment['E'], assignment['N'], assignment['D'], assignment['M'], assignment['O'], assignment['R'], assignment['Y']
    # Check if the equation holds: SEND + MORE == MONEY
    return s != 0 and m != 0 and (1000 * s + 100 * e + 10 * n + d + 1000 * m + 100 * o + 10 * r + e == 10000 * m + 1000 * o + 100 * n + 10 * e + y)

def solve_cryptarithmetic():
    letters = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']
    
    # Try all permutations of digits (0-9) for the letters
    for perm in permutations(range(10), len(letters)):
        assignment = dict(zip(letters, perm))
        
        # Check if the current assignment satisfies the equation
        if is_valid_assignment(assignment):
            # If a solution is found, print the result
            print(f"Solution found: {assignment}")
            print(f"{assignment['S']} {assignment['E']} {assignment['N']} {assignment['D']}")
            print(f"+ {assignment['M']} {assignment['O']} {assignment['R']} {assignment['E']}")
            print("-----------")
            print(f"{assignment['M']} {assignment['O']} {assignment['N']} {assignment['E']} {assignment['Y']}")
            return
    
    # If no solution is found after checking all permutations
    print("No solution found.")

if __name__ == "__main__":
    solve_cryptarithmetic()

    
