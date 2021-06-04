import json
from urllib.parse import urlencode

from ..items import WholesaleItem

import scrapy


class WholesaleSpider(scrapy.Spider):
    name = 'wholesale'
    allowed_domains = ['1688.com']
    start_urls = ['http://1688.com/']

    # url = 'https://search.1688.com/service/marketOfferResultViewService?keywords=%C5%AE%D7%B0&beginPage={}'
    base_url = 'https://search.1688.com/service/marketOfferResultViewService?'
    keyword = input('请输入想要批发的货物名称（准确填写一种货物）：')
    def start_requests(self):
        params2 = {'keywords': f'{self.keyword}'}
        url2 = self.base_url + urlencode(params2, encoding='gbk') + '&beginPage={}'
        print(url2)
        for page in range(1, 51):
            page_url = url2.format(page)
            print(page_url)
            yield scrapy.Request(url=page_url, callback=self.first_parse)

    def first_parse(self, response):
        '''解析提取女装的数据'''
        html = json.loads(response.text)
        offer_list = html['data']['data']['offerList']
        # print(html)
        for one_html in offer_list:
            item = WholesaleItem()
            item['rePurchaseRate'] = one_html['information']['rePurchaseRate']
            item['price'] = one_html['tradePrice']['offerPrice']['valueString']
            item['title'] = one_html['information']['simpleSubject']
            item['href'] = one_html['information']['detailUrl']
            try:
                item['integer'] = one_html['tradeQuantity']['gmvValue']['integer']
            except:
                item['integer']=''
            # yield scrapy.Request(url=href, callback=self.parse_second, meta={'item': item})
            yield item

    # def parse_second(self, response):
    #     item = response.meta['item']
    #     item['express_fee'] = response.xpath(
    #         '//div[@class="cost-entries"]/div[@class="cost-entries-type"]//p[2]/em/text()').get()
    #     yield item


