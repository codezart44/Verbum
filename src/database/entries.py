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


def select_all_entries(
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
        success1 = insert_entry(c, "test", "this is a test", "test") > 0
        success2 = update_entry(c, "test", "this is the new desc.", 'tst') > 0
        # insert_entry(c, "testt", "this is a test", "test")
        # success3 = delete_entry(c, "test") > 0

        one = select_entry(c, "test")
        _all = select_all_entries(c)

        print(success1)
        print(success2)

        print(one)
        print(_all)
    pass

if __name__=="__main__":
    main()