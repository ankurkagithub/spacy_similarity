
# importing spacy
import spacy

#loading NLP model for similiary check, different from 'en_core_web_sm'
#nlp = spacy.load('en_core_web_md')
nlp = spacy.load('en_core_web_sm')


word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
word4 = nlp("fish")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# Observations on similarities between cat, monkey and banana
'''
Cat and monkey are 59% approx similar, as both are animals and mammals.
Wherease cat and banana are 22% approx similar, in comparison to monkey and banana
which are 40% approx similar, as latter eats the fruit and link is more prescribed
where cat does not have such association.
'''

tokens = nlp("india brazil usa uk developing")
print("Similarity in tokens")
for token1 in tokens:
    for token2 in tokens:
        print(token1, token2, token1.similarity(token2))

# Observations on similarity using simple language model - 'en_core_web_sm'
'''
Using simple language model, now the USA and the UK have 27% approx and 22% approx.
wherease Brazil and India have approx 13% and 17% respectively.
'''
