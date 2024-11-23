from itertools import permutations

def is_valid_assignment(assignment):
    g, o, t, u = assignment['G'], assignment['O'], assignment['T'], assignment['U']
    left_side = (10 * g + o) + (10 * t + o)
    right_side = 100 * o + 10 * u + t
    return left_side == right_side

def solve_cryptarithmetic():
    letters = ['G', 'O', 'T', 'U']
    for perm in permutations(range(10), len(letters)):
        assignment = dict(zip(letters, perm))
        if is_valid_assignment(assignment):
            print(f"Solution found: {assignment}")
            print(f"{assignment['G']} {assignment['O']}")
            print(f"+ {assignment['T']} {assignment['O']}")
            print("--------")
            print(f"{assignment['O']} {assignment['U']} {assignment['T']}")
            return
    print("No solution found.")

if __name__ == "__main__":
    solve_cryptarithmetic()
