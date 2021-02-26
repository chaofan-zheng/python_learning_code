"""
抓取豆瓣电影排行榜
"""
import re

import requests
import time
import random
from fake_useragent import UserAgent
import json


class DoubanSpider:
    def __init__(self):
        self.get_js_url = 'https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start={}&limit=20'
        self.index_url = 'https://movie.douban.com/chart'
        self.get_total_url = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90'

    def get_html(self, url):
        headers = {'User-Agent': UserAgent().random}
        html = requests.get(url=url, headers=headers).text
        return html

    def parse_js_html(self, url):
        html = self.get_html(url=url)
        html = json.loads(html)
        for one_file_dict in html:
            item = {}
            item['rank'] = one_file_dict['rank']
            item['title'] = one_file_dict['title']
            item['score'] = one_file_dict['score']
            item['time'] = one_file_dict['release_date']
            print(item)

    def get_total(self, url):
        html = self.get_html(url=url)
        json_obj = json.loads(html)
        total = json_obj['total']
        return total

    def get_category(self, category):
        regex = '''<span><a href="(.*?)">{}</a></span>'''.format(category)
        html = self.get_html(self.index_url)
        href = re.findall(regex, html)[0]
        return re.findall('type=(.*?)&', href, re.S)[0]

    def crawl(self):
        category = input("""请输入电影的种类
        剧情,喜剧,动作,爱情,科幻,动画,悬疑,惊悚,恐怖,纪录片,短片,情色,同性,音乐,歌舞,家庭,儿童,传记,历史,战争,犯罪,西部,奇幻,冒险,灾难,武侠,古装,运动,黑色电影
        """)
        type = self.get_category(category)
        total = self.get_total(self.get_total_url.format(type))
        for start in range(1,total,20):
            url = self.get_js_url.format(type, start)
            # print(url)
            self.parse_js_html(url)
            time.sleep(random.uniform(0,2))



if __name__ == '__main__':
    spider = DoubanSpider()
    spider.crawl()
