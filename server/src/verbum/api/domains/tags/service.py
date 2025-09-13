import sqlite3
from typing import Collection

from verbum.api.utils.hashing import get_entry_id, get_tag_id
from verbum.api.domains.tags.schema import TagParameterValidator
from verbum.api.domains.entries.schema import EntryParameterValidator
from verbum.api.domains.tags.schema import TagFactory
from verbum.api.domains.tags import queries


def select_tags_by_word(
        conn : sqlite3.Connection,
        word : str
    ) -> tuple[str]:
    EntryParameterValidator.valid_word(word)
    parameters = (get_entry_id(word),)
    tags = queries.select_word_tags(conn, parameters)
    return tags

# def select_words_by_tag

def insert_tags_by_word(
        conn : sqlite3.Connection,
        word : str,
        tags : Collection[str]
    ):
    EntryParameterValidator.valid_word(word)
    TagParameterValidator.valid_tags(tags)
    entry_id = get_entry_id(word)
    parameters = [(entry_id, get_tag_id(tag), word.lower(), tag.lower()) for tag in tags]
    queries.insert_tags(conn, parameters)

# def delete_tags_by_word

# def delete_all_by_word



# def delete_tag_kind

# def update_tag_kind

