import uuid
import sqlite3
from ..config import CONFIG

# VERBUM_NAMESPACE_SV = uuid.UUID("...")
NAMESPACE_ENTRIES_EN = uuid.UUID(CONFIG["database"]["en"]["entries"]["namespace"])
NAMESPACE_TAGS_EN    = uuid.UUID(CONFIG["database"]["en"]["tags"]["namespace"])
DATABASE_PATH = CONFIG["database"]["path"]


def get_connection() -> sqlite3.Connection:
    return sqlite3.connect(DATABASE_PATH)

def get_entry_id(word: str) -> uuid.UUID:
    return str(uuid.uuid5(NAMESPACE_ENTRIES_EN, word.lower()))

def get_tag_id(word: str, tag: str) -> uuid.UUID:
    return str(uuid.uuid5(NAMESPACE_TAGS_EN, f"{word.lower()}{tag.lower()}"))