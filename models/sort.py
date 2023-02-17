from typing import Literal

from models.vowel_count import InputVowelCountModel


class InputSortModel(InputVowelCountModel):
    order: Literal['asc', 'desc']
