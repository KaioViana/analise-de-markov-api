from numpy import random


class MarkovChain:
    # def chain(self, text, n=30):
    #     corpus = text.split()
    #     pairs = self.__make_pairs(corpus)
    #     word_dict = dict()


    #     for word_1, word_2 in pairs:
    #         word_dict.setdefault(word_1, []).append(word_2)
            
    #     first_word = random.choice(corpus)

    #     while first_word.islower():
    #         first_word = random.choice(corpus)
        
    #     chain = [first_word]

    #     for i in range(n):
    #         chain.append(random.choice(word_dict[chain[-1]]))

    #     return chain


    # def __make_pairs(self, corpus):
    #     for i in range(len(corpus)-1):
    #         yield (corpus[i], corpus[i+1])

    def pre_processing(self, corpus):
        for spaced in ['.','-',',','!','?','(','—',')''.','-',',','!','?','(','—',')']:
            corpus = corpus.replace(spaced, ' {0} '.format(spaced))
        corpus_words = corpus.split()
        corpus_words = [word for word in corpus_words if word != '']

        distinct_words = list(set(corpus_words))

        return corpus_words, distinct_words
    
    def train(self, corpus_words, distinct_words, k=2):
        from scipy.sparse import dok_matrix # para criação de matrizes esparsas


        sets_of_k_words = [' '.join(corpus_words[i:i+k]) for i, _ in enumerate(corpus_words[:-k])] # montando o conjunto de palavras
        sets_count = len(list(set(sets_of_k_words))) # quantidade de valores únicos no conjunto

        next_after_k_words_matrix = dok_matrix((sets_count, len(distinct_words))) # montando a matriz

