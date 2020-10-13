from markov_chain import MarkovChain


markov_chain = MarkovChain()
text = ''

chain = markov_chain.chain(text)

print(chain)