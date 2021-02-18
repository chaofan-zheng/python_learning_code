import pymysql
import pymongo
import csv
import requests
import re
import time
import random
import redis


class GuaZiSpider:
    def __init__(self):
        self.url = 'https://www.guazi.com/hz/buy/o{}/#bread'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            'Cookie': 'track_id=177523292806569984; uuid=6ebc3189-7d01-4c0a-e93e-e23a2a101806; antipas=88B3m44974066S379r05382; clueSourceCode=%2A%2300; ganji_uuid=2127355730094556457784; sessionid=b53b6fc9-334c-4155-9a50-ed617c764890; lg=1; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22pcbiaoti%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22%22%2C%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22ca_transid%22%3A%22%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22track_id%22%3A%22177523292806569984%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%226ebc3189-7d01-4c0a-e93e-e23a2a101806%22%2C%22ca_city%22%3A%22hz%22%2C%22sessionid%22%3A%22b53b6fc9-334c-4155-9a50-ed617c764890%22%7D; Hm_lvt_bf3ee5b290ce731c7a4ce7a617256354=1613480054; user_city_id=26; close_finance_popup=2021-02-17; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A77702636874%7D; cityDomain=hz; preTime=%7B%22last%22%3A1613572428%2C%22this%22%3A1613480051%2C%22pre%22%3A1613480051%7D; Hm_lpvt_bf3ee5b290ce731c7a4ce7a617256354=1613572430'
        }
        # mysql 连接
        self.mysql_db = pymysql.connect('localhost', 'root', '417355570', 'noveldb', charset='utf8')
        self.cur = self.mysql_db.cursor()

        # mongoDB连接
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.mongo_db = self.conn['guazidb']
        self.set = self.mongo_db['guaziset']

        # csv
        self.f = open('guazi.csv', 'w')
        self.writer = csv.writer(self.f)

        # redis 连接到第二个库
        self.r = redis.Redis(host='127.0.0.1', port=6379, db=2)

    def get_html(self, url):
        html = requests.get(url, headers=self.headers).content.decode('utf-8', 'ignore')
        return html

    def refunc(self, regex, html):
        rlist = re.findall(regex, html, re.S)
        return rlist

    def parse_html(self, first_url):
        first_html = self.get_html(first_url)
        first_regex = '<li data-scroll-track=.*?<a title=".*?" href="(.*?)"'
        rlist = self.refunc(first_regex, first_html)
        for r in rlist:
            item = {}
            item['href'] = 'https://www.guazi.com' + r.strip()
            print(item['href'])
            self.get_second_data(item['href'], item)

    def get_second_data(self, second_url, item):
        second_html = self.get_html(second_url)
        second_regex = '<h1 class="titlebox">(.*?)<'
        second_rlist = self.refunc(second_regex, second_html)
        for second in second_rlist:
            second_item = {}
            second_item['href'] = item['href']
            second_item['title'] = second.strip()
            print(second_item)
            time.sleep(random.uniform(0, 2))

    def save_mongo(self):
        pass

    def save_mysql(self):
        pass

    def save_csv(self):
        pass

    def crawl(self, pagen):
        for page in range(1, pagen + 1):
            url = self.url.format(page)
            self.parse_html(url)


if __name__ == '__main__':
    spider = GuaZiSpider()
    spider.crawl(1)
