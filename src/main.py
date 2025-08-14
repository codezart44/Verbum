from typing import Literal

from .database.entries import insert_entries, select_entries, select_entries_randn
from .database.connect import get_connection


def main():
    # with get_connection() as conn:
    #     c = conn.cursor()
    #     rows = select_entries_randn(c, n=10)

    # for row in rows:
    #     print(row[0])


    with open("entries.csv", mode="r", encoding="utf-8") as f:
        lines = f.readlines()[1:]  # skip header

    lines = [l.strip().split(";") for l in lines]
    entries = [(
        l[0].strip().lower(), 
        l[1].strip().lower(), 
        l[2].strip(), 
        l[3].strip().lower()
        ) for l in lines]
    
    with get_connection() as conn:
        c = conn.cursor()
        success = insert_entries(c, entries)
    
    print(success)


if __name__=="__main__":
    main()
