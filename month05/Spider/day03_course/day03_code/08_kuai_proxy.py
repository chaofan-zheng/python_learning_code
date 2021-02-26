import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent


class KuaiProxy:
    def __init__(self):
        self.url = 'https://www.kuaidaili.com/free/inha/{}/'
        self.headers = {'User-Agent': UserAgent().random}
        self.test_url = 'http://httpbin.org/get'
        self.ip_pool = []

    def get_proxy(self, url):
        html = requests.get(url=url, headers=self.headers).text
        self.parse_html(html)

    def parse_html(self, html):
        eobj = etree.HTML(html)
        td_list = eobj.xpath('//table//tr')
        for td in td_list:
            item = {}
            anonymity_list = td.xpath('./td[@data-title="IP"]/text()')
            item['anonymity'] = anonymity_list[0] if anonymity_list else None
            if anonymity_list == "高匿名":
                ip_list = td.xpath('./td[@data-title="IP"]/text()')
                item['ip'] = ip_list[0] if ip_list else None

                port_list = td.xpath('./td[@data-title="PORT"]/text()')
                item['port'] = port_list[0] if port_list else None
                print(item)
                self.test_proxy(item)
            else:
                continue
        print(self.ip_pool)

    def test_proxy(self, item):
        proxies = {
            'http': f"http://{item['ip']}:{item['port']}",
            'https': f"https://{item['ip']}:{item['port']}",
        }
        try:
            html = requests.get(url=self.test_url, headers=self.headers, proxies=proxies, timeout=3).text
        except:
            print('ip不可用')
        self.ip_pool.append(item['ip'] + ':' + item['port'])
        print(self.ip_pool)

    def crawl(self):
        for page in range(1, 1000):
            url = self.url.format(page)
            self.get_proxy(url)
            time.sleep(random.randint(1,2))


if __name__ == '__main__':
    spider = KuaiProxy()
    spider.crawl()
