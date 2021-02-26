"""
库名:noveldb
集合名:novelset
文档:{'name':'大空翼','hobby':'踢足球'}
"""
import pymongo

conn = pymongo.MongoClient('localhost', 27017)
db = conn['noveldb']
myset = db['novelset']
myset.insert_one({'name': '大空翼', 'hobby': '踢足球'})
