from src.text_normalizer import (
    expand_contractions,
    lemmatize_text,
    remove_accented_chars,
    remove_extra_new_lines,
    remove_extra_whitespace,
    remove_html_tags,
    remove_special_chars,
    remove_stopwords,
    stem_text,
)


def test_remove_html_tags():
    """Test for remove_html_tags."""

    doc_html = """
<br /><br />But with plague out there and the news being kept a secret,
the New Orleans PD starts a dragnet of the city's underworld.
"""
    good_html = """
But with plague out there and the news being kept a secret,
the New Orleans PD starts a dragnet of the city's underworld.
"""

    assert good_html == remove_html_tags(doc_html)


def test_stem_text():
    """Test for stem_text."""

    doc_stem = """
Where did he learn to dance like that?
His eyes were dancing with humor.
She shook her head and danced away.
"""
    good_stem = (
        "where did he learn to danc like that ? hi eye were danc with humor . "
        "she shook her head and danc away ."
    )

    assert good_stem == stem_text(doc_stem)


def test_lemmatize_text():
    """Test for lemmatize_text."""

    doc_lemma = "The striped bats are hanging on their feet for best"
    good_lemma = "the stripe bat be hang on their foot for good"

    assert good_lemma == lemmatize_text(doc_lemma)


def test_expand_contractions():
    """Test for expand_contractions."""

    doc_contractions = "I can't, because it doesn't work."
    good_contractions = "I cannot, because it does not work."

    assert good_contractions == expand_contractions(doc_contractions)


def test_remove_accented_chars():
    """Test for remove_accented_chars."""

    doc_accented = "Héllo, thís is an accented sénténce."
    good_accented = "Hello, this is an accented sentence."

    assert good_accented == remove_accented_chars(doc_accented)


def test_remove_special_chars():
    """Test for remove_special_chars."""

    doc_specials = (
        "hello? there A-Z-R_T(,**), world, welcome to python. "
        "this **should? the next line #followed- by@ an#other %million^ %%like $this."
    )
    good_specials = (
        "hello there AZRT world welcome to python this should the next "
        "line followed by another million like this"
    )

    assert good_specials == remove_special_chars(doc_specials)

    doc_digits = "abc123def456ghi789zero0 hello my friend number 10"
    good_digits = "abcdefghizero hello my friend number "

    assert good_digits == remove_special_chars(doc_digits, remove_digits=True)


def test_remove_stopwords(stop_words_list):
    """Test for remove_stopwords."""

    doc_stop = "He is a very good person"
    good_stop = "good person"

    assert good_stop == remove_stopwords(doc_stop, stopwords=stop_words_list)


def test_remove_extra_new_lines():
    """Test for remove_extra_new_lines."""

    doc_new_lines = """we
use
a
lot
of
lines"""
    good_new_lines = "we use a lot of lines"

    assert good_new_lines == remove_extra_new_lines(doc_new_lines)


def test_remove_extra_whitespace():
    """Test for remove_extra_whitespace."""

    doc_spaces = "Hello           my      dear          friend"
    good_spaces = "Hello my dear friend"

    assert good_spaces == remove_extra_whitespace(doc_spaces)
