from models import Book

def validate_book(book: Book) -> bool:
    return (
        len(book.title) > 0 
        and len(book.author) > 0
    )
