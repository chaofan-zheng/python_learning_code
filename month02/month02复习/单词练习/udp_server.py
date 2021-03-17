"""
练习2. 基于udp循环收发程序完成

在客户端输入单词，从服务端那里得到单词解释
并打印出来，要求多个客户端可以一起查询

服务端，利用数据库dict->words表 帮助
客户端完成单词查询，将解释发送给客户端
"""
from socket import *
import pymysql


class Database:
    """用于和数据库之间的交互"""
    database_args = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "417355570azcfqgg",
        "database": "dict",
        "charset": "utf8"
    }

    def __init__(self):
        self.db = pymysql.connect(**Database.database_args)  # **kwargs 使用时，字典传餐实参需要拆参
        self.cur = self.db.cursor()

    def get_word(self, word):
        self.cur.execute('select mean from dict where word = %s', [word])
        mean = self.cur.fetchone()  # 获取查询结果集的第一条数据，查找到返回一个元组，否则返回None
        if mean:
            mean = mean[0]
        else:
            mean = 'Not Found'
        return mean

    def close(self):  # 封装这个是为了在下面udp连接的时候可以最后关掉，不用频繁关闭
        self.cur.close()
        self.db.close()


class QueryWord():
    """处理udp连接"""

    def __init__(self):
        self.udp_socket = socket(AF_INET, SOCK_DGRAM)
        self.udp_socket.bind(('127.0.0.1', 8888))  # 记住不要少括号
        self.db = Database()

    def query_word(self):
        while True:
            data, addr = self.udp_socket.recvfrom(1024)
            mean = self.db.get_word(data.decode())
            self.udp_socket.sendto(mean.encode(), addr)
    # 还可以设计成一起推出，客户端发送'##'就退出
    # 这种情况是不会一起退出的，客户端退出了服务器还在等着服务别人


if __name__ == '__main__':
    q = QueryWord()
    q.query_word()
