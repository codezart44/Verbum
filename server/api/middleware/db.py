# from flask import g, Blueprint
# import sqlite3

# from ..utils.connect import get_db_conn

# def register_middleware(blueprint: Blueprint):
    
#     @blueprint.before_request
#     def _setup_conn():
#         db = get_db_conn()
#         db.row_factory = sqlite3.Row
#         g.db = db

#     @blueprint.teardown_request
#     def _teardown_conn(err):
#         db: sqlite3.Connection = g.get("db", None)
#         if db is None: return
#         if err is None:
#             db.commit()
#         else:
#             db.rollback()
#         db.close()
