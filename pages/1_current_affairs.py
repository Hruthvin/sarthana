import streamlit as st
import requests

def fetch_news(category):
    """Fetch news based on category using News API"""
    NEWS_API_KEY = "pub_60208bd691345e57519b7d614bf21139f26f7"  # Your News API key
    NEWS_API_URL = "https://newsdata.io/api/1/news"
    params = {
        "apikey": NEWS_API_KEY,
        "country": "in",
        "language": "en",
        "category": category,
    }
    try:
        response = requests.get(NEWS_API_URL, params=params)
        response.raise_for_status()  # Will raise an error for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching news: {e}")
        return {}

def current_affairs():
    st.header("Daily Current Affairs")
    CATEGORIES = ["politics", "economy", "environment", "science", "world"]
    category = st.selectbox("Select News Category", CATEGORIES)

    if st.button("Fetch News"):
        news_data = fetch_news(category)
        if news_data and "results" in news_data and news_data["results"]:
            st.subheader(f"News for {category.capitalize()}:")
            for article in news_data["results"][:5]:
                st.write(f"**{article['title']}**")
                st.write(article.get("description", "No description available."))
                st.write(f"[Read more]({article['link']})")
                st.write("---")
        else:
            st.error("No news available for this category. Please try again later.")

# Call current_affairs() to run the page
if __name__ == "__main__":
    current_affairs()
