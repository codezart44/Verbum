import sqlite3

from verbum.api.utils.errors import SelectError, DeleteError, InsertError, UpdateError

#################### SINGLE RECORD ####################

def select_record(
        conn : sqlite3.Connection,
        parameters : tuple[str]
) -> tuple[str]:
    sql = """--sql
    SELECT * FROM en_entries AS a
    JOIN ON en_tags AS b
    WHERE a.entry_id = b.entry_id;
    """
    ...