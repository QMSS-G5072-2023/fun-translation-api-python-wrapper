import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from python_funtranslation import python_funtranslation


@pytest.mark.parametrize("sentence1, sentence2, expected", [
    ("Hello world", "Hello world", 1.0),  # Identical sentences
    ("Hello world", "Hola mundo", 0.0),   # Completely different sentences
])
def test_sentence_similarity(sentence1, sentence2, expected):
    result = python_funtranslation.sentence_similarity(sentence1, sentence2)
    assert result == pytest.approx(expected)


@pytest.mark.parametrize("language, expected", [
    ("leetspeak", "Convert"), ("post-modern", "Convert"),
    ("a", "no desc")
])
def test_get_full_description(language, expected):
    result = python_funtranslation.get_full_description(language = language)
    assert result[:7] == expected

