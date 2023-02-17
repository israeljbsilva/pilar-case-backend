from pydantic import BaseModel


class InputVowelCountModel(BaseModel):
    words: list[str]
