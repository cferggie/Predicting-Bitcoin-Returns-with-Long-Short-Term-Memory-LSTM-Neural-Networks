import vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import re

#Read in Preprocessed tweets
OGdata = pd.read_csv(r'FILE PATH HERE')

tweets = OGdata.drop_duplicates(subset=['text'], keep='first') #remove duplicates

#Create function that cleans text
def cleanTxt(tweets):
    tweets = re.sub(r'@[A-Za-z0-9_]+', '', tweets) #Removes @ mentions
    tweets = re.sub(r'#', '', tweets) #Remove '#'
    tweets = re.sub(r'RT[\s]', '', tweets) #Removing RT
    tweets = re.sub(r'https?:\/\/\S+|www\.\S+', '', tweets) #Remove links
    tweets = re.sub(r'<.*?>', '', tweets) #Remove HTML code
    tweets = re.sub(r'[^ a-zA-Z0-9!.?,;]', '', tweets) #Removes special characters

    return tweets

#Clean the text
cleanedTweets = tweets['text'].apply(cleanTxt)


#Lets analyze some tweets
analyzer = SentimentIntensityAnalyzer()

def getPolarity(cleanedTweets):
    df = cleanedTweets

    #get compound polarity scores
    polarity = []
    for tweet in df:
        rawScore = analyzer.polarity_scores(text=tweet)
        polarity.append(rawScore['compound']) 
 
    #classify the scores
    posORneg = [] #positive or negative
    for score in polarity:
        if score > 0:
            posORneg.append(1)
        else: 
            posORneg.append(0)

    neutral = []
    for score in polarity:
        if score == 0:
            neutral.append(1)
        else:
            neutral.append(0)
    return (polarity, posORneg, neutral)

sentiment = getPolarity(cleanedTweets)
polarity = sentiment[0]
posORneg = sentiment[1]
neutral = sentiment[2]
# # print(polarity)
# print(posORneg)

data = {'Tweets': cleanedTweets,
        'Polarity Score': polarity,
        'Pos or Neg': posORneg,
        'Neutral': neutral} 

df = pd.DataFrame(data)
df = df.reset_index(drop=True)
print(df)
