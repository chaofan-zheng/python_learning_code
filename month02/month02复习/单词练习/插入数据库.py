import re
import pymysql

db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='417355570azcfqgg', database='dict',
                     charset='utf8')
cur = db.cursor()

with open('dict.txt') as f:
    try:
        for line in f:
            res = re.findall(r'(\w+)\s(.*)', line)[0]
            word = res[0].strip()
            mean = res[-1].strip()
            cur.execute(f'insert into dict(word,mean) values(%s,%s)', [word, mean])
        db.commit()
    except Exception as e:
        db.rollback()
        print('程序出错已退回')
        print(e)

    cur.close()
    db.close()
