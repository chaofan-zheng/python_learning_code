import requests

# https://www.guazi.com/hz/buy/o50/#bread
# url = 'https://www.guazi.com/hz/buy/o{}/#bread'
# for page in range(1,51):
#     page_url = url.format(page)
#     print(page_url)

# https://www.baidu.com/s?wd=张靓颖&pn=170
url = 'https://www.baidu.com/s?wd=张靓颖&pn={}'
for page in range(1,101):
    page_url = url.format((page-1)*10)
    print(page_url)