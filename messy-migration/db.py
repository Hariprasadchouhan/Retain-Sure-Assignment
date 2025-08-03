import sqlite3

_db = None

def get_db():
    global _db
    if _db is None:
        _db = sqlite3.connect('users.db', check_same_thread=False)
    return _db

def get_cursor():
    return get_db().cursor()
