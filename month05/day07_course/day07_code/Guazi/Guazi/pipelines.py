# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import pymongo


class GuaziMysqlPipeline:
    def open_spider(self, spider):
        """爬虫项目启动时，只执行一次，一般用于数据库的连接"""
        self.db = pymysql.connect(
            'localhost', 'root', '417355570azcfqgg', 'cardb', charset='utf8'
        )
        self.cur = self.db.cursor()
        self.ins = 'insert into cartab values(%s,%s,%s)'

    def process_item(self, item, spider):
        # 把抓取的数据处理成列表
        li = [v for k, v in item.items()]
        self.cur.execute(self.ins, li)
        self.db.commit()
        return item

    def close_spider(self, spider):
        """爬虫项目结束时，只执行一次，一般用于数据库断开"""
        self.cur.close()
        self.db.close()


class GuaziMongoPipeline:
    def open_spider(self, spider):
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['guaziScrapyDB']
        self.set = self.db['guaziScrapySet']

    def process_item(self, item, spider):
        # 把抓取的数据处理成列表
        self.set.insert_one(dict(item))
        return item


class GuaziPipeline:
    def process_item(self, item, spider):
        print(item['title'])
        return item
    # 管道2，将数据存入mysql
    # create database cardb charset utf8;
    # use cardb;
    # create table cartab(
    # name varchar(200),
    # price varchar(100),
    # url varchar(500)
    # )charset=utf8;
