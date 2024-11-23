"""
String Transformation using Mean-End Analysis Algorithm

Question:
Write a Python program using the Mean-End Analysis algorithm to transform a string of
lowercase letters into another string.

How to Run:
1. Windows:
   Open Command Prompt or PowerShell and navigate to the directory containing this script.
   Run the command: python mean_end_analysis.py

2. Linux:
   Open a terminal and navigate to the directory containing this script.
   Run the command: python3 mean_end_analysis.py
"""

def mean_end_analysis(start, goal):
    operations = []

    while start != goal:
        # Find the first character that differs between start and goal
        index = next((i for i, (s, g) in enumerate(zip(start, goal)) if s != g), None)

        if index is not None:
            # Choose an operation (e.g., replace)
            operations.append(f"Replace '{start[index]}' at index {index} with '{goal[index]}'")
            start = start[:index] + goal[index] + start[index + 1:]
        else:
            break

    return operations

if __name__ == "__main__":
    initial_string = "abcd"
    goal_string = "bcda"

    transformation_operations = mean_end_analysis(initial_string, goal_string)

    if transformation_operations:
        print("Transformation Operations:")
        for operation in transformation_operations:
            print(operation)
    else:
        print("No transformation needed. The strings are already the same.")
