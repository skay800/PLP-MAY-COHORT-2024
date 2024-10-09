# library_logic.py

from sqlalchemy.orm import Session
from models import Author, Book, Member

def create_author(db: Session, name: str):
    author = Author(name=name)
    db.add(author)
    db.commit()
    db.refresh(author)
    return author

def create_book(db: Session, title: str, author_id: int):
    book = Book(title=title, author_id=author_id)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def create_member(db: Session, name: str, email: str):
    member = Member(name=name, email=email)
    db.add(member)
    db.commit()
    db.refresh(member)
    return member

def get_authors(db: Session):
    return db.query(Author).all()

def get_books(db: Session):
    return db.query(Book).all()

def get_members(db: Session):
    return db.query(Member).all()
