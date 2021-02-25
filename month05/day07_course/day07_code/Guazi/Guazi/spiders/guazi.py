import scrapy
from ..items import GuaziItem


class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['www.guazi.com']
    start_urls = ['https://www.guazi.com/tj/buy/']
    url = 'https://www.guazi.com/tj/buy/o{}/#bread'

    def start_requests(self):
        """生成所有要抓取的URL地址，一次性交给调度器"""
        for page in range(1, 6):
            page_url = self.url.format(page)
            # 交给调度器入队列
            yield scrapy.Request(url=page_url, callback=self.parse)

    def parse(self, response):
        """一级页面的解析函数"""
        # 解析提取汽车数据
        li_list = response.xpath('//ul[@class="carlist clearfix js-top"]/li')
        for li in li_list:
            # 给items.py中的GuaziItem类实例化
            item = GuaziItem()
            # scrapy1.5以后的版本，不用item.title了，要用字典item['title']
            # 变量名要和items.py中高度一致
            item['title'] = li.xpath('./a/@title').get()
            item['price'] = li.xpath('.//div[@class="t-price"]/p/text()').get()
            item['href'] = 'https://www.guazi.com' + li.xpath('./a/@href').get()
            # 详情页链接继续交给调度器入队列
            # meta参数：在不同的解析函数之间传递数据
            # meta会随着url一起入队列，meta作为response属性传回来了，进入到callback对应的函数
            yield scrapy.Request(url=item['href'],
                                 meta={'item': item},
                                 callback=self.parse_second_page)

    def parse_second_page(self, response):
        # 接受上个解析函数中传递过来的item对象
        item = response.meta['item']
        item['km'] = response.xpath('//ul[@class="assort clearfix"]/li[2]/span/text()').get()
        item['displace'] = response.xpath('//ul[@class="assort clearfix"]/li[3]/span/text()').get()
        item['typ'] = response.xpath('//ul[@class="assort clearfix"]/li[4]/span/text()').get()

        # 至此，一辆完整的汽车信息提取完成，交给管道
        yield item

# 一个函数中有yield语句，这个函数当成生成器来使用
# yield语句能够让函数先暂停再后续执行
# yield 是实现协程的关键字
# 进程 线程 协程
# 协程： 纤程， 微线程，是一个比线程还要小的执行单元
# 协程能够在线程当中来回切换
# 实现协程：
# yielf语句是实现协程的关键字
# greenlet gevent
