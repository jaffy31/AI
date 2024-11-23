"""
Python Program to Solve Cryptarithmetic Problem

Question:
Write a Python program to solve the Cryptarithmetic problem "CROSS + ROADS = DANGER".

How to Run:
1. Windows:
   Open Command Prompt or PowerShell and navigate to the directory containing this script.
   Run the command: python cryptarithmetic.py

2. Linux:
   Open a terminal and navigate to the directory containing this script.
   Run the command: python3 cryptarithmetic.py
"""

from itertools import permutations

def is_valid_assignment(assignment):
    cross = assignment['C']*10000 + assignment['R']*1000 + assignment['O']*100 + assignment['S']*10 + assignment['S']
    roads = assignment['R']*10000 + assignment['O']*1000 + assignment['A']*100 + assignment['D']*10 + assignment['S']
    danger = assignment['D']*100000 + assignment['A']*10000 + assignment['N']*1000 + assignment['G']*100 + assignment['E']*10 + assignment['R']

    return cross + roads == danger

def solve_cryptarithmetic():
    letters = ['C', 'R', 'O', 'S', 'A', 'D', 'N', 'G', 'E']
    for perm in permutations(range(10), len(letters)):
        assignment = dict(zip(letters, perm))
        if is_valid_assignment(assignment):
            print(f"Solution found: {assignment}")
            print(f"{assignment['C']} {assignment['R']} {assignment['O']} {assignment['S']} {assignment['S']}")
            print(f"+ {assignment['R']} {assignment['O']} {assignment['A']} {assignment['D']} {assignment['S']}")
            print("-----------")
            print(f"{assignment['D']} {assignment['A']} {assignment['N']} {assignment['G']} {assignment['E']} {assignment['R']}")
            return
    print("No solution found.")

if __name__ == "__main__":
    solve_cryptarithmetic()
