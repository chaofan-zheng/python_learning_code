# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
import pymysql
from itemadapter import ItemAdapter


class DoubanPipeline:
    def process_item(self, item, spider):
        print(dict(item))
        return item


class DoubanMysqlPipeline:
    def open_spider(self,spider):
        self.db = pymysql.connect('localhost', 'root', '417355570azcfqgg', 'doubandb', charset='utf8')
        self.cur = self.db.cursor()
        self.ins = 'insert into doubantab values(%s,%s,%s)'

    def process_item(self, item, spider):
        self.cur.execute(self.ins, [v for k, v in item.items()])
        self.db.commit()
        return item

    def close_spider(self,spider):
        self.cur.close()
        self.db.close()


class DoubanMongoPipeline:
    def open_spider(self,spider):
        self.conn = pymongo.MongoClient('localhost',27017)
        self.db = self.conn['doubanDB']
        self.set = self.db['doubanSet']

    def process_item(self, item, spider):
        self.set.insert_one(dict(item))
        return item


