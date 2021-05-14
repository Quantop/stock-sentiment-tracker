import tweepy
import configparser
import pandas as pd

parser = configparser.RawConfigParser()
parserfilepath = r'config.ini'
parser.read(parserfilepath)

consumer_key = parser.get('twitter', 'consumer_key')
consumer_secret = parser.get('twitter', 'consumer_secret')

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)