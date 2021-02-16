"""笔趣阁小说爬虫"""
import requests
import re
import time
import random
import pymysql


class NovelSpider:
    def __init__(self):
        self.url = 'https://www.biqukan.cc/fenlei1/{}.html'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
                                      ' AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
        self.db = pymysql.connect('localhost', 'root', '417355570', 'noveldb', charset='utf8')
        self.cur = self.db.cursor()

    def get_html(self, url):
        html = requests.get(url, headers=self.headers).content.decode('gbk', 'ignore')
        return self.parse_html(html)

    def parse_html(self, html):
        target_re = '<div class="caption">.*?<a href="(.*?)" title="(.*?)">.*?<small class="text-muted fs-12">(.*?)</small><p class="text-muted fs-12 hidden-xs">(.*?)</p></div>'
        rlist = re.findall(target_re, html, re.S)
        return rlist

    def save_html(self, rlist):
        # with open('小说.txt', 'a') as f:
        #     for r in rlist:
        #         title = r[1]
        #         href = r[0]
        #         author = re.findall('(.*?) / 著', r[2], re.S)[0]
        #         description = r[3].strip()
        #         f.write(f'小说名称:{title} 小说连接：{href} 小说作者：{author} 小说描述{description}\n')

        for r in rlist:
            ins = 'insert into novel_tab values(%s,%s,%s,%s)'
            title = r[1]
            href = r[0]
            author = re.findall('(.*?) / 著', r[2], re.S)[0]
            description = r[3].strip()
            list01 = [title,href,author,description]
            self.cur.execute(ins, list01)
            self.db.commit()

    def crawl(self, pagen):
        for page in range(1, pagen + 1):
            url = self.url.format(page)
            rlist = self.get_html(url)
            self.save_html(rlist)
            time.sleep(random.randint(1, 2))
        self.cur.close()
        self.db.close()


if __name__ == '__main__':
    novel_spider = NovelSpider()
    novel_spider.crawl(2)
