import sqlite3

DATABASE = "test.db"

class Database:
    def get_db(self, g):
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(DATABASE, check_same_thread=False)
        return db