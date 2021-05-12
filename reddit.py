import praw
from praw.models import MoreComments
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
postids = []
comments = []

for currentsub in subreddits:
    for post in reddit.subreddit(currentsub).hot(limit=2):
        posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
        postids.append(post.id)

posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])

for id in postids:
    submission = reddit.submission(id)
    submission.comments.replace_more(limit=5)

    for comment in submission.comments.list():
        comments.append([id, submission.title, comment.body])

comments = pd.DataFrame(comments,columns=['postid','title','comments'])