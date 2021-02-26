import random
import time

import pymongo
import requests
from lxml import etree
from fake_useragent import UserAgent


class BookSpider:
    def __init__(self):
        self.url = 'https://book.douban.com/top250?start={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['doubandb']
        self.set = self.db['doubanset']

    def get_html(self, url):
        self.headers['User-Agent'] = UserAgent().random
        html = requests.get(url=url, headers=self.headers).text
        self.parse_html(html)

    def parse_html(self, html):
        # 创建解析对象
        eobj = etree.HTML(html)
        table_list = eobj.xpath('//table')
        # print(table_list)
        for table in table_list:
            item = {}
            # item['title']=table.xpath('.//div[@class="pl2"]/a/@title')[0]
            # xpath 肯定是一个列表，所以要用索引
            # 也不能贸然去取，万一有特殊数据会报错
            title_list = table.xpath('.//div[@class="pl2"]/a/@title')
            item['title'] = title_list[0] if title_list else None
            info_list = table.xpath('.//p[@class="pl"]/text()')
            item['info'] = info_list[0] if info_list else None
            score_list = table.xpath('.//span[@class="rating_nums"]/text()')
            item['score'] = score_list[0] if score_list else None
            comment_list = table.xpath('.//span[@class="inq"]/text()')
            item['comment'] = comment_list[0] if comment_list else None
            print(item)
            self.set.insert_one(item)

    def crawl(self):
        for page in range(1, 11):
            start = (page - 1) * 25
            page_url = self.url.format(start)
            self.get_html(url=page_url)
            time.sleep(random.uniform(0, 2))


if __name__ == '__main__':
    spider = BookSpider()
    spider.crawl()
