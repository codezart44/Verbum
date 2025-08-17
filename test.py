import typing
from enum import StrEnum
from typing import TypedDict

class EntryTyping(TypedDict):
    word: str
    pos: str
    description: str
    translation: str

entry = {
    "word": "run",
    "pos": "verb"
}

class EntryEnum(StrEnum):
    WORD = "word"
    POS = "pos"
    DESCRIPTION = "description"
    TRANSLATION = "translation"

missing_fields = [e.value for e in EntryEnum if e not in entry.keys()]
print(missing_fields)


print(EntryEnum.WORD in entry)
print("word" in EntryEnum)
print(None in EntryEnum)

entry = typing.cast(EntryTyping, entry)


print([e.value for e in EntryEnum])

var = -1

match var:
    case 0: print("Good")
    case 1: print("Also Good")
    case _: print("BAD")