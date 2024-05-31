from flask import render_template, request
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download resources for the NLTK library (only needs to be done once)
nltk.download('vader_lexicon')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    user_input = request.form['user_input']
    sentiment_result = analyze_sentiment(user_input)
    return render_template('index.html', user_input=user_input, sentiment_result=sentiment_result)

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
    app.run(debug=True)
