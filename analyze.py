from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import reticker

reddit_data = pd.read_csv('datasets/comments.csv', usecols=["comment"])
comments = reddit_data.comment.to_list()

analyzer = SentimentIntensityAnalyzer()
ticker_extractor = reticker.TickerExtractor()

scores = []
tickers = []
for comment in comments:
    sentiment_score = 0
    try:
        sentiment_score = sentiment_score + analyzer.polarity_scores(comment)['compound']
    except TypeError:
        sentiment_score = 0

    extracted_tickers = ticker_extractor.extract(comment)

    scores.append(sentiment_score)
    tickers.append(extracted_tickers)

reddit_data['sentiment score'] = scores
reddit_data['tickers'] = tickers

reddit_data.to_csv('datasets/simple_analysis.csv', index=True)