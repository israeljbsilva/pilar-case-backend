import pytest

from algorithms.vowel_count import get_vowel_count


@pytest.mark.parametrize('words, count', [("batman", 2), ("rObin", 2), ("coringA", 3)])
def test_must_get_vowel_count(words, count):
    vowel_count = get_vowel_count(words)
    assert vowel_count == count
