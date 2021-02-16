"""
向京东官网发请求，拿到响应内容即可
"""
import requests

# resp = requests.get(url='https://www.jd.com/')
# res = resp
# print(res)
# # res = resp.text
# print(res)
# res = resp.content # 二进制
# print(res)
# res = resp.status_code
# print(res)
# res = resp.url# 实际数据的url（重定向之后的url）
# print(res)

# 测试网站
url = 'http://httpbin.org/get'
res = requests.get(url=url)
html = res.text
print(html)

# 包装User-Agent
url = 'http://httpbin.org/get'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
                         ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
res = requests.get(url=url, headers=headers).text
print(res)
