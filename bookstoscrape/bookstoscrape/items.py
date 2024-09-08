# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class BookstoscrapeItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    rating = scrapy.Field()
    description = scrapy.Field()
    upc = scrapy.Field()
    type_ = scrapy.Field()
    total_reviews = scrapy.Field()


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


engine = create_engine("sqlite:///books.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
