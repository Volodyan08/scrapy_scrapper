import scrapy
from scrapy_scrapper.items import ScrapyScrapperItem
from scrapy.loader import ItemLoader


class WhiskySpider(scrapy.Spider):
    name = 'whisky'
    start_urls = ['https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock']

    def parse(self, response):
        for product in response.css('div.product-item-info'):
            element = ItemLoader(item=ScrapyScrapperItem(), selector=product)
            element.add_css('name', 'a.product-item-link')
            element.add_css('price', 'span.price')
            element.add_css('link', 'a.product-item-link::attr(href)')

            yield element.load_item()

        next_page = response.css('a.action.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
