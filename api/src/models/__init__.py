from services import Twitter
from utils import formatingText
from markov_chain import MarkovChain


class SearchModels:
    def __init__(self):
        self.twitter = Twitter()
        self.markov_chain = MarkovChain()

    def search(self, category, search):
        if category == 'timeline':
            tweets = self.__timeline_tweets(search)
            text = formatingText.formatText(tweets)
            chain = self.markov_chain.chain(text, 150)

            return {'text': ' '.join(chain)}
        elif category == 'public':
            tweets = self.__public_tweets(search)
            text = formatingText.formatText(tweets)
            chain = self.markov_chain.chain(text, 150)

            return {'text': ' '.join(chain)}
        else:
            return None
    

    def __timeline_tweets(self, id):
        tweets = self.twitter.get_user_timeline_tweets(id)
        return ' '.join(tweets)


    def __public_tweets(self, q):
        tweets = self.twitter.get_public_tweets(q)
        return ' '.join(tweets)