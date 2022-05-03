#Imports
import pandas as pd
import numpy as np
import re
import string

##This is all the preprocessing that is required before using VADER. Anything more does more harm than good in terms of having the most unbiased data. 

#Read in Preprocessed tweets
tweets = pd.read_csv('Preprocessed.csv')

#Remove all duplicate tweets (keep the first instance)
Dup_tweets = tweets[tweets.duplicated()]
Remove_dups = tweets.drop_duplicates(subset='Tweets', keep='first')

#Create function that cleans text
def cleanTxt(text):
    text = re.sub(r'@[A-Za-z0-9_]+', '', text) #Removes @ mentions
    text = re.sub(r'#', '', text) #Remove '#'
    text = re.sub(r'RT[\s]', '', text) #Removing RT
    text = re.sub(r'https?:\/\/\S+|www\.\S+', '', text) #Remove links
    text = re.sub(r'<.*?>', '', text) #Remove HTML code
    text = re.sub(r'[^ a-zA-Z0-9!.?,;]', '', text) #Removes special characters

    return text

#Clean the text
tweets['Tweets'] = tweets['Tweets'].apply(cleanTxt)
       
