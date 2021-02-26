"""
将图片抓取到本地
"""
import requests
from fake_useragent import UserAgent

image_url = 'https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201902%2F18%2F20190218114647_shmed.jpg&refer=http%3A%2F%2Fb-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1616508734&t=29f0012c8083db1c6fad51bf2ec22572'
headers = {'User-Agent': UserAgent().random}
image_html = requests.get(url=image_url, headers=headers).content
with open('girl.jpg', 'wb') as f:
    f.write(image_html)
