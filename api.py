from fastapi import FastAPI
from src.news_extraction import extract_news
from src.sentiment_analysis import analyze_sentiment
#from src.comparative_analysis import compare_sentiments
from src.comparative_analysis import comparative_sentiment_analysis  # Correct function name


#from src.text_to_speech import generate_hindi_speech
from src.tts_hindi import text_to_speech  # ✅ Use the correct function name


app = FastAPI()

@app.get("/")
def home():
    return {"message": "News Sentiment API is running"}

@app.get("/extract-news/{company}")
def get_news(company: str):
    articles = extract_news(company)
    return {"company": company, "articles": articles}

@app.post("/analyze-sentiment")
def sentiment_analysis(articles: list):
    sentiment_results = analyze_sentiment(articles)
    return {"sentiment_analysis": sentiment_results}

@app.post("/compare-sentiment")
def comparative_analysis(sentiment_results: dict):
    comparison = comparative_sentiment_analysis(sentiment_results)
    return {"comparative_analysis": comparison}

@app.post("/tts")
def generate_tts(text: str):
    audio_path = text_to_speech(text)
    return {"audio_file": audio_path}

