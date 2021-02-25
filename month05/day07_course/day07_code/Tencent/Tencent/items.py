# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    """    1.1) 职位名称
    1.2) 职位地点
    1.3) 职位类别
    1.4) 发布时间
    1.5) 工作职责
    1.6) 工作要求"""
    post_name =scrapy.Field()
    location = scrapy.Field()
    category = scrapy.Field()
    update_time = scrapy.Field()
    responsibility = scrapy.Field()
