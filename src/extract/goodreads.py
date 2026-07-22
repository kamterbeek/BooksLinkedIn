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

def clean_value(value):
    if pd.isna(value):
        return None
    return value

def load_books():
    df = pd.read_csv(DATA_PATH)

    df = df.where(pd.notnull(df), None)

    books = []

    for _, row in df.iterrows():
      
      book = Book(
    book_id=clean_value(row["Book Id"]),
    title=clean_value(row["Title"]),
    author=clean_value(row["Author"]),
    isbn=clean_value(row["ISBN"]),
    isbn13=clean_value(row["ISBN13"]),
    rating=clean_value(row["My Rating"]),
    pages=clean_value(row["Number of Pages"]),
    year_published=clean_value(row["Year Published"]),
    date_added=clean_value(row["Date Added"]),
    date_read=clean_value(row["Date Read"]),
    shelf=clean_value(row["Exclusive Shelf"]),
    review=clean_value(row["My Review"]),
)
    if validate_book(book):
            books.append(book)
    return books

if __name__ == "__main__":

    books = load_books()

    print(f"Loaded {len(books)} books.")

    print("Firest books:")
    print(books[0])