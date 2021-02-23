"""
民政部最新行政区划代码数据抓取
"""
from selenium import webdriver
import time
import redis
from hashlib import md5
import sys


class MzbSpider:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(executable_path="/Users/aiden_zcf/PycharmProjects/Tmooc/chromedriver",
                                       options=self.options)
        self.driver.get(url='http://www.mca.gov.cn/article/sj/xzqh/2020/')
        self.r = redis.Redis(host='localhost', port='6379', db=0)

    def parse_html(self):
        new_month_a = self.driver.find_element_by_xpath(
            '//*[@id="list_content"]/div[2]/div/ul/table/tbody/tr[1]/td[2]/a')
        href = new_month_a.get_attribute('href')
        finger = self.md5_href(href)
        if self.r.sadd('mzb:spider', finger) == 1:
            new_month_a.click()
            # 切换句柄
            time.sleep(2)  # 给句柄的加载预留时间
            li = self.driver.window_handles
            self.driver.switch_to.window(li[1])
            self.get_data()  # 写一个函数去提取数据
            self.driver.quit()

        else:
            sys.exit('更新完成')

    def md5_href(self, href):
        """md5加密的功能函数"""
        m = md5()
        m.update(href.encode())
        return m.hexdigest()

    def get_data(self):
        tr_list = self.driver.find_elements_by_xpath('//tr[@height="19"]')
        for tr in tr_list:
            item = {}
            li = tr.text.split()
            item['code'] = li[0]
            item['name'] = li[1]
            print(item)


if __name__ == '__main__':
    spider = MzbSpider()
    spider.parse_html()
