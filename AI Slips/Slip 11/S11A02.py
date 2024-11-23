"""
Water Jug Problem Solver

Question:
Write a Python program to solve the water jug problem. Two jugs with capacities 4 gallons
and 3 gallons are given with unlimited water supply. The target is to achieve 2 gallons of water
in the second jug.

How to Run:
1. Windows:
   Open Command Prompt or PowerShell and navigate to the directory containing this script.
   Run the command: python water_jug_solver.py

2. Linux:
   Open a terminal and navigate to the directory containing this script.
   Run the command: python3 water_jug_solver.py
"""

def water_jug_solver(capacity_jug1, capacity_jug2, target):
    jug1 = 0
    jug2 = 0

    while jug2 != target:
        print(f"Jug 1: {jug1} gallons | Jug 2: {jug2} gallons")

        # Fill jug2 from jug1
        transfer = min(jug1, capacity_jug2 - jug2)
        jug1 -= transfer
        jug2 += transfer

        # Check if the target is reached
        if jug2 == target:
            print(f"Jug 1: {jug1} gallons | Jug 2: {jug2} gallons")
            print("Target reached!")
            break

        # If jug2 is full, empty it
        if jug2 == capacity_jug2:
            print(f"Jug 1: {jug1} gallons | Jug 2: {jug2} gallons")
            print("Emptying Jug 2")
            jug2 = 0

        # If jug1 is empty, fill it
        if jug1 == 0:
            print(f"Jug 1: {jug1} gallons | Jug 2: {jug2} gallons")
            print("Filling Jug 1")
            jug1 = capacity_jug1

        # Pour water from jug1 to jug2
        pour = min(jug1, capacity_jug2 - jug2)
        jug1 -= pour
        jug2 += pour

    print(f"Final State: Jug 1: {jug1} gallons | Jug 2: {jug2} gallons")

if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target_gallons = 2

    water_jug_solver(jug1_capacity, jug2_capacity, target_gallons)
