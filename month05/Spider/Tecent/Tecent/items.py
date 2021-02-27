# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TecentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    post_name = scrapy.Field()
    location_name = scrapy.Field()
    category = scrapy.Field()
    update_time = scrapy.Field()
    responsibility = scrapy.Field()
    requirement = scrapy.Field()