# streamlit_app.py

import streamlit as st
import pickle
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download resources for the NLTK library (only needs to be done once)
nltk.download('vader_lexicon')

# Load the pre-trained sentiment analysis model
with open('sentiment_model.pkl', 'rb') as model_file:
    sentiment_model = pickle.load(model_file)

# Streamlit app
def main():
    st.title("Simple Streamlit App for Sentiment Analysis")

    # User input
    user_input = st.text_input("Enter text:")
    
    if st.button("Analyze"):
        sentiment_result = analyze_sentiment(user_input)
        st.success(f"Sentiment: {sentiment_result}")

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)['compound']

    if sentiment_score >= 0.05:
        return 'Positive'
    elif sentiment_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

if __name__ == '__main__':
    main()
