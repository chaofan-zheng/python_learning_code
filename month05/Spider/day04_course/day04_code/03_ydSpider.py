import hashlib
import json
import random
import time

import requests


class YoudaoSpider:
    def __init__(self):
        # URL地址一定要是F12抓包抓到的POST地址
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en,zh;q=0.9,zh-CN;q=0.8",
            "Connection": "keep-alive",
            "Content-Length": "336",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "OUTFOX_SEARCH_USER_ID=-2082348340@10.108.160.105; JSESSIONID=aaac-lfLCK6Dke_xMPhFx; OUTFOX_SEARCH_USER_ID_NCOO=215298858.81387576; ___rl__test__cookies=1613964724270",
            "Host": "fanyi.youdao.com",
            "Origin": "http://fanyi.youdao.com",
            "Referer": "http://fanyi.youdao.com/",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }

    def get_translation(self, word):
        lts, salt, sign = self.get_params(word)
        data = {
            "i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "lts": lts,
            "bv": "17972008730c9a8d5c897db09c8e0c15",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
        }
        json_str = requests.post(url=self.url, headers=self.headers, data=data).text
        json_obj = json.loads(json_str)
        # 等同于
        # json_obj = requests.post(url=self.url, headers=self.headers, data=data).json()
        # print(json_obj)
        result = json_obj['translateResult'][0][0]['tgt']
        print(result)

    def get_params(self, word):
        # 获取lts
        lts = str(int(time.time() * 1000))

        # 获取salt
        salt = lts + str(random.randint(0, 9))

        # 获取sign
        md5 = hashlib.md5()
        str01 = "fanyideskweb" + word + salt + "Tbh5E8=q6U3EXe+&L[4c@"
        md5.update(str01.encode())
        sign = md5.hexdigest()
        return lts, salt, sign

    def crawl(self):
        word = input("请输入要爬取的单词")
        self.get_translation(word)

    # def get_bv(self):
    #     md5 = hashlib.md5()
    #     app_version = "5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"
    #     md5.update(app_version.encode())
    #     return


if __name__ == '__main__':
    spider = YoudaoSpider()
    spider.crawl()
