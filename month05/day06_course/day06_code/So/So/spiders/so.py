import scrapy


class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['www.so.com']
    start_urls = ['http://www.so.com/']

    def parse(self, response):
        res = response.xpath('/html/head/title/text()')
        print(res)
