import streamlit as st 
from data_collection import collect_news_data 
from sentiment_analysis import get_sentiments
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def main():
    st.title("News Sentiment Analysis")
    st.write("Enter few keywords separated by comma to analyze the sentiments of news articles related to those keywords")
    keywords = st.text_area("Keywords")
    days = st.slider("Select number of days to analyze",1,30,7)

    if st.button("Analyze Sentiments"):

        if not keywords:    
            st.warning("Please enter some keywords to analyze.")
            return 
        text_input = "OR".join(k.strip() for k in keywords.split(','))
        try : 
            with st.spinner("Fetching Data"):
                news_df = collect_news_data(text_input,days)

            with st.spinner("Analyzing Sentiments"):
                news_df = get_sentiments(news_df)
        
            with st.spinner("Generating Visualizations"):
                st.bar_chart(news_df['sentiments'].value_counts())
                title = "".join(news_df['title'].dropna().astype(str))
                wc = WordCloud(width = 800,height = 400, background_color = 'white').generate(title)
                plt.figure(figsize = (10,6))
                plt.imshow(wc,interpolation = 'bilinear')
                plt.axis('off')
                plt.show()
                st.pyplot(plt)

            st.subheader("News Articles")
            for _,rows in news_df.iterrows():
                st.markdown(f"[{rows['title']}]({rows['url']})")
            
            if st.button("Download CSV"):
                csv = news_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download data as CSV",
                    data=csv,
                    file_name='news_sentiment_analysis.csv',
                    mime='text/csv',
                )

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()