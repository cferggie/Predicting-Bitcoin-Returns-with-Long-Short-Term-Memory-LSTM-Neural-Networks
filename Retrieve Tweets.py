#Imports
import tweepy
import csv
import time
import datetime
from pytz import timezone

#Twitter Access 

consumer_key = 'KEY HERE'
consumer_secret = 'KEY HERE'
access_token = 'KEY HERE'
access_token_secret = 'KEY HERE'
bearer_token = 'KEY HERE'

#Create API for use in any function and pass AUTH
client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret, bearer_token=bearer_token)

def getTweets(client):
  ''' 
  This function will the scrape Twitter to retrieve the most recent tweets mentioning bitcoin and its various other nicknames. 
  The scrape will exclude any non-english tweets, retweets, or replies.
  '''
  
    #Define the search 
    searchList = "Bitcoin" or "BitCoin" or "BTC" or "btc" or "$BTC" or "$btc" or "bitcoin"
    newSearch = searchList + ' lang:en' + ' -is:retweet' + ' -is:reply'  #additional search filters
 
    #Perform Search
    response = client.search_recent_tweets(query=newSearch, max_results=100, tweet_fields=["created_at","text"])

    #Grab the data from the search  
    tweets = response.data

    return tweets

#Create a loop to grab 6000 tweets per hour starting at 9:00am
currentTime = datetime.datetime.now(timezone('EST')).time()
startTime = datetime.time(9,0) #9am start time

def scrapeLoop(startTime, currentTime):
  ''' 
  This function takes the current time and a designated start time (both in EST) to determine when start scrapping Twitter for tweets.
  You can change the start time using the startTime variable above.
  '''
  
    #Open a csv file to write tweets to 
    with open('tweets.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row to the CSV file
        writer.writerow(['created_at', 'text'])

        # Start an infinite loop to fetch new tweets
        while True:
            if currentTime < startTime or currentTime > datetime.time(17,0): # when to stop the infinite loop
                break

            try:
                #save tweets in an object from the getTweets function
                tweets = getTweets(client)

                #write each tweet to a csv
                for tweet in tweets:
                    writer.writerow([tweet.created_at, tweet.text])
                
                #wait for 60 seconds before searching again
                time.sleep(60)

            except tweepy.errors as e:
                print(f'Error: {e}')
                continue

scrapeLoop(startTime, currentTime) #Start grabbing tweets!!!

