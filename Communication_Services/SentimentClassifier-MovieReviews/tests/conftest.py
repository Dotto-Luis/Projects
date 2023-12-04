import nltk
import pytest


@pytest.fixture(scope="module")
def stop_words_list():
    stop_words = nltk.corpus.stopwords.words("english")

    yield stop_words
