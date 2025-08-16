import sqlite3
from ..connect import get_connection, get_entry_id, get_tag_id
from typing import Collection


def insert_tags(
        c : sqlite3.Cursor,
        word : str,
        tags : Collection[str],
) -> int:
    entry_id = get_entry_id(word)
    parameters = [(entry_id, get_tag_id(t), word.lower(), t.lower()) for t in tags]

    sql = """--sql
    INSERT OR IGNORE INTO en_tags ([entry_id], [tag_id], [word], [tag])
    VALUES (?, ?, ?, ?);
    """
    c.executemany(sql, parameters)
    return c.rowcount


def select_word_tags(
        c : sqlite3.Cursor,
        word : str,
) -> list[tuple[str]]:
    entry_id = get_entry_id(word)

    parameters = (entry_id,)

    sql = """--sql
    SELECT [tag] FROM en_tags
    WHERE [entry_id] = ?;
    """
    c.execute(sql, parameters)
    return c.fetchall()


def select_tag_words(
        c : sqlite3.Cursor,
        tag : str,
) -> list[tuple[str]]:
    tag_id = get_tag_id(tag)
    parameters = (tag_id,)

    sql = """--sql
    SELECT [word] FROM en_tags
    WHERE [tag_id] = ?;
    """
    c.execute(sql, parameters)
    return c.fetchall()


def delete_tags(
        c : sqlite3.Cursor,
        tags : Collection[str],
) -> int:
    parameters = [(get_tag_id(t),) for t in tags]

    sql = """--sql
    DELETE FROM en_tags
    WHERE [tag_id] = ?;
    """
    c.executemany(sql, parameters)
    return c.rowcount

def delete_word_tags(
        c : sqlite3.Cursor,
        word : str,
        tags : Collection[str],
) -> int:
    entry_id = get_entry_id(word)
    parameters = [(entry_id, get_tag_id(t)) for t in tags]

    sql = """--sql
    DELETE FROM en_tags
    WHERE [entry_id] = ? AND [tag_id] = ?;
    """
    c.executemany(sql, parameters)
    return c.rowcount




def main():
    w1 = "yolo"
    w2 = "swag"

    t1 = "contemporary"
    t2 = "abbreviation"
    t3 = "inofficial"
    t4 = "nsfw"

    with get_connection() as conn:
        c = conn.cursor()

        # print(insert_tags(c, w1, (t1, t2, t3)))
        # print(delete_tags(c, (t1, t2, t3)))

        print(insert_tags(c, w2, (t2, t3, t4)))
        # print(delete_tags(c, (t2, t3, t4)))

        tags = select_word_tags(c, w1)
        print(w1, tags)

        words = select_tag_words(c, t2)
        print(t2, words)


if __name__=="__main__":
    main()








def insert_tag(
        c : sqlite3.Cursor,
        word : str,
        tag : str,
) -> int:
    entry_id = get_entry_id(word)
    tag_id = get_tag_id(tag)
    parameters = (entry_id, tag_id, word, tag)
    
    sql = """--sql
    INSERT OR IGNORE INTO en_tags ([entry_id], [tag_id], [word], [tag])
    VALUES (?, ?, ?, ?);
    """
    c.execute(sql, parameters)
    return c.rowcount

def delete_tag(
        c : sqlite3.Cursor,
        tag : str,
) -> int:
    tag_id = get_tag_id(tag)
    parameters = (tag_id,)

    sql = """--sql
    DELETE FROM en_tags
    WHERE [tag_id] = ?;
    """
    c.execute(sql, parameters)
    return c.rowcount

