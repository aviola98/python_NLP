import nltk
#bigrams
from nltk import bigrams
#trigrams
from nltk import trigrams
#4 or more
from nltk import ngrams

corpus = open("corpus_teste.txt").read()
tokens = nltk.word_tokenize(corpus)

tokens_bigrams = list(bigram(tokens))
print(tokens_bigrams)

tokens_trigrams = list(trigrams(tokens))
print(tokens_trigrams)

tokens_ngrams = list(ngrams(tokens,4))
print(tokens_ngrams)

#recognizing named entities
bigramas = list(bigrams(tokens))
trigramas = list(trigrams(tokens))

for bigrama in bigramas:
    #checking if the first character of the first word and the first character of the second word are upper case
    if bigrama[0][0].isupper() and bigrama[1][0].isupper():
        print(bigrama)

#trigams
for trigrama in trigramas:
    if trigrama[0][0].isupper() and trigrama[1][0].isupper() and trigrama[2][0].isupper():
        print(trigrama)

#stemming
#lematização
stemmer = nltk.RSLPStemmer()

print(stemmer.stem("amigo"))
print(stemmer.stem("amigão"))
print(stemmer.stem("propõe"))
print(stemmer.stem("propuseram"))

#etiquetador

from nltk.corpus import mac_morpho
from nltk.tag import UnigramTagger

tokens = nltk.word_tokenize(corpus)
sentencas_treino = mac_morpho.tagged_sents()
etiquetador = UnigramTagger(sentencas_treino)

etiquetado = etiquetador.tag(tokens)
print(etiquetado)

#DefaultTagger
from nltk.corpus import mac_morpho
from nltk.tag import UnigramTagger
from nltk.tag import DefaultTagger

tokens = nltk.word_tokenize(corpus)
etiq_padrao = DefaultTagger('N')
sentencas_treino = mac_morpho.tagged_sents()
etiquetador = UnigramTagger(sentencas_treino, backoff = etiq_padrao)

etiquetado = etiquetador.tag(tokens)
print(etiquetado)

from nltk.chunk import RegexpParser
pattern = 'NP: (<NPROP><NPROP> | <N><N>)'
analise_gramatical = RegexpParser(pattern)

arvore = analise_gramatical.parse(etiquetando)
print(arvore)

