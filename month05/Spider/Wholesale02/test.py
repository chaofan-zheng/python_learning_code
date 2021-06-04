import os
import pickle
import re
from pprint import pprint
from concurrent.futures import ThreadPoolExecutor
import requests
from fake_useragent import UserAgent
from tqdm import tqdm


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
            resp = requests.get(url=self.test_url, proxies=proxies, headers=UserAgent().random, timeout=3)
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
                response = requests.get(url=url, headers=UserAgent().random, timeout=1).text
            except:
                print(response)
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
        if os.path.exists('proxies.plk'):
            file = open('proxies.plk','rb')
            self.useful_ip = pickle.loads(file.read())
        else:
            res_ip_list = self.thread_manager()
            for proxy in tqdm(res_ip_list,total=len(res_ip_list)):
                self.test_url(proxy)
            with open('proxies.plk','wb') as file:
                file.write(pickle.dumps(self.useful_ip))
        print(f'*************************构建代理ip池完成，可用ip{len(self.useful_ip)}个*************************')

if __name__ == '__main__':
    proxy_pool = ProxyPool()

