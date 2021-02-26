import scrapy
from ..items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['www.maoyan.com']
    start_urls = ['https://maoyan.com/board/4']

    def parse(self, response):
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        print(response)
        for dd in dd_list:
            item = MaoyanItem()
            item['title'] = dd.xpath('.//p[@class="name"]/a/@title').get()
            # print('dd',dd.xpath('.//p[@class="name"]/a/@title').get())
            item['actor'] = dd.xpath('.//p[@class="star"]/text()').get().strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').get()
            item['score'] = dd.xpath('.//p[@class="score"]/text()').get()
            yield item
