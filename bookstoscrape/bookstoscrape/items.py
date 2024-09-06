# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookstoscrapeItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    rating = scrapy.Field()
    description = scrapy.Field()
    upc = scrapy.Field()
    type_ = scrapy.Field()
    total_reviews = scrapy.Field()
    img_url = scrapy.Field()
    url = scrapy.Field()

    # define the fields for your item here like:
    # name = scrapy.Field()
