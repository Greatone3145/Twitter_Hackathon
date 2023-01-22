from textblob import TextBlob
import tweepy
import string
import emoji
import datetime
from datetime import timedelta
import yfinance as yf
import re


def no_emoji(text):
    allchars = [str for str in text]
    emoji_list = [c for c in allchars if c in emoji.EMOJI_DATA]
    clean_text = ' '.join(
        [str for str in text.split() if not any(i in str for i in emoji_list)])

    return clean_text


consumer_key = "FewvGUWFzxX8R4FXdf9TKy7ig"
consumer_secret = "waLdoXNol4BuQnvi8qVSVtMcLRl1Hj1POL2ZpLdiaFBXj9bK5e"
access_token = "3106169722-sSXsSczGL6wm23ANJxS3lhIlvDHRcFXEaLDUxgi"
access_token_secret = "ynUelweUWnjPBBAdQyGwZIx0UCssy5sR8AkvMbDT6skga"

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)
api = tweepy.API(auth)


client = tweepy.Client(
    bearer_token='AAAAAAAAAAAAAAAAAAAAADcYlAEAAAAATA%2Blu1tuJRznRiJ8GRvye1vwUNc%3DwBUaJMesT8CZGxZVBHy3YWzaT7aNlldCa40C1hEUVjbbzqiQqx')


# initializing values
polarity = 0
date_since = datetime.datetime.now() - timedelta(days=7)
replied = []
q = 'TSLA'

for tweet in tweepy.Paginator(client.search_recent_tweets, query=q, tweet_fields=['context_annotations', 'created_at', 'public_metrics'], max_results=10).flatten(limit=10):
    text = tweet.text

    # removing links
    text = re.sub(r"http\S+", "", text)

    # removing @ and RT
    text = text.replace('RT', '')
    if text.startswith(' @'):
        position = text.index(':')
        text = text[position+2:]
    if text.startswith('@'):
        position = text.index(' ')
        text = text[position+2:]

    # removing emoji and puctuation
    text = no_emoji(text)
    text = text.translate(str.maketrans('', '', string.punctuation))

    # print(tweet.favorite_count)

    # sentiment analysis
    analysis = TextBlob(text)
    polarity = analysis.polarity

    # print(tweet.favorite_count)

    # initializing the date
    tweet_date = tweet.created_at.date()

    # pulling the stock prices for the tweet date
    stock_info = yf.download("TSLA", start=tweet_date, end=tweet_date)
    open_price = stock_info['Open'][0]
    close_price = stock_info['Close'][0]

    # initializing the variables for the ML
    price_movement = close_price - open_price
    success = 0

    # determining success
    if (price_movement >= 0) and (polarity >= 0):
        success = 1
    elif (price_movement <= 0) and (polarity <= 0):
        success = 1
    else:
        success = 0

    # things to use
    # q, polarity, success, tweet.public_metrics['like_count'], price_movement

    # printing the final text
    # print(text)
    # print('----------------------------')
