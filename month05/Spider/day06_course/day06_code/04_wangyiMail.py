"""
【2】使用selenium+浏览器 登录网易163邮箱 : https://mail.163.com/
"""
from selenium import webdriver


class WangyiSpider:
    def __init__(self):
        # self.options = webdriver.ChromeOptions()
        # self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(executable_path="/Users/aiden_zcf/PycharmProjects/Tmooc/chromedriver")
        self.driver.get('https://mail.163.com/')

    def crawl(self):
        # 方法一 因为是第一个，所以可以直接find_element
        frame = self.driver.find_element_by_tag_name('iframe')
        # 方法二
        frame = self.driver.find_element_by_xpath('//div[@id="loginDiv"]/iframe')
        self.driver.switch_to.frame(frame)
        input_name = self.driver.find_element_by_xpath('.//input[@data-placeholder="邮箱帐号或手机号码"]')
        input_password = self.driver.find_element_by_xpath('.//input[@data-placeholder="输入密码"]')
        input_name.send_keys('123@163.com')
        input_password.send_keys('123456')
        self.driver.quit()


if __name__ == '__main__':
    spider = WangyiSpider()
    spider.crawl()
