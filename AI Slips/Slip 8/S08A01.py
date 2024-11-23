"""
Count Uppercase and Lowercase Alphabets in a String

Question:
Write a Python program to accept a string. Find and print the number of uppercase alphabets
and lowercase alphabets.

How to Run:
1. Windows:
   Open Command Prompt or PowerShell and navigate to the directory containing this script.
   Run the command: python count_alphabets.py

2. Linux:
   Open a terminal and navigate to the directory containing this script.
   Run the command: python3 count_alphabets.py
"""

def count_alphabets(input_string):
    uppercase_count = sum(1 for char in input_string if char.isupper())
    lowercase_count = sum(1 for char in input_string if char.islower())

    print(f"Number of Uppercase Alphabets: {uppercase_count}")
    print(f"Number of Lowercase Alphabets: {lowercase_count}")

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    count_alphabets(user_input)
