from threading import Thread
from queue import Queue


class XxxSpider:
    def __init__(self):
        self.url = 'http://www.abc.com/page{}.html'
        self.q = Queue()

    def url_to_q(self):
        """
        生成所有的url地址，如队列
        :return:
        """
        for page in range(1, 100001):
            page_url = self.url.format(page)
            self.q.put(page_url)

    def parse_url(self):
        """线程事件函数，获取地址，请求解析数据处理"""
        while not self.q.empty():
            url = self.q.get()
            # 拿出来一个地址，向url发送请求，解析、处理数据
            # 多个线程在写同一个文件的时候，会互相争夺资源，解决办法就是使用线程锁
            pass

    def crawl(self):
        # url地址入队列
        self.url_to_q()
        # 创建多线程爬虫,5个线程
        t_list = []
        for i in range(5):
            t = Thread(target=self.parse_url())
            t_list.append(t)
            t.start()

        # 回收线程
        for t in t_list:
            t.join()


if __name__ == '__main__':
    spider = XxxSpider()
    spider.crawl()
