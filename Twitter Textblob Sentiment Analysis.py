from textblob import TextBlob
import tweepy
from textblob.sentiments import NaiveBayesAnalyzer
#imports the textblob, tweeoy, and naivebayesanalyzer libraries into python.

client_key = 'WWFET0NXMDQ0QmtWWUJYeWJVSTY6MTpjaQ'
client_secret = 'OljY4fcsoSTpgwVuEfj6VmcKMYrdUCFBGqwSDB5IIDGjc7LtMs'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAIG7bQEAAAAAIUKCrMKGNhLpM6vtBfcVe6kEfbE%3DiPfA43afxdXDGiX9SyPrpdQAyJvYhjw2zNtQhA3iKjfX9t2dJZ'
access_token = '1512862494603177985-7JTpWhMVkd47rptkRUmayZTZBt2sCF'
access_secret = 'FXiXpqhsCIUWtNisqmejuJLNFFytrzifIiDPXmFxJv7RI'
#Created keys from the twitter developer portal to use in the client.

client = tweepy.Client(
    bearer_token,
    client_key,
    client_secret,
    access_token,
    access_secret,
    wait_on_rate_limit=False
)
#Establishes and initializes the client using the keys and tokens to authenticate the user with the bearer token.

query='war'
response = client.search_recent_tweets(query, max_results=100)
#Client.search searches for the most recent tweets in the last 7 days based on the term in the query.

counter=0
totalP=0
totalS=0 
temp_tweet=""
tweets = response.data
for tweet in tweets:
    blob_object = TextBlob(tweet.text, analyzer=NaiveBayesAnalyzer())
    currP = blob_object.polarity
    currS = blob_object.subjectivity
    totalP=totalP + currP
    totalS=totalS + currS
    counter+=1
#Gets the tweets from the response.data and does a sentiment analysis on the twitter statements.
#It then makes a loop which adds the calculated polarity and subjectivity to the variable counter 

#Once it divided the polarity and subjectivity by the counter, it prints the polarity and subjectivity of 100 tweets.
P_analysis = totalP/counter
S_analysis = totalS/counter
print('The Polarity for the tweets is: ' + str(P_analysis))
print('The Subjectivity for the tweets is: ' + str(S_analysis))
#print(counter)
#print(totalP)
#print(totalS)