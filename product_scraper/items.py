# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Data(scrapy.Item):
    url_movie = scrapy.Field()
    name = scrapy.Field()
    genre = scrapy.Field()
    rate = scrapy.Field()
    stars = scrapy.Field()
    type = scrapy.Field()
    Country = scrapy.Field()
    Language = scrapy.Field()
    Budget = scrapy.Field()
    Sound = scrapy.Field()
    Ratio = scrapy.Field()