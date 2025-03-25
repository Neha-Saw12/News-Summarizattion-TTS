import sys
import os

# Dynamically add 'src' folder to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

# Import modules
from news_extraction import extract_news
from sentiment_analysis import analyze_sentiment
from tts_hindi import text_to_speech  # Renaming for clarity

import streamlit as st


# Streamlit UI
st.title("📢 News Sentiment & Hindi TTS Generator")

speaker_audio="src/ref20.wav"


# User input
company_name = st.text_input("Enter Company Name:", "Tesla")

if st.button("Fetch News & Generate Report"):
    st.write(f"🔍 Searching for news about: **{company_name}**")

    # Fetch News
    news_articles = extract_news(company_name)
    if "error" in news_articles:
        st.error("❌ Failed to fetch news articles.")
    else:
        st.success("✅ News articles fetched successfully!")

        # Display articles and analyze sentiment
        sentiment_summary = []
        combined_text = ""

        for idx, article in enumerate(news_articles):
            sentiment = analyze_sentiment(article["summary"])
            sentiment_summary.append(sentiment)
            combined_text += article["summary"] + ". "

            st.subheader(f"📰 Article {idx+1}: {article['title']}")
            st.write(f"📌 **Summary:** {article['summary']}")
            st.write(f"🧐 **Sentiment:** `{sentiment}`")

        # Generate TTS speech
        if combined_text.strip():
            st.write("🔊 Generating Hindi Speech...")
            speech_file = text_to_speech(combined_text, "output.wav", speaker_audio)
            if os.path.exists(speech_file):
                st.audio(speech_file, format="audio/wav")
                st.success("✅ Hindi Speech Generated!")
            else:
                st.error("❌ Error generating speech!")
