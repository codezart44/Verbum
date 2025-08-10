import sqlite3
import uuid

from ..config import CONFIG


conn = sqlite3.connect(CONFIG["database"]["file"])
c = conn.cursor()
