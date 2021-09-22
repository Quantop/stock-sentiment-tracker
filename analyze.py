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
def process_sentiment(sentiment_datatable):
    general_sentiment = 0.0
    #reddit_sentiment = 0.0 Add this later once twitter and news sentiment is taken
    #ticker_sentiment = []

    row_count = 0

    for row in sentiment_datatable['sentiment score']:
        if row != 0:
            row_count += 1
            general_sentiment += row

    return general_sentiment/row_count

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

general_sentiment = process_sentiment(reddit_data)