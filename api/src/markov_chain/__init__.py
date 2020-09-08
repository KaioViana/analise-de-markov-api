from numpy import random


class MarkovChain:
    def __init__(self, text):
        self.corpus = text.split()
        self.pairs = self.make_pairs(self.corpus)
        self.word_dict = dict()
   

    def make_pairs(self, corpus):
        for i in range(len(corpus)-1):
            yield (corpus[i], corpus[i+1])
    

    def chain(self, n=30):
        for word_1, word_2 in self.pairs:
            if word_1 in self.word_dict.keys():
                self.word_dict[word_1].append(word_2)
            else:
                self.word_dict[word_1] = [word_2]

        first_word = random.choice(self.corpus)

        while first_word.islower():
            first_word = random.choice(self.corpus)
        
        chain = [first_word]

        for i in range(n):
            chain.append(random.choice(self.word_dict[chain[-1]]))

        return chain