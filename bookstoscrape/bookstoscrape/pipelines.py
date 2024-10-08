# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .items import session, BookSqlAlchemyItem


class BookstoscrapePipeline:
    def process_item(self, item, spider):
        item["stock"] = int(
            "".join(item["stock"])
            .strip()
            .replace("In stock (", "")
            .replace(" available)", "")
        )
        item["price"] = float(item["price"].replace("£", ""))
        item["rating"] = self.get_rating(item["rating"].split()[-1])
        return item

    def get_rating(self, item):
        match item:
            case "One":
                return 1
            case "Two":
                return 2
            case "Three":
                return 3
            case "Four":
                return 4
            case "Five":
                return 5
            case _:
                return 0


class SqlAlchemyPipeline:
    def open_spider(self, spider):
        self.session = session

    def close_spider(self, spider):
        self.session.close()

    def process_item(self, item, spider):
        book = BookSqlAlchemyItem(**item)
        book_exist = (
            self.session.query(BookSqlAlchemyItem).filter_by(title=book.title).first()
        )
        if book_exist:
            print(f"Book {book.title} already exists")
        else:
            self.session.add(book)
            self.session.commit()
            print(f"Book {book.title} added")
