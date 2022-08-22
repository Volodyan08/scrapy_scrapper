import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import  TakeFirst, MapCompose
from w3lib.html import remove_tags


def remove_currency(value):
    return value.replace('£','').strip()


class ScrapyScrapperItem(scrapy.Item):
    name = scrapy.Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(remove_tags, remove_currency), output_processor=TakeFirst())
    link = scrapy.Field()
