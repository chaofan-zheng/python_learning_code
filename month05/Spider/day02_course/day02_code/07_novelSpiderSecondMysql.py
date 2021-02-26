"""
两集页面的数据抓取
"""
import requests
import re
import time
import random
import pymysql


class NovelSpider:
    def __init__(self):
        self.url = 'https://www.biqukan.cc/fenlei1/{}.html'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'}
        self.db=pymysql.connect('localhost', 'root', '417355570', 'noveldb', charset='utf8')
        self.cur = self.db.cursor()

    def get_html(self, url):
        """请求,发请求获取响应内容html"""
        html = requests.get(url=url, headers=self.headers).content.decode('gbk', 'ignore')
        # 直接调用解析函数
        return html

    def refunc(self, regex, html):
        """正则解析功能函数"""
        r_list = re.findall(regex, html, re.S)
        return r_list

    def parse_html(self, first_url):
        first_html = self.get_html(url=first_url)
        first_regex = '<div class="caption">.*?href="(.*?)" title="(.*?)">.*?<small class="text-muted fs-12">(.*?)</small>.*?>(.*?)</p>'
        first_list = self.refunc(first_regex, first_html)
        for first in first_list:
            item = {}
            item['href'] = first[0]
            item['title'] = first[1]
            item['author'] = first[2]
            item['comment'] = first[3]
            # 继续向item['href']发请求
            self.get_novel_data(item)
            # 控制数据抓取频率
            time.sleep(random.uniform(0, 2))  # 生成浮点数

    def get_novel_data(self, item):
        second_html = self.get_html(url=item['href'])
        second_regex = '<dd class="col-md-4">.*?<a href="(.*?)">(.*?)</a></dd>'
        second_list = self.refunc(second_regex, second_html)
        for second in second_list:
            one_chapter_dict = {}
            one_chapter_dict['chapter_name'] = second[1]
            one_chapter_dict['chapter_href'] = second[0]
            one_chapter_dict['href'] = item['href']
            one_chapter_dict['title'] = item['title']
            one_chapter_dict['author'] = item['author']
            one_chapter_dict['comment'] = item['comment']
            ins = 'insert into novel_tab2 values(%s,%s,%s,%s,%s,%s)'
            self.cur.execute(ins,[v for k,v in one_chapter_dict.items()])


    def crawl(self):
        """爬虫逻辑函数"""
        for page in range(1, 2):
            page_url = self.url.format(page)
            self.parse_html(page_url)


if __name__ == '__main__':
    spider = NovelSpider()
    spider.crawl()
