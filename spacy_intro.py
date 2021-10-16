#!python -m spacy download pt_core_news_lg
import spacy

text = ""
nlp = spacy.load("pr_core_news_lg")
doc = nlp(texto)

#tokenization

tokens = [token for token in doc]
print(tokens)
type(tokens[0])

#how to rescue a text from a token
tokens = [tokens.orth_ for token in doc]
tokens
#orth_ brings the text itself instead of the spacy representation

alpha_tokens = [token.orth_ for token in doc if token.is_alpha]
#generating a list containing the textual representation of the token of the list doc if and only if it is a character

print("alpha tokens: %s " % alpha_tokens)

#generating only numbers

digit_tokens = [token.orth_ for token in doc if token.is_digit]
print("digit tokens : %s" % digit_tokens)

#only punctuation

punct_tokens = [token.orth_ for token in  doc if token.is_punct]
print("punctation tokens: %s" % punct_tokens)

corpus = open("corpus_teste.txt").read()
corpus

doc = nlp(corpus)
tokens = [token.orth_ for token in doc]
tokens

alpha_tokens = [token.orth_ for token in doc if token.is_alpha]
#generating a list containing the textual representation of the token of the list doc if and only if it is a character

print("alpha tokens: %s " % alpha_tokens)

#generating only numbers

digit_tokens = [token.orth_ for token in doc if token.is_digit]
print("digit tokens : %s" % digit_tokens)

#only punctuation

punct_tokens = [token.orth_ for token in  doc if token.is_punct]
print("punctation tokens: %s" % punct_tokens)

lemmas = [token.lemma_ for token in doc if token.pos_=="VERB"]
lemmas 

#tuple 
#all tokens with their grammar class
pos = [(token.orth_ , token.pos_) for token in doc]
pos

#morfological information

morpho = [(token.orth_ , token.morph) for token in doc]
morpho

#named entities

entities = list(doc.ents)
print(entities)

#details entities

details_entities = [(entity, entity.label_), for entity in doc.entities]
details_entities

#display named entities

html = spacy.displacy.render(doc, style = "ent")
output_path = open("named_entities.html","w",encoding="utf-8")
output_path.write(html)
output_path.close()

#relationship between tokens

sintax = [(token.orth_ , token.dep_) for token in doc]
print(sintax)

#displaying sintax

visualize_sintax = spacy.displacy.render(doc, style = "dep")
output_path = open("dependency.svg","w",encoding="utf-8")
output_path.write(visualize_syntax)
output_path.close()