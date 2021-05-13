from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import reticker

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


reddit_data = pd.read_csv('datasets/comments.csv', usecols=["comment"])
comments = reddit_data.comment.tolist()
ticker_data = pd.read_csv('tickers.csv', usecols=["tickers"])
ticker_data = ticker_data.tickers.tolist()

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

verified_tickers = verify_tickers(tickers, ticker_data)

reddit_data['sentiment score'] = scores
reddit_data['tickers'] = verified_tickers

reddit_data.to_csv('datasets/simple_analysis.csv', index=True)