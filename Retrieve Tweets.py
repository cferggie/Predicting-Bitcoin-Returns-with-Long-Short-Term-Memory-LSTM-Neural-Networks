##This is the trial program, will update the amount of tweets it searches once the whole bot is built
#Imports

import re
import tweepy
import csv
import numpy as np
import pandas as pd
import random

#Twitter Access 

consumer_key = 'KEY HERE'
consumer_secret = 'KEY HERE'
access_token = 'KEY HERE'
access_token_secret = 'KEY HERE'
bearer_token = 'KEY HERE'

#Create API for use in any function and pass AUTH
client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret, bearer_token=bearer_token)

#Define the search (right now it only finds 10 tweets for testing)
searchList = "Bitcoin" or "BitCoin" or "BTC" or "btc" or "$BTC" or "$btc" or "bitcoin"

#Perform Search
response = client.search_recent_tweets(query=searchList, max_results=10, tweet_fields=["created_at","text"])

#Grab the data from the search  
tweets = response.data

#Create a dataframe to hold tweets and save to csv
data = pd.DataFrame(data=[[tweet.created_at,tweet.text]for tweet in tweets], columns=['Date','Tweets'])
data.to_csv("CBT.csv")


