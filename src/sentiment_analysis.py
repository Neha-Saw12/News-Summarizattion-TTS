import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER lexicon if not already downloaded
nltk.download("vader_lexicon")

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """
    Performs sentiment analysis on the given text and classifies it as Positive, Negative, or Neutral.
    """
    sentiment_score = sia.polarity_scores(text)["compound"]

    if sentiment_score >= 0.05:
        return "Positive"
    elif sentiment_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Example usage:
if __name__ == "__main__":
    sample_text = input("Enter article summary for sentiment analysis: ")
    sentiment = analyze_sentiment(sample_text)
    print(f"Sentiment: {sentiment}")
