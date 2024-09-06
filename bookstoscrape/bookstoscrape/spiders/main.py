import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http.response import Response
from scrapy.linkextractors import LinkExtractor
from ..items import BookstoscrapeItem as Book


class MainSpider(CrawlSpider):
    name = "main"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]
    rules = [
        # Rule to extract item pages
        Rule(
            LinkExtractor(
                allow=(r"/catalogue/.*_\d+/index\.html"), deny=(r"/category/")
            ),
            callback="parse_item",
            follow=True,
        ),
        # Rule to follow pagination links
        Rule(
            LinkExtractor(
                restrict_css="li.next a"  # This will extract the 'next' pagination links
            ),
            follow=True,
        ),
    ]

    def parse(self, response: Response):
        title = response.css("h3 a::attr(title)").get()

    def parse_item(self, response: Response):
        product_page: Response = response.css("div.col-sm-6.product_main")
        table_page = response.css("table.table.table-striped td::text").getall()

        title = product_page.css("h1::text").get()
        price = response.css("p.price_color::text").get()
        stock = "".join(
            product_page.css("p.instock.availability::text").getall()
        ).strip()
        rating = response.css(
            "p.star-rating::attr(class)"
        ).get()  # self.get_rating(response)
        description = response.css("div#product_description ~ p::text").get()
        upc = table_page[0]
        type_ = table_page[1]
        total_reviews = int(table_page[-1])
        book = Book(
            title=title,
            price=price,
            stock=stock,
            rating=rating,
            description=description,
            upc=upc,
            type_=type_,
            total_reviews=total_reviews,
        )
        yield book


"""        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse_item)"""
