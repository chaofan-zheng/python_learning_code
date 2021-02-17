import requests
import re
import time
import random

class MovieSpider:
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
                                      ' AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}

    def get_html(self, url):
        try:
            html = requests.get(url, headers=self.headers).content.decode('utf-8', 'ignore')
        except Exception as e:
            print(e)
        return html

    def parse_html(self, html):
        target_re = '<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>'
        res = re.findall(target_re, html, re.S)
        list_out = []
        for r in res:
            dict_out = {}
            dict_out['title'] = r[0]
            dict_out['actor'] = r[1].strip()
            dict_out['time'] = r[2].strip()
            list_out.append(dict_out)
        return list_out

    def save_html(self, list_out):
        for item in list_out:
            print(item)

    def crawl(self,pagen):
        for page in range(1,pagen+1):
            url = self.url.format((page-1)*10)
            html = self.get_html(url)
            list_out = self.parse_html(html)
            self.save_html(list_out)
            time.sleep(random.randint(1,2))

if __name__ == '__main__':
    movie_spider = MovieSpider()
    movie_spider.crawl(2)