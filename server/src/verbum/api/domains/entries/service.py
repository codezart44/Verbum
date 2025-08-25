import sqlite3

from verbum.api.utils.hashing import get_entry_id
from verbum.api.domains.entries.schema import EntryParameterValidator
from verbum.api.domains.entries import queries
from verbum.api.domains.entries.schema import EntryFactory
from verbum.api.utils.errors import *

class EntriesService:
    def insert_one(
            conn : sqlite3.Connection,
            entry : dict[str, str],
        ) -> int:
        (word, pos, description, translation) = EntryFactory.destruct(entry)
        EntryParameterValidator.valid_entry(word, pos, description, translation)
        entry_id = get_entry_id(word)

        parameters = (entry_id, word, pos, description, translation)
        queries.insert_entry(conn, parameters)
    

    def update_one(
            conn : sqlite3.Connection,
            entry : dict[str, str],
    ) -> int:
        parameters = (
            entry.get("pos").lower(),
            entry.get("description"),
            entry.get("translation"),
            get_entry_id(entry["word"])
        )
        return queries.update_entry(conn, parameters)
    
    def delete_one(
            conn : sqlite3.Connection,
            word : str,
    ) -> int:
        parameters = (get_entry_id(word),)
        return queries.delete_entry(conn, parameters)
    
    def select_one(
            conn : sqlite3.Connection,
            word : str,
    ) -> tuple[str, str, str, str]:
        parameters = (get_entry_id(word),)
        return queries.select_entry(conn, parameters)
    
    def insert_many(
            conn : sqlite3.Connection,
            entries : list[dict[str,str]]
        ) -> int:
        parameters = [(
            get_entry_id(e["word"]),
            e["word"],
            e.get("pos").lower(),
            e.get("description"),
            e.get("translation")
        ) for e in entries]
        return queries.insert_entries(conn, parameters)
    
    def update_many(
            conn : sqlite3.Connection,
            entries : list[dict[str,str]]
    ) -> int:
        parameters = [(
            e.get("pos").lower(),
            e.get("description"),
            e.get("translation"),
            get_entry_id(e["word"])
        ) for e in entries]
        return queries.update_entries(conn, parameters)
    
    def delete_many(
            conn : sqlite3.Connection,
            words : list[str],
    ) -> int:
        parameters = [(get_entry_id(w),) for w in words]
        return queries.delete_entries(conn, parameters)
    
    def select_all(
            conn : sqlite3.Connection,
    ) -> list[tuple[str, str, str, str]]:
        return queries.select_entries(conn)
    
    def select_randn(
            conn : sqlite3.Connection,
            n : int,
    ) -> list[tuple[str, str, str, str]]:
        return queries.select_entries_randn(conn, n)


    # word : str,
    # pos : str,
    # description : str,
    # translation : str,
    # parameters = (entry_id, word.lower(), pos, description, translation.lower())
