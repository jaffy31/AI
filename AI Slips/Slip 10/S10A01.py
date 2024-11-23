"""
Cryptarithmetic Problem Solver

Question:
Write a Python program to solve the cryptarithmetic problem "TWO + TWO = FOUR".

How to Run:
1. Windows:
   Open Command Prompt or PowerShell and navigate to the directory containing this script.
   Run the command: python cryptarithmetic_solver.py

2. Linux:
   Open a terminal and navigate to the directory containing this script.
   Run the command: python3 cryptarithmetic_solver.py
"""

from itertools import permutations

def solve_cryptarithmetic():
    # Define the unique letters in the problem
    letters = 'TWOFUR'
    
    # Generate all possible digit permutations for the letters
    for perm in permutations(range(10), len(letters)):
        # Map letters to digits
        mapping = dict(zip(letters, perm))
        
        # Extract numbers from the mapping
        T, W, O, F, U, R = mapping['T'], mapping['W'], mapping['O'], mapping['F'], mapping['U'], mapping['R']
        
        # Ensure leading digits are not zero
        if T == 0 or F == 0:
            continue
        
        # Construct the numbers TWO and FOUR
        TWO = T * 100 + W * 10 + O
        FOUR = F * 1000 + O * 100 + U * 10 + R
        
        # Check if the equation holds
        if TWO + TWO == FOUR:
            print(f"SOLUTION: TWO={TWO}, FOUR={FOUR}")
            print(f"Mapping: {mapping}")
            return

    print("No solution found.")

# Run the solver
solve_cryptarithmetic()

