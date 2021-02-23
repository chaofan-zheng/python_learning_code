from selenium import webdriver

# 1. 打开浏览器，输入百度的地址
driver = webdriver.Chrome(executable_path="/Users/aiden_zcf/PycharmProjects/Tmooc/chromedriver")
driver.get(url='http://www.baidu.com')
# 2. 找到搜索框节点，并发送关键字：高圆圆
search_obj = driver.find_element_by_xpath('//*[@id="kw"]')
search_obj.send_keys('高圆圆')
# 3. 找到百度一下，并点击确认
driver.find_element_by_xpath('//*[@id="su"]').click()
# 关闭浏览器
driver.quit()
