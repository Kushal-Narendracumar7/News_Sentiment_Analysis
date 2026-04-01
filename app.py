import streamlit as st

def main():
    st.title("News Sentiment Analysis")

    st.write("Welcome to the News Sentiment Analysis app! This application allows you to analyze the sentiment of news articles. You can input a news article or provide a URL to analyze its sentiment.")

    input = st.text_area("Enter few keywords for getting the news articles")

    if st.button("Analyze Sentiment"):
        text_input = input.replace(","," AND ")
        st.write(f"Analyzing sentiment for: {text_input}")

if __name__ == "__main__":
    main()