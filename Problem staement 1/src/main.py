from api.fetch_books import fetch_books_from_api
from database.book_repository import (
    create_books_table,
    insert_books,
    fetch_all_books
)


def main():
    # ---- Problem 1.1 ----
    create_books_table()

    books = fetch_books_from_api()
    insert_books(books)

    stored_books = fetch_all_books()
    print("\nBooks stored in database:\n")

    for book in stored_books:
        print(f"Title: {book[0]}")
        print(f"Author: {book[1]}")
        print(f"Published Year: {book[2]}")
        print("-" * 40)


if __name__ == "__main__":
    main()
