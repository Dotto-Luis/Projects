from unittest.mock import Mock

import gensim.downloader as api
import numpy as np

from src import word2vec


def test_vectorizer():
    word_vectors = api.load("glove-wiki-gigaword-50")

    vector1 = word_vectors["personal"]
    vector2 = word_vectors["computer"]

    model = Mock()
    model.wv = word_vectors

    avg = word2vec.vectorizer([["personal", "computer"]], model, 50)[0]

    assert np.allclose(
        (vector1 + vector2) / 2, avg
    ), "You should check your vectorizer!"
