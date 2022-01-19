import praw
from praw.models import MoreComments
import configparser
import pandas as pd

# parsing the config file for reddit login and subreddit information
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

posts_per_sub = parser.getint('options', 'posts_per_sub')
morecomments_limit = parser.getint('options', 'morecomments_limit')

# looping through subreddits and adding hot posts to list
for currentsub in subreddits:
    for post in reddit.subreddit(currentsub).hot(limit=posts_per_sub):
        posts.append([post.id, post.title, post.score, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
        postids.append(post.id)

posts = pd.DataFrame(posts,columns=['id', 'title', 'score', 'subreddit', 'url', 'num_comments', 'body', 'created'])
posts.to_csv('datasets/posts.csv', index=True)

# looping through the posts list to get comments from them, up to the morecomments limit
for id in postids:
    submission = reddit.submission(id)
    submission.comments.replace_more(limit=morecomments_limit)

    for comment in submission.comments.list():
        comments.append([comment.id, comment.parent_id, id, submission.title, comment.body])

comments = pd.DataFrame(comments,columns=['post_id', 'parent_id', 'id', 'title', 'comment'])
comments.to_csv('datasets/comments.csv', index=True)