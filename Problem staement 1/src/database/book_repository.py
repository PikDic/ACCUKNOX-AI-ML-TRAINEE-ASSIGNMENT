from database.db_connection import get_connection

def create_books_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            publish_year INTEGER
        )
    """)

    conn.commit()
    conn.close()


def insert_books(book_list):
    conn = get_connection()
    cursor = conn.cursor()

    for book in book_list:
        cursor.execute(
            "INSERT INTO books (title, author, publish_year) VALUES (?, ?, ?)",
            (book["title"], book["author"], book["year"])
        )

    conn.commit()
    conn.close()


def fetch_all_books():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT title, author, publish_year FROM books")
    rows = cursor.fetchall()

    conn.close()
    return rows
