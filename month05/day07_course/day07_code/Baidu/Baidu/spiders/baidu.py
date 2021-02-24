import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        r = response.xpath('/html/head/title/text()')
        # xpath: [<selector>,<selector>]
        # extract() 把列表当中所有的选择器提取成unicode字符串                      ['百度一下，你就知道']
        print(r.extract())
        print(r.extract_first())  # 提取出的是第一个选择器，不是列表，而是字符串     百度一下，你就知道
        print(r.get())  # 等价于extract_first() 记住get就行 要么是一个字符串，要么是None           百度一下，你就知道
        # respones的方法以及属性
        html = response.text  # 获取响应内容，而不是selenium的渲染后的页面
        html = response.body  # 获取二进制的响应内容，相当于requests模块中的content



