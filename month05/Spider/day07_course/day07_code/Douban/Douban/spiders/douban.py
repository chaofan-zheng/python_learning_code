import json
import scrapy
from ..items import DoubanItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/']
    url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={}&limit=20'
    # json地址：就是get提交到的地址（返回json数据的地址）
    # 可以用request模块，获取总页数。

    def start_requests(self):
        for start in range(0,101,20):
            page_url = self.url.format(start)
            yield scrapy.Request(url=page_url,
                                 callback=self.parse)

    def parse(self, response):
        html = json.loads(response.text)  # 这里面得手动找json模块
        for one_dict in html:
            item = DoubanItem()
            item['rank']=one_dict['rank']
            item['title']=one_dict['title']
            item['score']=one_dict['score']
            # 交给项目管道处理
            yield item

