import re


def get_vowel_count(word: str) -> int:
    return len(re.sub('[^aeiou]', '', word.lower()))
