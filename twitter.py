import tweepy
import configparser
import pandas as pd

parser = configparser.RawConfigParser()
parserfilepath = r'config.ini'
parser.read(parserfilepath)

consumer_key = parser.get('twitter', 'consumer_key')
consumer_secret = parser.get('twitter', 'consumer_secret')
access_token = parser.get('twitter', 'access_token')
access_secret = parser.get('twitter', 'access_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# verifying that the credentials are valid from config file
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# gathering tweets from list of tickers
tickers_list = pd.read_csv('tickers.csv', usecols=["tickers"])
tickers_list = tickers_list.tickers.tolist()

for ticker in tickers_list:
    tweets = api.search(q=ticker)
    
    for x in tweets:
        print(x.text)