from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import reticker

# using 'reticker' to verify that a suspected ticker in a string is a valid ticker
# ensures that sentiment is only conducted on tickers that exist
def verify_tickers(tickers_list, ticker_data):
    verified = []
    ticker_data_set = set(ticker_data)

    for tickers in tickers_list:
        tickers_set = set(tickers)

        if tickers_set:
            verified.append(list(tickers_set & ticker_data_set))
        else:
            verified.append([])

    return verified

# compiles the positive sentiment percentage together to be used on visuals
# output order is [general sentiment, reddit sentiment, twitter sentiment]
def process_sentiment(reddit, twitter):
    general_sentiment = 0.0
    reddit_sentiment = 0.0
    twitter_sentiment = 0.0
    #ticker_sentiment = []

    reddit_row_count = 0
    twitter_row_count = 0

    for row in reddit['sentiment score']:
        if row != 0:
            reddit_row_count += 1
            reddit_sentiment += row

    for row in twitter['sentiment score']:
        if row != 0:
            twitter_row_count += 1
            twitter_sentiment += row

    return [(reddit_sentiment+twitter_sentiment)/(reddit_row_count+twitter_row_count)/2, reddit_sentiment/reddit_row_count, twitter_sentiment/twitter_row_count]

analyzer = SentimentIntensityAnalyzer()
ticker_extractor = reticker.TickerExtractor()

# calculates the sentiment on each comment made on reddit
reddit_data = pd.read_csv('datasets/comments.csv', usecols=["comment"])
comments = reddit_data.comment.tolist()
ticker_data = pd.read_csv('tickers.csv', usecols=["tickers"])
ticker_data = ticker_data.tickers.tolist()

reddit_scores = []
tickers = []
for comment in comments:
    sentiment_score = 0
    try:
        sentiment_score = sentiment_score + analyzer.polarity_scores(comment)['compound']
    except TypeError:
        sentiment_score = 0

    extracted_tickers = ticker_extractor.extract(comment)

    reddit_scores.append(sentiment_score)
    tickers.append(extracted_tickers)

verified_tickers = verify_tickers(tickers, ticker_data)

reddit_data['sentiment score'] = reddit_scores
reddit_data['tickers'] = verified_tickers


# calculates the sentiment on each comment made on reddit
twitter_data = pd.read_csv('datasets/tweets.csv', usecols=["text"])
tweets = twitter_data.text.tolist()

twitter_scores = []
twitter_tickers = []
for tweet in tweets:
    sentiment_score = 0
    try:
        sentiment_score = sentiment_score + analyzer.polarity_scores(tweet)['compound']
    except TypeError:
        sentiment_score = 0

    extracted_tickers = ticker_extractor.extract(tweet)

    twitter_scores.append(sentiment_score)
    twitter_tickers.append(extracted_tickers)

verified_tickers = verify_tickers(twitter_tickers, ticker_data)

twitter_data['sentiment score'] = twitter_scores
twitter_data['tickers'] = verified_tickers

# outputs the sentiment results to a datasheet
reddit_data.to_csv('datasets/simple_analysis_reddit.csv', index=True)
twitter_data.to_csv('datasets/simple_analysis_twitter.csv', index=True)

general_sentiment = process_sentiment(reddit_data, twitter_data)
print(general_sentiment)