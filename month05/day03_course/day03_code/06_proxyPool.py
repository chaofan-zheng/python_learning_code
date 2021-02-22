import requests
from fake_useragent import UserAgent
class ProxyPool:
    def __init__(self):
        self.api_url = 'http://dev.kdlapi.com/api/getproxy/?orderid=999955248138592&num=20&protocol=2&method=2&an_ha=1&sep=1'
        self.test_url = 'http://httpbin.org/get'
        self.headers = {
            'User-Agent': UserAgent().random}

    def get_proxy(self):
        html = requests.get(url=self.api_url,headers = self.headers).text
        proxy_list = html.split('\r\n')
        # print(proxy_list)
        for proxy in proxy_list:
            self.test_proxy(proxy)

    def test_proxy(self,proxy):
        proxies = {
            'http':'http://{}'.format(proxy),
            'https':'https://{}'.format(proxy),
        }
        try:
            resp = requests.get(url=self.test_url,proxies=proxies,headers = self.headers, timeout=3)
            print(proxy,'可用')
        except:
            print(proxy,'不可用')


