#!/usr/bin/env python
# coding: utf-8

# In[1]:


from data_collection import collect_news_data
from model import analyze_sentiment
import pandas as pd


# In[1]:


def get_sentiments(df):
    df['text_to_analyze'] = df['text_to_analyze'].fillna('').astype(str)
    df['sentiments'] = df['text_to_analyze'].apply(lambda x : analyze_sentiment(x)[0]['label'])
    return df


# In[ ]:




