import scrapy
from ..items import HouseinformationItem


class HouseinformationSpider(scrapy.Spider):
    name = 'houseInformation'
    allowed_domains = ['hz.58.com']
    start_urls = ['https://hz.58.com/ershoufang/p1/']
    url = 'https://hz.58.com/ershoufang/p{}/'

    def start_requests(self):
        for page in range(1, 51):
            page_url = self.url.format(page)
            yield scrapy.Request(url=page_url, callback=self.parse)

    def parse(self, response):
        li_list = response.xpath('//section[@class="list"]/div')
        for li in li_list:
            item = HouseinformationItem()
            item['title'] = li.xpath('./a/div[2]/div[1]/div[1]/h3/text()').get().strip()
            huxing = ''
            for span in li.xpath('./a/div[2]/div[1]/section/div[1]/p[1]/span'):
                huxing += span.xpath('./text()').get().strip()
            item['huxing'] = huxing

            item['area'] = li.xpath('./a/div[2]/div[1]/section/div[1]/p[2]/text()').get().strip()
            item['chaoxiang'] = li.xpath('./a/div[2]/div[1]/section/div[1]/p[3]/text()').get().strip()
            item['louceng'] = li.xpath('./a/div[2]/div[1]/section/div[1]/p[4]/text()').get().strip()
            item['built_time'] = li.xpath('./a/div[2]/div[1]/section/div[1]/p[5]/text()').get().strip()
            item['location_name'] = li.xpath('.//p[@class="property-content-info-comm-name"]/text()').get().strip()
            location = ''
            for span in li.xpath('.//p[@class="property-content-info-comm-address"]/span'):
                location += span.xpath('./text()').get().strip() + '-'
            item['location'] = location[:-1]

            item['total_price'] = li.xpath('.//span[@class="property-price-total-num"]/text()').get().strip()
            item['price_average'] = li.xpath('.//p[@class="property-price-average"]/text()').get().strip()
            yield item
