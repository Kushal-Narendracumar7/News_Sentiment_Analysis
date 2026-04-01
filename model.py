#!/usr/bin/env python
# coding: utf-8

# In[1]:


from transformers import pipeline


# In[ ]:
classifier = pipeline(model="cardiffnlp/twitter-roberta-base-sentiment-latest")

def analyze_sentiment(texts):
        return classifier(texts,batch_size = 32)

# In[ ]:




