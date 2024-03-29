import json
from urllib.parse import urlencode
from ..items import WholesaleItem
import scrapy
import re
from concurrent.futures import ThreadPoolExecutor
import requests
from fake_useragent import UserAgent
from tqdm import tqdm

class WholesaleSpider(scrapy.Spider):
    name = 'wholesale'
    allowed_domains = ['1688.com']
    start_urls = ['http://1688.com/']

    # url = 'https://search.1688.com/service/marketOfferResultViewService?keywords=%C5%AE%D7%B0&beginPage={}'
    base_url = 'https://search.1688.com/service/marketOfferResultViewService?'

    def start_requests(self):
        keyword = input('请输入关键字：')
        params2 = {'keywords': f'{keyword}'}
        url2 = self.base_url + urlencode(params2, encoding='gbk') + '&beginPage={}'
        for page in range(1, 51):
            page_url = url2.format(page)
            print(page_url)
            yield scrapy.Request(url=page_url,headers=UserAgent.random , callback=self.first_parse)

    def first_parse(self, response):
        '''解析提取女装的数据'''
        html = json.loads(response.text)
        offer_list = html['data']['data']['offerList']
        # print(html)
        for one_html in offer_list:
            item = WholesaleItem()
            item['title'] = one_html['information']['simpleSubject']
            item['price'] = one_html['tradePrice']['offerPrice']['valueString']
            item['rePurchaseRate'] = one_html['information']['rePurchaseRate']
            try:
                item['integer'] = one_html['tradeQuantity']['gmvValue']['integer']
            except:
                item['integer']=''
            href = one_html['information']['detailUrl']
            # yield scrapy.Request(url=href, callback=self.parse_second, meta={'item': item})
            yield item

    def parse_second(self, response):
        item = response.meta['item']
        item['express_fee'] = response.xpath(
            '//div[@class="cost-entries"]/div[@class="cost-entries-type"]//p[2]/em/text()').get()
        yield item


class ProxyPool:
    """
    使用快代理网站中的免费代理
    """

    def __init__(self):
        # self.api_url = 'http://dev.kdlapi.com/api/getproxy/?orderid=999955248138592&num=20&protocol=2&method=2&an_ha=1&sep=1' # 隧道代理
        self.free_url = 'https://www.kuaidaili.com/free/inha/{}/'  # 免费代理
        self.test_url = 'http://httpbin.org/get'
        self.headers = {
            'User-Agent': UserAgent().random}
        self.useful_ip = []
        self.run()

    def get_proxy(self):
        html = requests.get(url=self.api_url, headers=self.headers).text
        proxy_list = html.split('\r\n')
        # print(proxy_list)
        for proxy in proxy_list:
            self.test_proxy(proxy)

    def test_proxy(self, proxy):
        proxies = {
            'http': 'http://{}'.format(proxy),
            'https': 'https://{}'.format(proxy),
        }
        try:
            resp = requests.get(url=self.test_url, proxies=proxies, headers=self.headers, timeout=3)
            # print(f'{proxy}可用！！！！')
            self.useful_ip.append(proxy)
        except Exception as e:
            # print(f'{proxy}不可用')
            pass

    def thread_manager(self):
        res_ip_list = []  # 最后得到的所有免费的ip
        with ThreadPoolExecutor(max_workers=48) as executor:
            for i in range(1, 4001, 100):
                executor.submit(self.get_ip, i, i+100, res_ip_list)
        print(f'共获取待测试ip{len(res_ip_list)}个ip')
        return res_ip_list

    def get_ip(self, start, end, res_ip_list):
        """ 爬取免费代理的ip """
        for i in range(start, end):
            url = self.free_url.format(i)
            try:
                response = requests.get(url=url, headers=self.headers, timeout=2).text
            except:
                continue
            # print(response)
            ip_list = re.findall('<td data-title="IP">(.*?)</td>', response)
            port_list = re.findall('<td data-title="PORT">(.*?)</td>', response)
            if len(ip_list) != len(port_list):
                continue
            for i in range(len(ip_list)):
                res_ip_list.append(ip_list[i] + ':' + port_list[i])
        print(f'共获取待测试ip{len(res_ip_list)}个ip')
        # return res_ip_list

    def run(self):
        print('*************************构建代理ip池开始*************************')
        print('*************************构建代理ip中*************************')
        res_ip_list = self.thread_manager()
        for proxy in tqdm(res_ip_list,total=len(res_ip_list)):
            self.test_url(proxy)


if __name__ == '__main__':
    proxy_pool = ProxyPool()
    print(proxy_pool.useful_ip)
