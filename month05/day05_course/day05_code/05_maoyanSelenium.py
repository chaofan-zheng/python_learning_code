from selenium import webdriver

url = "https://maoyan.com/board/4"

# 设置无头模式
options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(executable_path="/Users/aiden_zcf/PycharmProjects/Tmooc/chromedriver",options=options)
driver.get(url=url)


def get_one_page():
    dd_list = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
    for dd in dd_list:
        item = {}
        info_list = dd.text.split('\n')
        item['rank'] = info_list[0].strip()
        item['title'] = info_list[1].strip()
        item['star'] = info_list[2].strip()
        item['time'] = info_list[3].strip()
        item['score'] = info_list[4].strip()
        print(item)


while True:
    get_one_page()
    try:
        next_page = driver.find_element_by_link_text('下一页')
    except Exception as e:
        print(e)
        break
    next_page.click()