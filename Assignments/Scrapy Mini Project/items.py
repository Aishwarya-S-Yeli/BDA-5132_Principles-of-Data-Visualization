# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapy1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    html_title = scrapy.Field()
    html_first_example = scrapy.Field()
    css_title = scrapy.Field()
    css_first_example = scrapy.Field()
    php_title = scrapy.Field()
    php_first_example = scrapy.Field()
    pass
