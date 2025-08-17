import sqlite3


#################### SINGLE RECORD ####################

def select_entry(
        conn : sqlite3.Connection,
        parameters : tuple[str]
) -> tuple[str]:
    sql = """--sql
    SELECT [word], [pos], [description], [translation] FROM en_entries 
    WHERE entry_id = ?;
    """
    return conn.execute(sql, parameters).fetchone()

def insert_entry(
        conn : sqlite3.Connection,
        parameters : tuple[str, str, str, str]
) -> int:
    sql = """--sql
    INSERT OR IGNORE INTO en_entries ([entry_id], [word], [pos], [description], [translation]) 
    VALUES (?, ?, ?, ?, ?);
    """
    c = conn.execute(sql, parameters)
    return c.rowcount

def delete_entry(
        conn : sqlite3.Connection,
        parameters : tuple[str]
) -> int:
    sql = """--sql
    DELETE FROM en_entries WHERE [entry_id] = ? ;
    """
    c = conn.execute(sql, parameters)
    return c.rowcount

def update_entry(
        conn : sqlite3.Connection,
        parameters : tuple[str, str, str, str]
) -> int:
    sql = """--sql
    UPDATE en_entries
    SET [pos] = ?, [description] = ?, [translation] = ?
    WHERE [entry_id] = ?;
    """
    c = conn.execute(sql, parameters)
    return c.rowcount


#################### MULTI RECORD ####################

def insert_entries(
        conn : sqlite3.Connection,
        parameters : list[tuple[str, str, str, str]]
) -> int:
    sql = """--sql
    INSERT OR IGNORE INTO en_entries ([entry_id], [word], [pos], [description], [translation])
    VALUES (?, ?, ?, ?, ?);
    """
    c = conn.executemany(sql, parameters)
    return c.rowcount

def update_entries(
        conn : sqlite3.Connection,
        parameters : list[tuple[str, str, str, str]]
) -> int:
    sql = """--sql
    UPDATE en_entries
    SET [pos] = ?, [description] = ?, [translation] = ?
    WHERE [entry_id] = ?;
    """
    c = conn.executemany(sql, parameters)
    return c.rowcount

def delete_entries(
        conn : sqlite3.Connection,
        parameters : list[tuple[str]],
) -> int:
    sql = """--sql
    DELETE FROM en_entries WHERE [entry_id] = ?;
    """
    c = conn.executemany(sql, parameters)
    return c.rowcount

def select_entries(
        conn : sqlite3.Connection,
) -> list[tuple[str]]:
    sql = """--sql
    SELECT [word], [pos], [description], [translation] FROM en_entries;
    """
    return conn.execute(sql).fetchall()

def select_entries_randn(
        conn : sqlite3.Connection,
        n : int,
) -> list[tuple[str]]:
    sql = """--sql
    SELECT [word], [pos], [description], [translation] FROM en_entries
    ORDER BY RANDOM()
    LIMIT ?;
    """
    return conn.execute(sql, (n,)).fetchall()











def main():
    # with get_connection() as conn:
    #     c = conn.cursor()

    #     entries = [
    #         ("monkey", "noun", "hairy man", "apa"),
    #         ("rabbit", "noun", "funny furry thing", "kanin"),
    #         ("turtle", "noun", "u wont crack 'im", "sköldpadda"),
    #         ("lion", "noun", "big pussy", "lejon"),
    #         ("skbhf", None, "nonsense", None),
    #     ]
    #     words = ["monkey", "rabbit", "turtle", "lion", "skbhf", "word"]

    #     # success = insert_entries(c, entries) > 0
    #     success = delete_entries(c, words) > 0
    #     # success = update_entries(c, entries) > 0

    #     print(success)

        
    pass

if __name__=="__main__":
    main()

