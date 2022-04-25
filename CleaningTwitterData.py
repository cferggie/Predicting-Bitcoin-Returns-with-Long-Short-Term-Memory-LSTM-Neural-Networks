#Imports
import pandas as pd
import numpy as np
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import *
from nltk.stem.wordnet import WordNetLemmatizer

#Read in Preprocessed tweets
tweets = pd.read_csv('CBT.csv', index_col=['Date', 'Tweets'])

#To check what is coming out of tweets
#Tweets that were tweeted at the same time are grouped together
#print(tweets)

#Start the cleaning process

