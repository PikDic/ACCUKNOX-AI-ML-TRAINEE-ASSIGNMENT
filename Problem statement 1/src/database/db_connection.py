import sqlite3

def get_connection(db_path="data/books.db"):
    """
    Creates and returns a SQLite database connection.
    """
    return sqlite3.connect(db_path)
