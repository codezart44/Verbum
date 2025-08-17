import sqlite3
from ...config import CONFIG

PROJECT_PATH = CONFIG["project"]["path"]
DATABASE_PATH = CONFIG["database"]["path"]

def connect_db() -> sqlite3.Connection:
    abs_path_db = f"{PROJECT_PATH}/{DATABASE_PATH}"
    return sqlite3.connect(abs_path_db)
