"""
Python Program to Remove Punctuations from a Given String (Without Importing string Module)

Question:
Write a Python program to remove punctuations from the given string without importing the string module.
"""

def remove_punctuation(input_string):
    # Define a set of punctuation characters
    punctuation_chars = set("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    
    # Create a translation table to remove punctuations
    translation_table = str.maketrans("", "", "".join(punctuation_chars))
    
    # Use translate method to remove punctuations from the input string
    cleaned_string = input_string.translate(translation_table)
    
    return cleaned_string

if __name__ == "__main__":
    # Input: String with punctuations
    input_string = input("Enter a string with punctuations: ")

    # Remove punctuations
    result_string = remove_punctuation(input_string)

    # Print the result
    print("String without punctuations:", result_string)
