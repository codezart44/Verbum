import sqlite3

from .connect import get_connection, get_entry_id

def insert_entry(
        c : sqlite3.Cursor,
        word : str, 
        description : str, 
        translation : str,
) -> int:
    entry_id = get_entry_id(word)
    parameters = (entry_id, word.lower(), description, translation.lower())

    sql = """--sql
    INSERT OR IGNORE INTO en_entries ([entry_id], [word], [description], [translation]) 
    VALUES (?, ?, ?, ?);
    """
    c.execute(sql, parameters)
    return c.rowcount


def insert_entries(
        c : sqlite3.Cursor,
        entries : list[tuple[str, str, str]]
) -> int:
    parameters = [(get_entry_id(t[0]), t[0], t[1], t[2]) for t in entries]

    sql = """--sql
    INSERT OR IGNORE INTO en_entries ([entry_id], [word], [description], [translation])
    VALUES (?, ?, ?, ?);
    """
    c.executemany(sql, parameters)
    return c.rowcount


def delete_entry(
        c : sqlite3.Cursor,
        word : str,
) -> int:
    entry_id = get_entry_id(word)
    parameters = (entry_id,)

    sql = """--sql
    DELETE FROM en_entries WHERE [entry_id] = ? ;
    """
    c.execute(sql, parameters)
    return c.rowcount


def delete_entries(
        c : sqlite3.Cursor,
        words : list[str],
) -> int:
    parameters = [(get_entry_id(w),) for w in words]

    sql = """--sql
    DELETE FROM en_entries WHERE [entry_id] = ?;
    """
    c.executemany(sql, parameters)
    return c.rowcount


def update_entry(
        c : sqlite3.Cursor,
        word : str,
        description : str,
        translation : str,
) -> int:
    entry_id = get_entry_id(word)
    parameters = (description, translation.lower(), entry_id)

    sql = """--sql
    UPDATE en_entries
    SET [description] = ?, [translation] = ?
    WHERE [entry_id] = ?;
    """
    c.execute(sql, parameters)
    return c.rowcount


def update_entries(
        c : sqlite3.Cursor,
        entries : list[tuple[str, str, str]]
) -> int:
    parameters = [(t[1], t[2], get_entry_id(t[0])) for t in entries]

    sql = """--sql
    UPDATE en_entries
    SET [description] = ?, [translation] = ?
    WHERE [entry_id] = ?;
    """
    c.executemany(sql, parameters)
    return c.rowcount


def select_entry(
        c : sqlite3.Cursor,
        word : str,
) -> tuple[str]:
    entry_id = get_entry_id(word)
    parameters = (entry_id,)

    sql = """--sql
    SELECT [word], [description], [translation] FROM en_entries 
    WHERE entry_id = ?;
    """
    c.execute(sql, parameters)
    return c.fetchone()


def select_entries(
        c : sqlite3.Cursor,
) -> list[tuple[str]]:
    sql = """--sql
    SELECT [word], [description], [translation] FROM en_entries;
    """

    c.execute(sql)
    return c.fetchall()
    

def main():
    with get_connection() as conn:
        c = conn.cursor()

        entries = [
            ("monkey", "hairy man", "apa"),
            ("rabbit", "funny furry thing", "kanin"),
            ("turtle", "u wont crack 'im", "sköldpadda"),
            ("lion", "big pussy", "lejon"),
            ("skbhf", "nonsense", None),
        ]
        words = ["monkey", "rabbit", "turtle", "lion", "skbhf", "word"]

        # success = insert_entries(c, entries) > 0
        success = delete_entries(c, words) > 0
        # success = update_entries(c, entries) > 0

        print(success)

        
    pass

if __name__=="__main__":
    main()