-6#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd 
import requests
from datetime import datetime,timedelta
import os


# In[20]:


def collect_news_data(keywords,days):
    API_URL = "https://newsapi.org/v2/everything"

    params = {
        'q' : keywords,
        'language':'en',
        'from' : (datetime.now() - timedelta(days = days)).strftime('%Y-%m-%d'),
        'to' : datetime.now().strftime('%Y-%m-%d'),
        'sortBy':'popularity',
        'apiKey':os.getenv('NEWS_KEY')
  599999999999999999999999993
  
  -
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    }

    response = requests.get(API_URL,params = params)
    data = response.json()
    news_df = pd.DataFrame(data['articles'])
    news_df = news_df[['title','description','content']]
    news_df['text_to_analyze'] = news_df['title'] + ' ' + news_df['description'] + ' ' + news_df['content']
    return news_df


