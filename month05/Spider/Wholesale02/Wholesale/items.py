# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WholesaleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    integer = scrapy.Field()
    rePurchaseRate = scrapy.Field()
    price = scrapy.Field()
    title=scrapy.Field()
    href=scrapy.Field()



    # express_fee= scrapy.Field()