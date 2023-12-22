pip install googletrans==4.0.0-rc1
import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
from googletrans import Translator
import nltk
import emoji

# Download resources for the NLTK library (only needs to be done once)
nltk.download('vader_lexicon')

# Function to translate English text to a target language
def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)['compound']

    if sentiment_score >= 0.05:
        return 'Positive'
    elif sentiment_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def main():
    st.title("Sentiment Analysis Web App")

    user_input = st.text_area("Enter your text:")
    
    # Add checkboxes for translation and emoji analysis
    translate_checkbox = st.checkbox("Translate to:")
    target_language = st.selectbox("Select Language:", ["Telugu", "Hindi"])
    emoji_checkbox = st.checkbox("Include Emoji Analysis")

    if st.button("Analyze"):
        if translate_checkbox:
            # Translate English text to the selected language
            if target_language == "Telugu":
                user_input_translated = translate_text(user_input, 'te')
            elif target_language == "Hindi":
                user_input_translated = translate_text(user_input, 'hi')
            else:
                user_input_translated = user_input  # No translation
            
            st.write(f"{target_language} Translation: {user_input_translated}")
        else:
            user_input_translated = user_input

        if emoji_checkbox:
            # Analyze sentiment with emoji analysis
            user_input_with_emojis = emoji.demojize(user_input_translated)
            sentiment_result = analyze_sentiment(user_input_with_emojis)
        else:
            # Analyze sentiment without emoji analysis
            sentiment_result = analyze_sentiment(user_input_translated)

        st.write(f"Sentiment: {sentiment_result}")

if __name__ == "__main__":
    main()
