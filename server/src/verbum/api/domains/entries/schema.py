from typing import TypedDict
from enum import StrEnum

from verbum.config import CONFIG
from verbum.api.utils.models import POS
from verbum.api.utils.validate import ParameterValidator

MAX_CHARACTERS = CONFIG["database"]["en"]["entries"]["max_characters"]
MIN_CHARACTERS = CONFIG["database"]["en"]["entries"]["min_characters"]

MAX_CHARACTERS_WORD = MAX_CHARACTERS["word"]
MAX_CHARACTERS_POS = MAX_CHARACTERS["pos"]
MAX_CHARACTERS_DESCRIPTION = MAX_CHARACTERS["description"]
MAX_CHARACTERS_TRANSLATION = MAX_CHARACTERS["translation"]

MIN_CHARACTERS_WORD = MIN_CHARACTERS["word"]
MIN_CHARACTERS_POS = MIN_CHARACTERS["pos"]
MIN_CHARACTERS_DESCRIPTION = MIN_CHARACTERS["description"]
MIN_CHARACTERS_TRANSLATION = MIN_CHARACTERS["translation"]

class _EntryTyping(TypedDict):
    word: str
    pos: str
    description: str
    translation: str

class EntryEnum(StrEnum):
    WORD = "word"
    POS = "pos"
    DESCRIPTION = "description"
    TRANSLATION = "translation"

class EntryFactory:
    def from_dict(data: dict[str, str]) -> _EntryTyping:
        entry: _EntryTyping = {
            "word": data.get("word").strip().lower(),
            "pos":  data.get("pos").strip().lower(),
            "description": data.get("description").strip(),
            "translation": data.get("translation").strip(),      
        }
        return entry
    
    def from_values(
            word : str,
            pos : str,
            description : str,
            translation : str,
    ) -> dict[str,str]:
        return {
            "word": word,
            "pos": pos,
            "description": description,
            "translation": translation,
        }
    
    def destruct(entry: dict[str, str]) -> tuple[str,str,str,str]:
        return (
            entry.get("word").lower().strip(), 
            entry.get("pos").lower().strip(), 
            entry.get("description").strip(), 
            entry.get("translation").strip(),
            )


class EntryParameterValidator(ParameterValidator):
    @classmethod
    def valid_word(cls, word: str):
        cls._max_characters(word, MAX_CHARACTERS_WORD, EntryEnum.WORD)
        cls._min_characters(word, MIN_CHARACTERS_WORD, EntryEnum.WORD)

    @classmethod
    def valid_pos(cls, pos: str):
        cls._allowed_value(pos, POS)
        cls._max_characters(pos, MAX_CHARACTERS_POS, EntryEnum.POS)
        cls._min_characters(pos, MIN_CHARACTERS_POS, EntryEnum.POS)
 
    @classmethod
    def valid_description(cls, description: str):
        cls._max_characters(description, MAX_CHARACTERS_DESCRIPTION, EntryEnum.DESCRIPTION)
        cls._min_characters(description, MIN_CHARACTERS_DESCRIPTION, EntryEnum.DESCRIPTION)

    @classmethod
    def valid_translation(cls, translation: str):
        cls._max_characters(translation, MAX_CHARACTERS_TRANSLATION, EntryEnum.TRANSLATION)
        cls._min_characters(translation, MIN_CHARACTERS_TRANSLATION, EntryEnum.TRANSLATION)

    @classmethod
    def valid_entry(cls,
        word : str,
        pos : str | None,
        description : str | None,
        translation : str | None,
    ):
        cls.valid_word(word)
        if pos is not None:
            cls.valid_pos(pos)
        if description is not None:
            cls.valid_description(description)
        if translation is not None:
            cls.valid_translation(translation)


# difference between class method and static method?? 