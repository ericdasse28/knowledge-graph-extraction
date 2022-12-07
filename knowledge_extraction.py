import nltk

from nltk.tokenize import word_tokenize

nltk.download("punkt")


def get_entities_pair(sentence):
    """Get the subject and the object of a sentence. They represent entities of a potential
    graph

    Args:
        sentence (str): sentence

    Returns:
        tuple: entities pair
    """
    tokens = word_tokenize(sentence)
    return (tokens[0], tokens[-1])
