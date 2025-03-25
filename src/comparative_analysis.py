import nltk
import pandas as pd
import matplotlib.pyplot as plt
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

def comparative_sentiment_analysis(articles):
    """
    Conducts sentiment analysis across multiple articles and generates insights.
    """
    sentiment_results = {"Positive": 0, "Negative": 0, "Neutral": 0}
    article_sentiments = []

    for article in articles:
        sentiment = analyze_sentiment(article["Summary"])
        sentiment_results[sentiment] += 1
        article_sentiments.append({
            "Title": article["Title"],
            "Sentiment": sentiment
        })

    # Display sentiment distribution
    df = pd.DataFrame(article_sentiments)
    print("\nSentiment Analysis Summary:")
    print(df)

    # Plot sentiment distribution
    plt.figure(figsize=(6, 4))
    plt.bar(sentiment_results.keys(), sentiment_results.values(), color=["green", "red", "gray"])
    plt.title("Sentiment Distribution Across News Articles")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    plt.show()

    return sentiment_results, df

# Example usage:
if __name__ == "__main__":
    articles = [
        {"Title": "Tesla launches new EV model", "Summary": "Tesla's new car is a game-changer, increasing sales by 30%."},
        {"Title": "Regulatory concerns for Tesla", "Summary": "Tesla faces investigation over self-driving technology."},
        {"Title": "Tesla's stock sees record highs", "Summary": "Investor confidence surges as Tesla's stock reaches new levels."},
        {"Title": "Tesla faces production delays", "Summary": "Chip shortages cause significant delays in Tesla's production."},
    ]

    sentiment_results, df = comparative_sentiment_analysis(articles)
