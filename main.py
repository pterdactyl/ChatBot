# Step 1: Set Up the Conversation
responses = {
    "hi": "Hello!",
    "how are you?": "I'm good, thank you!",
    "bye": "Goodbye! Have a great day!"
    # Add more responses based on your preference
}

# Step 2: Build the Chat Function
def chat():
    print("Welcome! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = responses.get(user_input, "I'm sorry, I don't understand that.")
        print("Chatbot:", response)

# Step 3: Run the Chatbot
if __name__ == "__main__":
    chat()