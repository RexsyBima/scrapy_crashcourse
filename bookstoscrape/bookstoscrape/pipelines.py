# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookstoscrapePipeline:
    def process_item(self, item, spider):
        item["price"] = float(item["price"].removeprefix("£"))
        item["rating"] = self.process_rating(item["rating"])
        item["stock"] = self.process_stock(item["stock"])
        item["total_reviews"] = int(item["total_reviews"])
        item["img_url"] = (
            f"https://books.toscrape.com/{item['img_url'].removeprefix('../../')}"
        )
        return item

    def process_rating(self, value):
        match value.split()[-1]:
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

    def process_stock(self, value: list[str]):
        return int(
            "".join(value)
            .strip()
            .removeprefix("In stock (")
            .removesuffix(" available)")
        )
