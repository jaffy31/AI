"""
Lemmatization without NLTK in Python

Question:
Write a Python program to implement lemmatization without using the NLTK library.
Description:
Lemmatization is the process of reducing words to their base or root form.

How to Run:
1. Windows:
   Open Command Prompt or PowerShell and navigate to the directory containing this script.
   Run the command: python lemmatization_without_nltk.py

2. Linux:
   Open a terminal and navigate to the directory containing this script.
   Run the command: python3 lemmatization_without_nltk.py
"""

def lemmatize_word(word):
    lemmatization_dict = {
        'dogs': 'dog',
        'barking': 'bark',
        'running': 'run',
        'are': 'will',
        'is': 'be',
        'am': 'will'
        # Add more mappings as needed
    }
    return lemmatization_dict.get(word, word)

def lemmatize_text(text):
    tokens = text.split()
    lemmatized_tokens = [lemmatize_word(token) for token in tokens]
    lemmatized_text = ' '.join(lemmatized_tokens)
    return lemmatized_text

if __name__ == "__main__":
    # Example usage
    input_text = "The dogs are barking loudly. I am running ."
    lemmatized_result = lemmatize_text(input_text)

    print("Original Text:")
    print(input_text)
    
    print("\nLemmatized Text:")
    print(lemmatized_result)
