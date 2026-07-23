from pathlib import Path

import pandas as pd
from pydantic import ValidationError

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
    """
    Convert Pandas NaN values into Python None.
    """
    if pd.isna(value):
        return None
    return value


def load_books():
    """
    Read the Goodreads export and convert each row into a Book object.
    """

    df = pd.read_csv(DATA_PATH)

    books = []
    errors = []

    for index, row in df.iterrows():

        try:

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

        except ValidationError as e:
            errors.append(
                {
                    "row": index,
                    "title": row.get("Title"),
                    "error": e,
                }
            )

    return books, errors


if __name__ == "__main__":

    books, errors = load_books()

    print(f"\nLoaded {len(books)} books.")
    print(f"Errors: {len(errors)}")

    if books:
        print("\nFirst book:")
        print(books[0])

    if errors:
        print("\nFirst validation error:")
        print(f"Row: {errors[0]['row']}")
        print(f"Title: {errors[0]['title']}")
        print(errors[0]["error"])