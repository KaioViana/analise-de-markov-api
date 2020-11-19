from services import Twitter
from utils import formatingText
from numpy import random
from markov_chain import MarkovChain


class SearchModels:
    def __init__(self):
        self.twitter = Twitter()


    def search(self, category, search):
        if category == 'timeline':
            tweets = self.__timeline_tweets(search)
            text = formatingText.formatText(tweets)

            # trabalhando com a cadeia de Markov
            mkv = MarkovChain(text)
            k = 2 # quantidade de palavras a se considerar antes de prever a próxima

            # escolhendo aleatóriamente uma sequêcia para representar o estado atual da cadeia
            while True:
                word = random.choice(mkv.corpus_words)
                if word.istitle():
                    index = mkv.corpus_words.index(word)
                    seed = ' '.join(mkv.corpus_words[index:index+k])
                    break
            
            next_after_k_words_matrix, k_words_idx_dict = mkv.train(k) # treinando
            
            # gerando a cadeia
            chain = mkv.stochastic_chain(seed, next_after_k_words_matrix, k_words_idx_dict, chain_length=120, seed_length=k)
            
            return {'text': chain}
        elif category == 'public':
            tweets = self.__public_tweets(search)
            text = formatingText.formatText(tweets)

            # trabalhando com a cadeia de Markov
            mkv = MarkovChain(text)
            k = 2 # quantidade de palavras a se considerar antes de prever a próxima

            # escolhendo aleatóriamente uma sequêcia para representar o estado atual da cadeia
            while True:
                word = random.choice(mkv.corpus_words)
                if word.istitle():
                    index = mkv.corpus_words.index(word)
                    seed = ' '.join(mkv.corpus_words[index:index+k])
                    break
            
            next_after_k_words_matrix, k_words_idx_dict = mkv.train(k) # treinando
            
            # gerando a cadeia
            chain = mkv.stochastic_chain(seed, next_after_k_words_matrix, k_words_idx_dict, chain_length=120, seed_length=k)
            
            return {'text': chain}
        else:
            return None
    

    def __timeline_tweets(self, id):
        tweets = self.twitter.get_user_timeline_tweets(id)
        return ' '.join(tweets)


    def __public_tweets(self, q):
        tweets = self.twitter.get_public_tweets(q)
        return ' '.join(tweets)