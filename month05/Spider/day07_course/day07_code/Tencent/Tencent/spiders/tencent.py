import scrapy
import requests
import time
import json
from ..items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    # search_url = 'https://careers.tencent.com/en-us/search.html?index={}&keyword={}'

    get_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={}&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=en-us&area='
    get_headers = {'referer': 'https://careers.tencent.com/en-us/search.html',
                   'sec-ch-ua': '''"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"''',
                   'sec-ch-ua-mobile': ' ?0',
                   'sec-fetch-dest': 'empty',
                   'sec-fetch-mode': 'cors',
                   'sec-fetch-site': 'same-origin',
                   'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
                   }

    def make_timestamp(self):
        """生成url中的时间戳 1614216064753"""
        timestamp = int(time.time() * 1000)
        return str(timestamp)

    def get_total(self, timestamp, keyword):
        """获得总页数"""
        html = requests.get(url=self.get_url.format(timestamp, keyword, 1)).json()
        total_page = int(int(html['Data']['Count']) / 10) + 1
        return total_page

    def start_requests(self):
        keyword = input('请输入要抓取的关键字')
        time_stamp = self.make_timestamp()
        total_page = self.get_total(timestamp=time_stamp, keyword=keyword)
        for page in range(1, total_page + 1):
            page_url = self.get_url.format(time_stamp, keyword, page)
            yield scrapy.Request(url=page_url, callback=self.parse)

    def parse(self, response):
        html = json.loads(response.text)
        posts_list = html['Data']['Posts']
        for post in posts_list:
            item = TencentItem()
            #     post_name =scrapy.Field()
            #     location = scrapy.Field()
            #     category = scrapy.Field()
            #     update_time = scrapy.Field()
            #     responsibility = scrapy.Field()
            item['post_name']=post['RecruitPostName']
            item['location']=post['LocationName']
            item['category']=post['CategoryName']
            item['update_time']=post['LastUpdateTime']
            item['responsibility']=post['Responsibility']
            yield item

