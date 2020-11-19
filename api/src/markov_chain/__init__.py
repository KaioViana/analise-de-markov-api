class MarkovChain:
    def __init__(self, corpus):
        """ Inicializa a classe já com o pré processamento da entrada de dados.
        Retorna três valores: corpus_words, distinct_words e word_idx_dict.
        Que serão usados durante o restante do processo. """

        # pre-processamento do texto de entrada
        self.corpus_words, self.distinct_words, self.word_idx_dict = self.pre_processing(corpus)


    def pre_processing(self, corpus):
        """ Recebe o texto de entrada, limpa e estrutara ele de maneira para manipular
        durante o processo.
            :param corpus: texto de entrada.
            :return: corpus_words: lista de tokens, distinct_words: lista de tokens únicos,
                    word_idx_dict: dicionário palavra:índice. """

        # adicionando espaços entre cada token
        for spaced in ['.','-',',','!','?','(','—',')''.','-',',','!','?','(','—',')']:
            corpus = corpus.replace(spaced, ' {0} '.format(spaced))

        corpus_words = corpus.split() # lista de palavras
        corpus_words = [word for word in corpus_words if word != ''] # limpando lista
        distinct_words = list(set(corpus_words)) # lista de palavras distintas
        word_idx_dict = {word: i for i, word in enumerate(distinct_words)} # dicionário de palavra:índice

        return corpus_words, distinct_words, word_idx_dict # tupla
    
    def train(self, k=1):
        """ Treinamento do algorítmo. 
            :param k: quantidade de palavras que a cadeia vai considerar antes de prever a próxima. 
            : return: next_after_k_words_matrix: matriz de palavras, k_words_idx_dict: dicionário de chaves (palavra:índice). """

        from scipy.sparse import dok_matrix # para criação de matrizes esparsas


        sets_of_k_words = [' '.join(self.corpus_words[i:i+k]) for i, _ in enumerate(self.corpus_words)] # montando o conjunto de palavras
        sets_count = len(list(set(sets_of_k_words))) # quantidade de valores únicos no conjunto
        distinct_sets_of_k_words = list(set(sets_of_k_words)) # lista de palavras distintas no conjunto
        k_words_idx_dict = {word: i for i, word in enumerate(distinct_sets_of_k_words)} # dicionário de sequência:índice

        next_after_k_words_matrix = dok_matrix((sets_count, len(self.distinct_words))) # montando a matriz

        # preenchendo a matriz
        for i, word in enumerate(sets_of_k_words[:-k]):
            word_sequence_idx = k_words_idx_dict[word]
            next_word_idx = self.word_idx_dict[self.corpus_words[i+k]]
            next_after_k_words_matrix[word_sequence_idx, next_word_idx] += 1
        
        return next_after_k_words_matrix, k_words_idx_dict


    def sample_next_word_after_sequence(self, word_sequence, next_after_k_words_matrix, k_words_idx_dict, alpha=0):
        """Retorna a próxima palavra de acordo com a sua probabilidade de ocorrência.
            :param word_sequence: Estado inicial da cadeia
            :param next_after_k_words_matrix: matriz de tokens
            :param k_words_idx_dict: dicionário de chaves (palavra:índice)
            :param alpha: 'criatividade' da cadeia 
            :return: próxima palavra da sequência """

        next_word_vector = next_after_k_words_matrix[k_words_idx_dict[word_sequence]] + alpha # buscando posicão da sequência na matriz
        likelihoods = next_word_vector/next_word_vector.sum() # sua probabilidade
            
        return self.weighted_choice(self.distinct_words, likelihoods.toarray())
        

    def stochastic_chain(self, seed, next_after_k_words_matrix, k_words_idx_dict, chain_length=15, seed_length=1):
        """ Gera uma sequência de texto.
                :param seed: entrada de texto representando o estado atual da cadeia
                :param next_after_k_words_matrix: matriz de tokens
                :param k_words_idx_dict: dicionário de chaves (palavra:índice)
                :param chain_length: tamanho da cadeia
                :param seed_length: tamanho da entrada """

        current_words = seed.split(' ')

        if len(current_words) != seed_length:
            raise ValueError (f'número errado de palavras, é esperado {seed_length}')

        sentence = seed

        for _ in range(chain_length-1):
            sentence += ' '
            next_word = self.sample_next_word_after_sequence(' '.join(current_words), next_after_k_words_matrix, k_words_idx_dict)
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