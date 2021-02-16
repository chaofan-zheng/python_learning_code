"""
输入关键字，形成爬虫
"""
import requests


def baidu_spider(keyword):
    url = 'http://tieba.baidu.com/s?wd={}'.format(keyword)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
                             ' AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
    html = requests.get(url, headers=headers).text
    filename = '{}.html'.format(keyword)
    with open(filename, 'w') as f:
        f.write(html)

    # url = 'https://www.baidu.com/s?wd={}'.format(keyword)
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
    #                          ' AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}
    # html = requests.get(url, headers=headers).text
    # filename = '{}.html'.format(keyword)
    # with open(filename, 'w') as f:
    #     f.write(html)


if __name__ == '__main__':
    keyword = input('请输入关键字')
    baidu_spider(keyword)
