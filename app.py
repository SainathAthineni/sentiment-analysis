import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download resources for the NLTK library (only needs to be done once)
nltk.download('vader_lexicon')

def main():
    st.title("Sentiment Analysis App")
    user_input = st.text_input("Enter your text:")
    if st.button("Analyze"):
        sentiment_result = analyze_sentiment(user_input)
        st.write("Sentiment:", sentiment_result)

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)['compound']

    if sentiment_score >= 0.05:
        return 'Positive'
    elif sentiment_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

if __name__ == "__main__":
    main()
