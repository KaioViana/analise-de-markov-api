from numpy import random


class MarkovChain:
    def chain(self, text, n=30):
        corpus = text.split()
        pairs = self.__make_pairs(corpus)
        word_dict = dict()


        for word_1, word_2 in pairs:
            word_dict.setdefault(word_1, []).append(word_2)
            
        first_word = random.choice(corpus)

        while first_word.islower():
            first_word = random.choice(corpus)
        
        chain = [first_word]

        for i in range(n):
            chain.append(random.choice(word_dict[chain[-1]]))

        return chain


    def __make_pairs(self, corpus):
        for i in range(len(corpus)-1):
            yield (corpus[i], corpus[i+1])
    