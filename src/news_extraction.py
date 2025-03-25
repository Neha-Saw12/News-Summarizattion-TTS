import requests
from bs4 import BeautifulSoup

def extract_news(company_name, num_articles=10):
    """
    Extracts news articles related to the given company using Google News RSS Feed.
    """
    search_url = f"https://news.google.com/rss/search?q={company_name}&hl=en-IN&gl=IN&ceid=IN:en"
    
    response = requests.get(search_url)
    if response.status_code != 200:
        return {"error": "Failed to fetch news data"}
    
    soup = BeautifulSoup(response.content, "xml")  # Parse as XML for RSS feeds
    articles = soup.find_all("item")[:num_articles]

    news_data = []
    for article in articles:
        title = article.title.text if article.title else "No title"
        
        # Remove HTML tags from the summary
        raw_summary = article.description.text if article.description else "No summary available"
        summary = BeautifulSoup(raw_summary, "html.parser").get_text()  # Strip HTML

        link = article.link.text if article.link else "No link"
        date = article.pubDate.text if article.pubDate else "Unknown date"
        source = article.source.text if article.source else "Unknown source"

        news_data.append({
            "title": title,
            "summary": summary,  # Now it's clean
            "source": source,
            "date": date,
            "link": link
        })

    return news_data

# Example usage:
if __name__ == "__main__":
    company = input("Enter Company Name: ")
    news_articles = extract_news(company)
    for article in news_articles:
        print(article)
