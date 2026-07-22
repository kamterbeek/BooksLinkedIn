from pydantic import BaseModel, Field
from typing import Optional

class book(BaseModel):
    book_id: int
    title: str
    author: str