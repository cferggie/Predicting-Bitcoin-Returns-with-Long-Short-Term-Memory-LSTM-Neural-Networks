#Imports

import re
import tweepy
import csv
import numpy as np
import pandas as pd
import random

#Twitter Access 

consumer_key = 'tmFvWrc2JvyTt7K0H46OzOp6y'
consumer_secret = 'ISI9p8wSILuWSpI6E2vUz6H0cYHUSwkwGfDVOkQ9EtKvUuKoBO'
access_token = '1504894041544081412-pkD3SKWd0LQebfIFE4QqSd3UJ0CzIQ'
access_token_secret = 'Vais2DY6aWxjCRsPm7xacBNbMX7fFPxyWVQVcITT5Qq82'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAJ6CaQEAAAAAUcOj7rKXas5tVBSCKiant0H0KbY%3DQ9vHbE2ShFNrFVKxPE1Pa9Om1JMssfzBMnCxSMZx0od7JLLhvz'

#Create API for use in any function and pass AUTH
client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret, bearer_token=bearer_token)

#Define the search (right now it only finds 10 tweets for testing)
searchList = "Bitcoin" or "BitCoin" or "BTC" or "btc" or "$BTC" or "$btc" or "bitcoin"

#Perform Search
response = client.search_recent_tweets(query=searchList, max_results=10, tweet_fields=["created_at","text"])

#Create object that holds the twitter data 
tweets = response.data

#Create a dataframe to hold tweets and save to csv
data = pd.DataFrame(data=[[tweet.created_at,tweet.text]for tweet in tweets], columns=['Date','Tweets'])
data.to_csv("CBT.csv")


