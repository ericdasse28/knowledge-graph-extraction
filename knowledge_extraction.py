import nltk

from nltk.tokenize import word_tokenize

nltk.download("punkt")


def get_entity_pairs(sentence):
    tokens = word_tokenize(sentence)
    return (tokens[0], tokens[-1])
