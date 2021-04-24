import scrapy


class TmoocSpider(scrapy.Spider):
    name = 'tmooc'
    allowed_domains = ['tts.tmooc.cn','c.it211.com.cn']
    start_urls = ['https://c.it211.com.cn/aid20101106am/aid20101106am.m3u8?_time=1618722481205&sign=87BFA989C7B3E007811E80B4C35C62E4']

    def parse(self, response):
        pass
