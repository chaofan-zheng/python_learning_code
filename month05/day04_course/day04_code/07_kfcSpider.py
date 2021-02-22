"""
【1】肯德基餐厅门店信息抓取（POST请求练习）
    1.1) URL地址: http://www.kfc.com.cn/kfccda/storelist/index.aspx
    1.2) 所抓数据: 餐厅编号、餐厅名称、餐厅地址、城市
    1.3) 数据存储: 保存到数据库
    1.4) 程序运行效果：
         请输入城市名称：北京
         把北京的所有肯德基门店的信息保存到数据库中
"""
import csv
import random
import time
import pymongo
import requests


class KfcSpider:
    def __init__(self):
        self.post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
        self.headers = {
            '''Accept''': '''application/json, text/javascript, */*; q=0.01''',
            '''Accept-Encoding''': '''gzip, deflate''',
            '''Accept-Language''': '''en,zh;q=0.9,zh-CN;q=0.8''',
            '''Connection''': '''keep-alive''',
            '''Content-Length''': '''53''',
            '''Content-Type''': '''application/x-www-form-urlencoded; charset=UTF-8''',
            '''Cookie''': '''route-cell=ksa; SERVERID=a8ef50e74cdb73da974d5f9b427a5159|1614005989|1614005807''',
            '''Host''': '''www.kfc.com.cn''',
            '''Origin''': '''http://www.kfc.com.cn''',
            '''Referer''': '''http://www.kfc.com.cn/kfccda/storelist/index.aspx''',
            '''User-Agent''': '''Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36''',
            '''X-Requested-With''': '''XMLHttpRequest''',
        }
        self.conn = pymongo.MongoClient('localhost',27017)
        self.db=self.conn['kfcDB']
        self.set = self.db['kfcSet']

        self.f = open('kfc.csv','w')
        self.writer = csv.writer(self.f)

    def get_html(self, url, cname, pageIndex):
        data = self.make_data(cname, pageIndex)
        html = requests.post(url=url, headers=self.headers, data=data).json()
        for table1 in html['Table1']:
            item = {}
            item['storeNum'] = table1['rownum']
            item['storeAddress'] = table1['addressDetail']
            item['storeName'] = table1['storeName']
            item['cityName'] = table1['cityName']
            print(item)
            self.save_data(item)

    def make_data(self, cname, pageIndex):
        data = {
            'cname': cname,
            'pid': '',
            'pageIndex': pageIndex,
            'pageSize': '10',
        }
        return data

    def get_row_count(self, cname):
        data = self.make_data(cname, pageIndex=1)
        html = requests.post(url=self.post_url, headers=self.headers, data=data).json()
        row_count = html['Table'][0]['rowcount']
        pagen = int(row_count / 10) + 1
        return pagen

    def crawl(self):
        cname = input('请输入城市名字')
        pagen = self.get_row_count(cname)
        for page in range(1, pagen + 1):
            self.get_html(url=self.post_url, cname=cname, pageIndex=page)
            time.sleep(random.uniform(0, 2))
        self.f.close()

    def save_data(self,item):
        self.set.insert_one(item)
        self.writer.writerow([v for k,v in item.items()])




if __name__ == '__main__':
    spider = KfcSpider()
    spider.crawl()
