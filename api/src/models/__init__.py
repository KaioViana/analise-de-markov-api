from services import Twitter
from utils import formatingText


class SearchModels:
    def __init__(self):
        self.twitter = Twitter()

    def search(self, category, search):
        if category == 'timeline':
            tweets = self.__timeline_tweets(search)
            text = formatingText.formatText(tweets)

            return {'text': text}
        elif category == 'public':
            tweets = self.__public_tweets(search)


            return tweets
        else:
            return None
    

    def __timeline_tweets(self, id):
        tweets = self.twitter.get_user_timeline_tweets(id)
        return ' '.join(tweets)


    def __public_tweets(self, q):
        ...