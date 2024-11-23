"""
Simple Chatbot in Python

Question:
Write a Python program to implement a simple chatbot.

How to Run:
1. Windows:
   Open Command Prompt or PowerShell and navigate to the directory containing this script.
   Run the command: python simple_chatbot.py

2. Linux:
   Open a terminal and navigate to the directory containing this script.
   Run the command: python3 simple_chatbot.py
"""

def simple_chatbot():
    print("Simple Chatbot: Hello! How can I assist you today?")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Simple Chatbot: Goodbye!")
            break

        # Add your own simple responses based on user input
        if 'hello' in user_input.lower():
            print("Simple Chatbot: Hi there!")
        elif 'how are you' in user_input.lower():
            print("Simple Chatbot: I'm a computer program, so I don't have feelings, but I'm here to help!")
        else:
            print("Simple Chatbot: I'm not sure how to respond to that. Feel free to ask me something else.")

if __name__ == "__main__":
    simple_chatbot()
