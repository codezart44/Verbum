import uuid
import sqlite3
from ..config import CONFIG

NAMESPACE_ENTRIES_EN  = uuid.UUID(CONFIG["database"]["en"]["entries"]["namespace"])
NAMESPACE_TAGS_EN     = uuid.UUID(CONFIG["database"]["en"]["tags"]["namespace"])
NAMESPACE_EXAMPLES_EN = uuid.UUID(CONFIG["database"]["en"]["examples"]["namespace"])
NAMESPACE_SYNONYMS_EN = uuid.UUID(CONFIG["database"]["en"]["synonyms"]["namespace"])
NAMESPACE_ANTONYMS_EN = uuid.UUID(CONFIG["database"]["en"]["antonyms"]["namespace"])
DATABASE_PATH = CONFIG["database"]["path"]

MAX_CHARACTERS_EXAMPLES = CONFIG["database"]["en"]["examples"]["max_characters"]


def get_connection() -> sqlite3.Connection:
    return sqlite3.connect(DATABASE_PATH)

def get_entry_id(word: str) -> str:
    return str(uuid.uuid5(NAMESPACE_ENTRIES_EN, word.strip().lower()))

def get_tag_id(tag: str) -> str:
    return str(uuid.uuid5(NAMESPACE_TAGS_EN, tag.strip().lower()))

def get_example_id(example: str) -> str:
    assert len(example) <= MAX_CHARACTERS_EXAMPLES, "Error: Example exceeded max characters allowed. "
    return str(uuid.uuid5(NAMESPACE_EXAMPLES_EN, example.strip().lower()))

