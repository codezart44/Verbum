import sqlite3
from typing import Collection

from verbum.api.utils.errors import SelectError, DeleteError, InsertError, UpdateError


def select_word_tags(
        conn : sqlite3.Connection,
        parameters : tuple[str],
) -> list[tuple[str]]:
    # entry_id = get_entry_id(word)
    # parameters = (entry_id,)
    
    # continue here ... # FIXME NOTE NOTE NOTE NOTE NOTE NOTE NOTE NOTE


    sql = """--sql
    SELECT [tag] FROM en_tags
    WHERE [entry_id] = ?;
    """
    c.execute(sql, parameters)
    return c.fetchall()

def select_tag_words(
        conn : sqlite3.Connection,
        tag : str,
) -> list[tuple[str]]:
    # tag_id = get_tag_id(tag)
    # parameters = (tag_id,)

    sql = """--sql
    SELECT [word] FROM en_tags
    WHERE [tag_id] = ?;
    """
    c.execute(sql, parameters)
    return c.fetchall()

def insert_tags(
        conn : sqlite3.Connection,
        parameters
) -> int:
    sql = """--sql
    INSERT OR IGNORE INTO en_tags ([entry_id], [tag_id], [word], [tag])
    VALUES (?, ?, ?, ?);
    """
    ninserts = len(parameters)
    c = conn.executemany(sql, parameters)
    match c.rowcount:
        case 0: raise InsertError("InsertError: All records already exist.")
        case x if x < ninserts: raise InsertError("InsertError: Some records already exist.")
        case x if x == ninserts: return
        case _: raise Exception

def delete_word_tags(
        conn : sqlite3.Connection,
        word : str,
        tags : Collection[str],
) -> int:
    # entry_id = get_entry_id(word)
    # parameters = [(entry_id, get_tag_id(t)) for t in tags]

    sql = """--sql
    DELETE FROM en_tags
    WHERE [entry_id] = ? AND [tag_id] = ?;
    """
    c.executemany(sql, parameters)
    return c.rowcount

def delete_tag_kind(
        conn : sqlite3.Connection,
        tags : Collection[str],
) -> int:
    # parameters = [(get_tag_id(t),) for t in tags]

    sql = """--sql
    DELETE FROM en_tags
    WHERE [tag_id] = ?;
    """
    c.executemany(sql, parameters)
    return c.rowcount

def update_tag_kind(  # to update an identical tag across many entries
        conn : sqlite3.Connection,
        parameters : tuple[str]
    ):
    sql = """--sql
    UPDATE en_tags
    SET [tag] = ?
    WHERE [tag] = ?;
    """
    ...





# def main():
    # w1 = "yolo"
    # w2 = "swag"

    # t1 = "contemporary"
    # t2 = "abbreviation"
    # t3 = "inofficial"
    # t4 = "nsfw"

    # with get_connection() as conn:
    #     c = conn.cursor()

    #     # print(insert_tags(c, w1, (t1, t2, t3)))
    #     # print(delete_tags(c, (t1, t2, t3)))

    #     print(insert_tags(c, w2, (t2, t3, t4)))
    #     # print(delete_tags(c, (t2, t3, t4)))

    #     tags = select_word_tags(c, w1)
    #     print(w1, tags)

    #     words = select_tag_words(c, t2)
    #     print(t2, words)


# if __name__=="__main__":
#     main()








# def insert_tag(
#         c : sqlite3.Cursor,
#         word : str,
#         tag : str,
# ) -> int:
#     entry_id = get_entry_id(word)
#     tag_id = get_tag_id(tag)
#     parameters = (entry_id, tag_id, word, tag)
    
#     sql = """--sql
#     INSERT OR IGNORE INTO en_tags ([entry_id], [tag_id], [word], [tag])
#     VALUES (?, ?, ?, ?);
#     """
#     c.execute(sql, parameters)
#     return c.rowcount

# def delete_tag(
#         c : sqlite3.Cursor,
#         tag : str,
# ) -> int:
#     tag_id = get_tag_id(tag)
#     parameters = (tag_id,)

#     sql = """--sql
#     DELETE FROM en_tags
#     WHERE [tag_id] = ?;
#     """
#     c.execute(sql, parameters)
#     return c.rowcount

