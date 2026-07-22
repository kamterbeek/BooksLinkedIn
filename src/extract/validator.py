from models import Book

def validate_book(book: Book) -> bool:
    return (
      len(book.title.strip()) > 0
        and len(book.author.strip()) > 0
    )
