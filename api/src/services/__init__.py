import tweepy
import os


class Twitter:
    def __init__(self):
        self.keys = os.environ['KEYS'].split()
        self.auth = tweepy.AppAuthHandler(self.keys[0], self.keys[1])
        
        self.api = tweepy.API(self.auth)


    def get_user_timeline_tweets(self, id):
        tweets = tweepy.Cursor(self.api.user_timeline, id=id, exclude_replies=True, include_rts=False, tweet_mode='extended').items()

        return [tweet.full_text for tweet in tweets]


    def get_public_tweets(self, q):
        tweets = tweepy.Cursor(self.api.search, q=f'{q} -filter:retweets', result_type='mixed', lang='pt-br',  tweet_mode='extended').items()

        return [tweet.full_text for tweet in tweets]