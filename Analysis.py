#sentiment analysis- https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/?ref=rp
import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from nltk.util import pr 
from textblob import TextBlob


def word_count(text):
    
    skips = [".", ",", ":", ";", "'", '"',"!","?"]
    for ch in skips: 
        text = text.replace(ch, " ") 
    word_counts = {} 
    for word in text.split(" "): 
        if word in word_counts: 
            word_counts[word]+= 1 
        else: 
            word_counts[word]= 1 
    return word_counts  



def sentiment_analysis(text):
    Blob=TextBlob(text)
    res=Blob.sentiment
    if Blob.sentiment.polarity > 0:

        return 'positive'
    elif Blob.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'
    return res
