"""
免费代理测试
"""
import requests
from fake_useragent import UserAgent

url = "http://httpbin.org/get"
headers = {'User-Agent': UserAgent().random}
proxies = {
    'http': 'http://180.118.128.58:9000',
    'https': 'https://180.118.128.58:9000'
}
html = requests.get(url=url, headers=headers, proxies=proxies).text
print(html)
