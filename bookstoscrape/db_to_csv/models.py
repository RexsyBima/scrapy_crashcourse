from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, Float
from db_to_csv import Base


class BookSqlAlchemyItem(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)
    description = Column(String)
    upc = Column(String)
    type_ = Column(String)
    total_reviews = Column(Integer, nullable=False)


@dataclass
class Book:
    title: str
    price: float
    stock: int
    rating: int
    description: str
    upc: str
    type_: str
    total_reviews: int
