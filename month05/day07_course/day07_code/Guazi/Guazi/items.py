# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GuaziItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    href = scrapy.Field()
    # 里程 排量 变速箱
    km = scrapy.Field()
    displace = scrapy.Field()
    typ = scrapy.Field()
    # 属于类变量
    # 相当于定义了一个类字典：{'title': ,'price': ,'href': ,}
    # Item 内部实现本身就是字典
