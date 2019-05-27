
import tweepy
from textblob import TextBlob

# authentication for access to twitter data

consumer_key = 'hdaUFMqwwKxDxyXAgVUuURGah'
consumer_secret = 'Kooem1R2n86dcOPhImnxwCO3XdVWE7HNJBk9zKUKmC3X5XvAR8'

access_token = '2840087461-9GDpnKvvbpXuqeeh9g2ydtFdF3ZfY3ruB6C4f7f'
access_token_secret = 'Ed42DV6tc4lx1TTDVZcYD1p8ORC6eSyf02tiqijtkK42T'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# list tweets filter by string (permission for last 30 days)

tweet_search_term = api.search('nasa')

for tweet in tweet_search_term:
    print(tweet.text)

    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
