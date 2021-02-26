"""
增量爬虫
"""
import sys

import requests
import re
import time
import random
import pymongo
import redis
import hashlib


class NovelSpider:
    def __init__(self):
        self.url = 'https://www.biqukan.cc/fenlei1/{}.html'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
        # mongo 三个对象，mysql两个对象，
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['noveldb']
        self.set = self.db['novelset']
        self.r = redis.Redis(host='127.0.0.1', port=6379, db=0)

    def get_html(self, url):
        """请求,发请求获取响应内容html"""
        html = requests.get(url=url, headers=self.headers).text
        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """解析提取数据"""
        regex = '<div class="caption">.*?href="(.*?)" title="(.*?)">.*?<small class="text-muted fs-12">(.*?)</small>.*?>(.*?)</p>'
        # r_list: [(href,title,author,comment), (), ...]
        r_list = re.findall(regex, html, re.S)
        # 直接调用数据处理函数
        self.save_html(r_list)

    def save_html(self, r_list):
        """数据处理函数"""
        for r in r_list:
            item = {}
            item['href'] = r[0]
            href_h = self.hash_gen(r[0])
            result = self.r.sadd('novel:spider',href_h)
            if result == 1:
                item['title'] = r[1]
                item['author'] = r[2]
                item['comment'] = r[3]
                self.set.insert_one(item)
            else:
                sys.exit('更新完成')

    def hash_gen(self,href):
        md5 = hashlib.md5()
        md5.update(href.encode())
        res = md5.hexdigest()
        return res

    def crawl(self):
        """爬虫逻辑函数"""
        for page in range(1, 3):
            page_url = self.url.format(page)
            self.get_html(url=page_url)
            # 控制数据抓取频率
            time.sleep(random.randint(1, 3))

"""
面试题：
中华人民共和国乡镇行政区行政区划代码更新
"""

if __name__ == '__main__':
    spider = NovelSpider()
    spider.crawl()
