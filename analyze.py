from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

reddit_data = pd.read_csv('datasets/comments.csv', usecols=["comment"])
comments = reddit_data.comment.to_list()

analyzer = SentimentIntensityAnalyzer()

scores = []
for comment in comments:
    sentiment_score = 0
    try:
        sentiment_score = sentiment_score + analyzer.polarity_scores(comment)['compound']
    except TypeError:
        sentiment_score = 0

    scores.append(sentiment_score)

reddit_data['sentiment score'] = scores

reddit_data.to_csv('datasets/simple_analysis.csv', index=True)