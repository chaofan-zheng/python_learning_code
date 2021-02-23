"""
selenium 切换iframe子页面
"""
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(executable_path="/Users/aiden_zcf/PycharmProjects/Tmooc/chromedriver",options=options)
driver.get(url='https://music.163.com/#/discover/toplist')
# 切换iframe
driver.switch_to.frame('g_iframe')
tr_list = driver.find_elements_by_xpath('//table/tbody/tr')
for tr in tr_list:
    # print(tr.text)
    # print('*'*50)
    item = {}
    item['rank'] = tr.find_element_by_xpath('.//span[@class="num"]').text
    item['title'] = tr.find_element_by_xpath('.//span[@class="txt"]/a/b').get_attribute('title').replace('\xa0',' ')
    item['time'] = tr.find_element_by_class_name('u-dur ').text
    item['star'] = tr.find_element_by_xpath('.//div[@class="text"]/span').get_attribute('title')
    print(item)
driver.quit()