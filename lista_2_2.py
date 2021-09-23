import nltk

#open corpus 

infile = open("corpus_texte.txt","r")
texto = infile.read()

#tokenize the text
nltk.word_tokenize(texto)

#verify length

len(nltk.word_tokenize(texto))

#tokenize without numbers and pontuation

from nltk import RegexpTokenizer as regex

tokenizer = regex(r'[A-z]\w*')
tokens = tokenizer.tokenize(texto)
tokens

#verify length

len(tokens)

#check the frequence

frequence = nltk.FreqDist(tokens)
frequence.most_common

#check  the fifth , tenth and fifteenth most frequent words

fifth = frequence.most_common()[4]
tenth = frequence.most_common()[9]
fifteenth = frequence.most_common()[14]

print("the fifth most frequente word is: ", fifth,
"the tenth most frequent word is: ", tenth,
"the fifteenth most common word is: ", fifteenth)

#remove stopwords from nltk

stopwords = nltk.corpus.stopwords.words('portuguese')
print(stopwords)

#check frequence without stopwords

#removing all non letter strings
tokenizer = regex(r'[A-z]\w*')
#tokenizing the text
tokens = tokenizer.tokenize(texto)
#removing stopwords
stopwords = nltk.corpus.stopwords.words('portuguese')
tokens_without_stopwords = [w.lower() for w in tokens if w not in stopwords]
#checking frequence
frequence = nltk.FreqDist(tokens_without_stopwords)
#storing the most common words
mais_comuns = frequence.most_common()  
#printing the most common words without stopwords     
print(mais_comuns)