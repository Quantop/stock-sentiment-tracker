import praw
import configparser
import pandas as pd

parser = configparser.RawConfigParser()
parserfilepath = r'config.ini'
parser.read(parserfilepath)

client_id = parser.get('reddit-login', 'client_id')
client_secret = parser.get('reddit-login', 'client_secret')
user_agent = parser.get('reddit-login', 'user_agent')

subreddits = [sub.strip() for sub in parser.get('subreddits', 'subreddits').split(',')]

reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

posts = []

for currentsub in subreddits:
    for post in reddit.subreddit(currentsub).hot(limit=10):
        posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])

posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])