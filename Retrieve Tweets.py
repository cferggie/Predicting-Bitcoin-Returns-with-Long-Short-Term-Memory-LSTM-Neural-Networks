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
  This function will the scrape Twitter to retrieve the most recent tweets mentioning bitcoin. 
  The scrape will exclude any non-english tweets, retweets, or replies.
  '''
  
    #Define the search 
    searchWord = "Bitcoin"
    searchParam = searchList + ' lang:en' + ' -is:retweet' + ' -is:reply' 
 
    #Perform Search
    response = client.search_recent_tweets(query=searchParam, max_results=100, tweet_fields=["created_at","text"])

    #Grab the data from the search  
    tweets = response.data

    return tweets

#Create a loop to grab 6000 tweets per hour starting at 9:00am
startTime = datetime.time(9,0) #9am start time
stopTime = datetime.time(17 ,0) #5pm stop time

def scrapeLoop(startTime,stopTime):

    #Open a csv file to write tweets to 
    with open('tweets2.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        # Write the header row to the CSV file
        writer.writerow(['created_at', 'text'])

        # Start an infinite loop to fetch new tweets
        while True:
            #Initialize current time for checking 
            currentTime = datetime.datetime.now(timezone('EST')).time()

            if currentTime < startTime or currentTime > stopTime: # when to stop the infinite loop
                print('It is not time yet')
                break    

            try:
                #save tweets in an object from the getTweets function
                tweets = getTweets(client)

                #write each tweet to a csv
                for tweet in tweets:
                    writer.writerow([tweet.created_at, tweet.text])
                
                #wait for 50 seconds before searching again
                time.sleep(50) #i really want it to be a minute, but i reduced it to 50sec to give the 
                                # program time to do the search

            except tweepy.errors as e:
                print(f'Error: {e}')
                continue

scrapeLoop(startTime, stopTime)
