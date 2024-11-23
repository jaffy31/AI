"""
Hill Climbing Algorithm to Find Maximum of a Mathematical Function

Question:
Write a Python program that demonstrates the hill climbing algorithm to find the maximum of a mathematical function.
For example, consider the function f(x) = -x^2 + 4x.

How to Run:
1. Windows:
   Open Command Prompt or PowerShell and navigate to the directory containing this script.
   Run the command: python hill_climbing.py

2. Linux:
   Open a terminal and navigate to the directory containing this script.
   Run the command: python3 hill_climbing.py
"""

import numpy as np

def objective_function(x):
    # Define the objective function (in this case, f(x) = -x^2 + 4x)
    return -x**2 + 4*x

def hill_climbing(initial_x, step_size, max_iterations):
    current_x = initial_x
    
    for _ in range(max_iterations):
        current_value = objective_function(current_x)
        next_x = current_x + step_size
        next_value = objective_function(next_x)
        
        if next_value > current_value:
            current_x = next_x
        else:
            break
    
    return current_x, objective_function(current_x)

if __name__ == "__main__":
    # Set initial parameters
    initial_x = np.random.uniform(-10, 10)  # Initial random starting point
    step_size = 0.1
    max_iterations = 100
    
    # Run the hill climbing algorithm
    result_x, result_value = hill_climbing(initial_x, step_size, max_iterations)
    
    # Print the results
    print("Optimal x:", result_x)
    print("Optimal value:", result_value)
