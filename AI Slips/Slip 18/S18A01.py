"""
Remove Stop Words without NLTK in Python

Question:
Write a Python program to remove stop words for a given passage from a text file without using NLTK.
Description:
Stop words are common words that are often removed from text data during natural language processing tasks as they usually do not carry significant meaning.

How to Run:
1. Windows:
   Open Command Prompt or PowerShell and navigate to the directory containing this script.
   Run the command: python remove_stop_words.py

2. Linux:
   Open a terminal and navigate to the directory containing this script.
   Run the command: python3 remove_stop_words.py

Note:
1. Create a text file named 'your_file.txt' in the current directory.
2. Add a passage of text to the file for stop words removal.

Example of text file content:
The quick brown fox jumps over the lazy dog. This is a simple example passage for testing stop words removal.
"""

import os

def remove_stop_words(file_name):
    stop_words = set([
        "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves",
        "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their",
        "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was",
        "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and",
        "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between",
        "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on",
        "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all",
        "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same",
        "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "d", "ll", "m", "o", "re",
        "ve", "y", "ain", "aren", "couldn", "didn", "doesn", "hadn", "hasn", "haven", "isn", "ma", "mightn", "mustn", "needn",
        "shan", "shouldn", "wasn", "weren", "won", "wouldn"
    ])

    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, file_name)

    with open(file_path, 'r', encoding='utf-8') as file:
        passage = file.read()

    words = passage.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]

    result = ' '.join(filtered_words)

    return result

if __name__ == "__main__":
    # Use a file in the current directory
    input_file_name = 'your_file.txt'

    result_text = remove_stop_words(input_file_name)

    # Print the result
    print("Original Passage:")
    with open(input_file_name, 'r', encoding='utf-8') as file:
        original_passage = file.read()
        print(original_passage)

    print("\nPassage after removing stop words:")
    print(result_text)
