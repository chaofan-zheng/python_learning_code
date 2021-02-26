"""
使用selenium进入百度的搜索页面
"""
# 导入selenium的webdriver接口
from selenium import webdriver

# 打开浏览器 - 创建浏览器对象
driver = webdriver.Chrome(executable_path="/Users/aiden_zcf/PycharmProjects/Tmooc/chromedriver")
# 在地址栏输入百度的URL地址
driver.get(url='http://www.baidu.com')
