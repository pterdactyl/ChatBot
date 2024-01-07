import sys
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('punkt')
nltk.download('vader_lexicon')

# Initialize Sentiment Analyzer
sid = SentimentIntensityAnalyzer()

# Set up responses
responses = {
    "hi": "Hello!",
    "bye": "Goodbye! Have a great day!",
    "what is your name": "I am a simple chatbot.",
}

# Function to handle conversation with sentiment analysis
def chat():
    print("Welcome! Type 'bye' to exit.")
    while True:
        try:
            user_input = sys.stdin.readline().strip().lower()
        except KeyboardInterrupt:
            break

        if user_input == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Check for specific responses
        if user_input in responses:
            print("Chatbot:", responses[user_input])
        else:
            # Perform Sentiment Analysis on user input
            sentiment_scores = sid.polarity_scores(user_input)
            compound_score = sentiment_scores['compound']

            if compound_score >= 0.05:
                print("Chatbot: That sounds good!")
            elif compound_score <= -0.05:
                print("Chatbot: I'm sorry to hear that.")
            else:
                print("Chatbot: I'm neutral about that.")

if __name__ == "__main__":
    chat()
