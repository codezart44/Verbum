import uuid
import tomllib
import pprint

from connect import c
from config import CONFIG


VERBUM_NAMESPACE_EN = uuid.UUID(CONFIG["database"]["en"]["namespace"])
# VERBUM_NAMESPACE_SV = uuid.UUID("...")

def insert_entry(
        word : str, 
        description : str, 
        translation : str,
    ) -> None:
    word = word.lower()
    translation = translation.lower()

    entry_id = str(uuid.uuid5(VERBUM_NAMESPACE_EN, word))
    parameters = (entry_id, word, description, translation)

    sql = """--sql
    INSERT INTO en_entries ([entry_id], [word], [description], [translation]) 
    VALUES (?, ?, ?, ?);
    """
    c.execute(sql, parameters)

def main():
    insert_entry("test", "this is a test", "test")
    pass

if __name__=="__main__":
    main()