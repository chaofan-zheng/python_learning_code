# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseinformationItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    huxing = scrapy.Field()
    area = scrapy.Field()
    chaoxiang = scrapy.Field()
    louceng = scrapy.Field()
    built_time = scrapy.Field()
    location_name = scrapy.Field()
    location = scrapy.Field()
    total_price = scrapy.Field()
    price_average = scrapy.Field()
