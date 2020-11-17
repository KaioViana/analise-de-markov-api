class MarkovChain:
    def __init__(self, corpus):
        self.corpus_words, self.distinct_words, self.word_idx_dict = self.pre_processing(corpus)


    
    def pre_processing(self, corpus):
        # adicionando espaços entre cada token
        for spaced in ['.','-',',','!','?','(','—',')''.','-',',','!','?','(','—',')']:
            corpus = corpus.replace(spaced, ' {0} '.format(spaced))

        corpus_words = corpus.split() # lista de palavrask_words_idx_dict
        corpus_words = [word for word in corpus_words if word != ''] # limpando lista
        distinct_words = list(set(corpus_words)) # lista de palavras distintas
        word_idx_dict = {word: i for i, word in enumerate(distinct_words)}

        return corpus_words, distinct_words, word_idx_dict # tupla
    
    def train(self, k=1):
        from scipy.sparse import dok_matrix # para criação de matrizes esparsas


        sets_of_k_words = [' '.join(self.corpus_words[i:i+k]) for i, _ in enumerate(self.corpus_words)] # montando o conjunto de palavras
        print(sets_of_k_words)
        sets_count = len(list(set(sets_of_k_words))) # quantidade de valores únicos no conjunto
        distinct_sets_of_k_words = list(set(sets_of_k_words)) # lista de palavras distintas no conjunto
        k_words_idx_dict = {word: i for i, word in enumerate(distinct_sets_of_k_words)} 

        next_after_k_words_matrix = dok_matrix((sets_count, len(self.distinct_words))) # montando a matriz

        # preenchendo a matriz
        for i, word in enumerate(sets_of_k_words[:-k]):
            word_sequence_idx = k_words_idx_dict[word]
            next_word_idx = self.word_idx_dict[self.corpus_words[i+k]]
            next_after_k_words_matrix[word_sequence_idx, next_word_idx] += 1
        
        return next_after_k_words_matrix, k_words_idx_dict


    def sample_next_word_after_sequence(self, word_sequence, next_after_k_words_matrix, k_words_idx_dict, alpha=0):
        next_word_vector = next_after_k_words_matrix[k_words_idx_dict[word_sequence]]
        likelihoods = next_word_vector/next_word_vector.sum()
            
        return self.weighted_choice(self.distinct_words, likelihoods.toarray())
        

    def stochastic_chain(self, seed, next_after_k_words_matrix, k_words_idx_dict, chain_length=15, seed_length=1):
        current_words = seed.split(' ')

        if len(current_words) != seed_length:
            raise ValueError (f'número errado de palavras, é esperado {seed_length}')

        sentence = seed

        for _ in range(chain_length):
            sentence += ' '
            next_word = self.sample_next_word_after_sequence(' '.join(current_words), next_after_k_words_matrix, k_words_idx_dict, self.distinct_words)
            print(next_word)
            sentence += next_word
            current_words = current_words[1:] + [next_word]
            
        return sentence


    def weighted_choice(self, objects, weights):
        """ retorna um elemento aleatório da sequencia de objetos
        de acordo com seu peso (percentagem)"""

        import numpy as np
        import random
        from random import random


        weights = np.array(weights, dtype=np.float64)
        sum_of_weights = weights.sum()

        np.multiply(weights, 1/sum_of_weights, weights)
        weights = weights.cumsum()
        x = random()
        for i in range(len(weights)):
            if x < weights[i]:
                return objects[i]