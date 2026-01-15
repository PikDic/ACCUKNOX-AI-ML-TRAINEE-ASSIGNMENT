import requests

API_URL = "https://openlibrary.org/search.json?q=python&limit=10"

def fetch_books_from_api():
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()

    data = response.json()
    books = []

    for item in data.get("docs", []):
        books.append({
            "title": item.get("title"),
            "author": item.get("author_name", ["Unknown"])[0],
            "year": item.get("first_publish_year")
        })

    return books
