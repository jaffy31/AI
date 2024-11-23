"""
Sort Sentence in Alphabetical Order

How to Run:
1. Windows:
   Open Command Prompt or PowerShell and navigate to the directory containing this script.
   Run the command: python sort_sentence.py

2. Linux:
   Open a terminal and navigate to the directory containing this script.
   Run the command: python3 sort_sentence.py
"""

def sort_sentence(sentence):
    words = sentence.split()
    sorted_words = sorted(words)
    sorted_sentence = ' '.join(sorted_words)
    return sorted_sentence

if __name__ == "__main__":
    input_sentence = input("Enter a sentence: ")
    sorted_result = sort_sentence(input_sentence)
    print("Sorted Sentence:", sorted_result)
