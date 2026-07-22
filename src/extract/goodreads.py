from pathlib import Path

import pandas as pd

from models import Book
from validator import validate_book

DATA_PATH = (
    Path(__file__)
    .resolve()
    .parents[2]
    / "data"
    / "raw"
    / "goodreads_library_export.csv"
)


def load_books():
    df = pd.read_csv(DATA_PATH)

    df = df.where(pd.notnull(df), None)

    books = []

    for _, row in df.iterrows():
        book = Book(
            book_id=row["Book Id"],
            title=row["Title"],
            author=row["Author"],
            isbn=row.get("ISBN"),
            isbn13=row.get("ISBN13"),
            rating=row.get("My Rating"),
            pages=row.get("Number of Pages"),
            year_published=row.get("Year Published"),
            date_added=row.get("Date Added"),
            date_read=row.get("Date Read"),
            shelf=row.get("Exclusive Shelf"),
            review=row.get("Review"),
        )
        if validate_book(book):
            books.append(book)
    return books

if __name__ == "__main__":

    books = load_books()

    print(f"Loaded {len(books)} books.")
    
    print("Firest books:")
    print(books[0])