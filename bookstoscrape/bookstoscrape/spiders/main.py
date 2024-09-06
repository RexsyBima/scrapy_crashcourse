import scrapy
from ..items import BookstoscrapeItem as Book
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MainSpider(CrawlSpider):
    name = "main"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]
    rules = [
        Rule(
            LinkExtractor(allow=(r"catalogue/"), deny=(r"/category/")),
            follow=True,
            callback="parse_item",
        ),
        Rule(LinkExtractor(restrict_css="li.next a"), follow=True),
    ]

    def parse_item(self, response):
        title = response.css("article.product_page div.row h1::text").get()
        price = response.css("p.price_color::text").get()
        stock = response.css(
            "div.col-sm-6.product_main p.instock.availability::text"
        ).getall()
        rating = response.css("p.star-rating::attr(class)").get()
        description = response.css("div#product_description ~ p::text").get()
        table_data = response.css("table.table.table-striped td::text").getall()
        upc = table_data[0]
        type_ = table_data[1]
        total_reviews = table_data[-1]
        img_url = response.css("img ::attr(src)").get()
        url = response.url
        book = Book(
            title=title,
            price=price,
            stock=stock,
            rating=rating,
            description=description,
            upc=upc,
            type_=type_,
            total_reviews=total_reviews,
            img_url=img_url,
            url=url,
        )
        yield book


# soup.find("article", class_="product_page").find("div", class_="row").find("h1").get_text()
