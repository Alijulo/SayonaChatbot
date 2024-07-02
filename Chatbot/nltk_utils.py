import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from collections import Counter

lemmantizer=WordNetLemmatizer()
def tokenize(sentence):
    return nltk.tokenize.word_tokenize(sentence)

def lemmantize(word):
    return lemmantizer.lemmatize(word.lower())

def bag_of_words(tokenized_sentence,all_words):
    tokenized_sentence=[lemmantize(w) for w in tokenized_sentence]
    bag=np.zeros(len(all_words),dtype=np.float32)
    word_counts=Counter(tokenized_sentence)
    for indx,w in enumerate(all_words):
        if w in word_counts:
            bag[indx]=word_counts[w]

    return bag