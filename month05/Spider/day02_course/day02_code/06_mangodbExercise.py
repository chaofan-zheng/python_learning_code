import pymongo

conn = pymongo.MongoClient('localhost', 27017)
db = conn['guazidb']
set = db['guaziset']
set.insert_one({'title': 'Tesla Model Y', 'km': '594km', 'price': '33.99万'})
