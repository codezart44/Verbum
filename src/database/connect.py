import uuid
import sqlite3
from ..config import CONFIG

# VERBUM_NAMESPACE_SV = uuid.UUID("...")
VERBUM_NAMESPACE_EN = uuid.UUID(CONFIG["database"]["en"]["namespace"])
DATABASE_PATH = CONFIG["database"]["path"]


def get_connection() -> sqlite3.Connection:
    return sqlite3.connect(DATABASE_PATH)

def get_entry_id(word: str) -> uuid.UUID:
    return str(uuid.uuid5(VERBUM_NAMESPACE_EN, word.lower()))
