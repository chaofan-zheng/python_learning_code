import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫名，默认和文件名是一样的。作用：用于运行爬虫 ·scrapy crawl 爬虫名·
    name = 'baidu'
    # 允许抓取的域名
    allowed_domains = ['www.baidu.com']
    # 起始的url地址
    start_urls = ['http://www.baidu.com/'] # 是一个列表，第一个或者第一批

    def parse(self, response):
        r = response.xpath('/html/head/title/text()')
        print(r)
