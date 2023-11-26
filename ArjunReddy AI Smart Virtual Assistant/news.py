# news_functions.py

from newsapi import NewsApiClient

def get_latest_news(api_key, news_source):
    try:
        # Initialize the NewsApiClient with your API key
        newsapi = NewsApiClient(api_key=api_key)

        # Specify the news source and get the latest headlines
        top_headlines = newsapi.get_top_headlines(sources=news_source)

        # Extract and return the news headlines
        headlines = [article['title'] for article in top_headlines['articles']]
        print("Here are the latest news headlines:")
        for index, headline in enumerate(headlines, start=1):
            print(f"{index}. {headline}")

    except Exception as e:
        print(f"Sorry, I couldn't fetch the latest news. Error: {e}")
