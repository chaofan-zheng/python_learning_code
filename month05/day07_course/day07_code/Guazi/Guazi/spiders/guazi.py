import scrapy
from ..items import GuaziItem

class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['www.guazi.com']
    start_urls = ['https://www.guazi.com/tj/buy/']

    def parse(self, response):
        # 解析提取汽车数据
        li_list = response.xpath('//ul[@class="carlist clearfix js-top"]/li')
        for li in li_list:
            # 给items.py中的GuaziItem类实例化
            item = GuaziItem()
            # scrapy1.5以后的版本，不用item.title了，要用字典item['title']
            # 变量名要和items.py中高度一致
            item['title'] = li.xpath('./a/@title').get()
            item['price'] = li.xpath('.//div[@class="t-price"]/p/text()').get()
            item['href'] = li.xpath('./a/@href').get()
            # 提交到pipeline
            yield item
