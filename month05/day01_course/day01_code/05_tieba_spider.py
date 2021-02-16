import time
import random

import requests


# def tieba_spider(keyword, page_start, page_end):
#     url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
#                              ' AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
#     for page in range(page_start, page_end):
#         res = requests.get(url=url.format(keyword, (page - 1) * 50), headers=headers).content.decode(encoding='utf8',
#                                                                                                      errors='ignore')
#         filename = './tieba/{}吧_第{}页.html'.format(keyword, page)
#         with open(filename, 'w') as f:
#             f.write(res)
#
#
# keyword = input('关键字')
# page_start = input('开始页')
# page_end = input('结束页')
# print(keyword,page_start,page_end)
# tieba_spider(keyword, page_start, page_end)
class TieBaSpider:
    def __init__(self):
        self.url = url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
                                      ' AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}

    def get_html(self, url):
        """请求函数"""
        html = requests.get(url=url, headers=self.headers).text
        return html

    def parse_html(self):
        """解析函数"""
        pass

    def save_html(self, filename, html):
        """数据处理"""
        with open(filename, 'w') as f:
            f.write(html)

    def crawl(self):
        """爬虫逻辑函数"""
        name = input('贴吧名：')
        start = int(input('开始页'))
        end = int(input('结束页'))
        for page in range(start, end + 1):
            url = self.url.format(name, (page - 1) * 50)
            html = self.get_html(url)
            filename = './tieba/{}吧_第{}页.html'.format(name, page)
            self.save_html(filename, html)

            time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    spider = TieBaSpider()
    spider.crawl()
