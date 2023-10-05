
import sys

# python3 conversation.py

def simple_ai(user_input):
    # Predefined answers
    answers = {
        "hello": "Hello! How can I assist you today?",
        "how are you": "I'm just a program, but I'm doing well, thank you!",
        "bye": "(type just 'bye' to end the conversation)",
        "name": "I'm a simple AI created by Bleverse.",
        "age": "I don't have an age. I'm just a bunch of code!",
        "creator": "I was developed by some talented engineers at Bleverse."
    }

    # Check if we know an answer to the user's input
    for question, answer in answers.items():
        if question in user_input.lower():
            return answer
    
    # If we don't know the answer
    return "I'm sorry, I don't understand that."

def main():
    print("Hello! Type 'bye' to end our conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Simple AI: Goodbye! It was nice talking to you.")
            sys.exit()
        else:
            print("Simple AI:", simple_ai(user_input))

# Execute the main function if the script is run as the main module
if __name__ == "__main__":
    main()
