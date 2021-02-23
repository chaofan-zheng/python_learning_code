"""
【1】使用selenium+浏览器 获取有道翻译结果
	提示:1.text属性
         2.注意time.sleep()
"""
from selenium import webdriver
import time


class YouDaoSpider:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="/Users/aiden_zcf/PycharmProjects/Tmooc/chromedriver")
        self.driver.get('http://fanyi.youdao.com/')

    def crawl(self, target_word):
        input_box = self.driver.find_element_by_xpath('//*[@id="inputOriginal"]')
        input_box.send_keys(f'{target_word}')
        time.sleep(2)
        output_box = self.driver.find_element_by_xpath('//*[@id="transTarget"]')
        res = output_box.text
        print('result:', res)


if __name__ == '__main__':
    spider = YouDaoSpider()
    spider.crawl("hello")
