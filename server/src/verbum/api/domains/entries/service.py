import sqlite3

from verbum.api.utils.hashing import get_entry_id
from verbum.api.domains.entries.schema import EntryParameterValidator
from verbum.api.domains.entries.schema import EntryFactory
from verbum.api.domains.entries import queries

class EntriesService:

    def select_one(
            conn : sqlite3.Connection,
            word : str,
        ) -> tuple[str, str, str, str]:
        EntryParameterValidator.valid_word(word)
        parameters = (get_entry_id(word),)
        (word, pos, description, translation) = queries.select_entry(conn, parameters)
        entry = EntryFactory.from_values(word, pos, description, translation)
        return entry
    
    def delete_one(
            conn : sqlite3.Connection,
            word : str,
        ):
        EntryParameterValidator.valid_word(word)
        parameters = (get_entry_id(word),)
        queries.delete_entry(conn, parameters)
    
    def insert_one(
            conn : sqlite3.Connection,
            entry : dict[str, str],
        ):
        (word, pos, description, translation) = EntryFactory.destruct(entry)
        EntryParameterValidator.valid_entry(word, pos, description, translation)
        parameters = (get_entry_id(word), word, pos, description, translation)
        queries.insert_entry(conn, parameters)
 
    def update_one(
            conn : sqlite3.Connection,
            entry : dict[str, str],
        ):
        (word, pos, description, translation) = EntryFactory.destruct(entry)
        EntryParameterValidator.valid_entry(word, pos, description, translation)

        parameters = (pos, description, translation, get_entry_id(word))
        print("DEBUG", word, parameters)
        queries.update_entry(conn, parameters)


    def select_all(
            conn : sqlite3.Connection,
        ) -> list[tuple[str, str, str, str]]:
        entries = queries.select_entries(conn)
        return entries

    def select_randn(
            conn : sqlite3.Connection,
            n : int,
        ) -> list[tuple[str, str, str, str]]:
        EntryParameterValidator.valid_n(n)
        entries = queries.select_entries_randn(conn, n)
        return entries
    





    # def insert_many(
    #         conn : sqlite3.Connection,
    #         entries : list[dict[str,str]]
    #     ) -> int:
    #     parameters = [(
    #         get_entry_id(e["word"]),
    #         e["word"],
    #         e.get("pos").lower(),
    #         e.get("description"),
    #         e.get("translation")
    #     ) for e in entries]
    #     return queries.insert_entries(conn, parameters)
    
    # def update_many(
    #         conn : sqlite3.Connection,
    #         entries : list[dict[str,str]]
    #     ) -> int:
    #     parameters = [(
    #         e.get("pos").lower(),
    #         e.get("description"),
    #         e.get("translation"),
    #         get_entry_id(e["word"])
    #     ) for e in entries]
    #     return queries.update_entries(conn, parameters)
    
    # def delete_many(
    #         conn : sqlite3.Connection,
    #         words : list[str],
    #     ) -> int:
    #     parameters = [(get_entry_id(w),) for w in words]
    #     return queries.delete_entries(conn, parameters)

    

    # word : str,
    # pos : str,
    # description : str,
    # translation : str,
    # parameters = (entry_id, word.lower(), pos, description, translation.lower())
