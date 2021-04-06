import scrapy


class HouseinformationSpider(scrapy.Spider):
    name = 'houseInformation'
    allowed_domains = ['https://hz.58.com/']
    start_urls = ['http://https://hz.58.com//']

    def parse(self, response):
        pass
