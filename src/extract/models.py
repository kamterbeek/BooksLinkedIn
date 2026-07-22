from pydantic import BaseModel, Field
from typing import Optional

class book(BaseModel):
    book_id: int
    title: str
    author: str

    isbn: Optional[str] = None
    isbn13: Optional[str] = None

    rating: Optional[int] = None
    pages: Optional[int] = None

    year_published: Optional[int] = None

    date_added: Optional[str] = None
    date_read: Optional[str] = None

    shelf: Optional[str] = None

    review: Optional[str] = None