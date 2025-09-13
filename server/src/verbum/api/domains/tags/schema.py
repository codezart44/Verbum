from typing import TypedDict, Collection
from enum import StrEnum

from verbum.config import CONFIG
from verbum.api.utils.validate import ParameterValidator

CONFIG_TAGS = CONFIG["database"]["en"]["tags"]
MAX_RECORDS = CONFIG_TAGS["max_records"]
MAX_CHARACTERS = CONFIG_TAGS["max_characters"]
MIN_CHARACTERS = CONFIG_TAGS["min_characters"]

class _TagRecord(TypedDict):
    word: str
    tag: str

class TagEnum(StrEnum):
    WORD = "word"
    TAG = "tag"

class TagFactory():
    def from_values(
            word: str,
            tags: Collection[str]
        ) -> list[_TagRecord]:
        tag_records: _TagRecord = [{"word": word, "tag": tag} for tag in tags]
        return tag_records

class TagParameterValidator(ParameterValidator):
    @classmethod
    def valid_tag(cls, tag: str):
        cls._max_characters(tag, MAX_CHARACTERS, TagEnum.TAG)
        cls._min_characters(tag, MIN_CHARACTERS, TagEnum.TAG)
    
    @classmethod
    def valid_tags(cls, tags: Collection[str]):
        cls._max_records(tags, MAX_RECORDS, TagEnum.TAG)
        for tag in tags:
            cls.valid_tag(tag)

