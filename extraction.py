import tweepy
import csv
import re

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Set up Tweepy API connection
consumer_key = '5TDSE4D0bvOGRLsAGQjRTFdxa'
consumer_secret = 'xw5Ll6WLEp9ptRNPprIWE8n2jqEiO21h71CEQYWDYpWzNdu1kN'
access_token = '265195902-mSPaW59D6ZwGlZQDo9oS8EsGJGvXSG5GIf8pqghZ'
access_token_secret = '7JGPgjJe4XBN7v5iRXBf1kOu9CA1PWvD3JHrMV1QD7bme'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Define a function to clean the tweet text
def clean_tweet_text(tweet):
    # Remove URLs and mentions from the tweet text
    clean_tweet = re.sub(r'http\S+', '', tweet)
    clean_tweet = re.sub(r'http\S+', '', clean_tweet)
    clean_tweet = re.sub("@[A-Za-z0-9_]+","",clean_tweet)
    clean_tweet = re.sub("#[A-Za-z0-9_]+","",clean_tweet)
    # Remove special characters and extra whitespace
    clean_tweet = re.sub(r'[^\w\s]', '', clean_tweet)
    clean_tweet = re.sub(r'\s+', ' ', clean_tweet)
    return clean_tweet.strip()

# Define a function to get the sentiment of a tweet
def get_tweet_sentiment(tweet):
    # Use VADER sentiment analyzer on the cleaned tweet text
    sentiment = analyzer.polarity_scores(tweet)
    # Classify the tweet as happy, sad, or neutral based on the compound score
    if sentiment['compound'] >= 0.6:
        return 'very happy'
    elif 0.2 <= sentiment['compound'] < 0.6:
        return 'happy'
    elif -0.2 <= sentiment['compound'] < 0.2:
        return 'neutral'
    elif -0.6 <= sentiment['compound'] < -0.2:
        return 'sad'
    else:
        return 'very sad'

# Define a list of Twitter accounts to analyze
accounts = ['bbcnews','BillGates','elonmusk']

# Analyze the sentiment of the latest 1000 tweets from each account and write the result to a CSV file
with open('sentiment_analysis.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['tweet', 'sentiment']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for account in accounts:
        tweets = tweepy.Cursor(api.user_timeline,
                               screen_name=account,
                               tweet_mode='extended').items(10000)
        for tweet in tweets:
            cleaned_tweet = clean_tweet_text(tweet.full_text)
            sentiment = get_tweet_sentiment(cleaned_tweet)
            writer.writerow({'tweet': cleaned_tweet, 'sentiment': sentiment})
