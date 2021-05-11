import praw
import configparser

parser = configparser.RawConfigParser()
parserfilepath = r'config.ini'
parser.read(parserfilepath)

client_id = parser.get('reddit-login', 'client_id')
client_secret = parser.get('reddit-login', 'client_secret')
user_agent = parser.get('reddit-login', 'user_agent')

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)