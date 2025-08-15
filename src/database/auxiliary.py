import sqlite3
from .connect import get_connection, get_entry_id, get_tag_id


def insert_tag(
        c : sqlite3.Cursor,
        word : str,
        tag : str,
) -> int:
    entry_id = get_entry_id(word)
    tag_id = get_tag_id(word, tag)
    parameters = (tag_id, entry_id, word, tag)
    
    sql = """--sql
    INSERT OR IGNORE INTO en_tags ([tag_id], [entry_id], [word], [tag])
    VALUES (?, ?, ?, ?);
    """
    c.execute(sql, parameters)
    return c.rowcount


def select_word_tags(
        c : sqlite3.Cursor,
        word : str,
) -> list[tuple[str, str]]:
    entry_id = get_entry_id(word)

    parameters = (entry_id,)

    sql = """--sql
    SELECT [tag] FROM en_tags
    WHERE [entry_id] = ?
    """
    c.execute(sql, parameters)
    return c.fetchall()


def select_tag_words(
        c : sqlite3.Cursor,
        tag : str,
) -> list[tuple[str]]:
    pass


def main():
    w = "yolo"
    t1 = "contemporary"
    t2 = "abbreviation"
    t3 = "inofficial"

    with get_connection() as conn:
        c = conn.cursor()
        # c1 = insert_tag(c, w, t1)
        # c2 = insert_tag(c, w, t2)
        # c3 = insert_tag(c, w, t3)
        # print(c1, c2, c3)

        tags = select_word_tags(c, w)
        print(w, tags)


if __name__=="__main__":
    main()