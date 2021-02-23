import time

from selenium import webdriver
class JDSpider:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="/Users/aiden_zcf/PycharmProjects/Tmooc/chromedriver")
        self.driver.get(url='https://www.jd.com/')
        self.driver.find_element_by_xpath('//*[@id="key"]').send_keys("爬虫书")
        self.driver.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
        time.sleep(2)

    def get_one_page(self):
        """获取商品数据"""
        # 先拉动滚动条到最底部，让所有商品加载出来
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        li_list = self.driver.find_elements_by_xpath('//div[@id="J_goodsList"]/ul/li')
        for li in li_list:
            # print(li.text)
            # print("*"*50)
            item={}
            item['title']=li.find_element_by_xpath('.//div[@class="p-name"]/a/em').text
            item['price']=li.find_element_by_xpath('.//div[@class="p-price"]').text
            print(item)

    def crawl(self):
        while True:
            self.get_one_page()
            try:
                next =self.driver.find_element_by_xpath('//span[@class="p-num"]/a[@class="pn-next"]')
            except:
                break
            next.click()
            time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    spider =JDSpider()
    spider.crawl()