import tweepy
import os


class Twitter:
    def __init__(self):
        self.keys = os.environ['KEYS'].split()
        self.auth = tweepy.AppAuthHandler(self.keys[0], self.keys[1])
        
        self.api = tweepy.API(self.auth)

    # teste de conexão
    def public_tweets(self):
        tweets = tweepy.Cursor(self.api.search, q='python', lang='pt-br').items(10)

        for tweet in tweets:
            print(tweet.user.name, end='\n')