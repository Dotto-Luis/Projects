from typing import List

import numpy as np
from gensim.models.word2vec import Word2Vec


def vectorizer(
    corpus: List[List[str]], model: Word2Vec, num_features: int = 100
) -> np.ndarray:
    """
    This function takes a list of tokenized text documents (corpus) and a pre-trained
    Word2Vec model as input, and returns a matrix where each row represents the
    vectorized form of a document.

    Args:
        corpus : list
            A list of text documents that needs to be vectorized.

        model : Word2Vec
            A pre-trained Word2Vec model that will be used to vectorize the corpus.

        num_features : int
            The size of the vector representation of each word. Default is 100.

    Returns:
        corpus_vectors : numpy.ndarray
            A 2D numpy array where each row represents the vectorized form of a
            document in the corpus.
    """
    # TODO
    def get_vector(word):
        if word in model.wv:
            return model.wv[word]
        else:
            return np.zeros(num_features)

    corpus_vectors = []
    for doc in corpus:
        doc_vector = np.mean([get_vector(word) for word in doc], axis=0)
        corpus_vectors.append(doc_vector)

    return np.array(corpus_vectors)
    raise NotImplementedError
