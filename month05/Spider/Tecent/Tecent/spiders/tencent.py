import json
import scrapy
import time
import requests


from ..items import TecentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    first_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={}&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=en-us&area='
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
    second_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp={}&postId={}&num=7&language=en-us'

    def get_timestamp(self):
        timestamp = str(int(time.time() * 1000))
        return timestamp

    def get_pagen(self, timestamp, keyword):
        url = self.first_url.format(timestamp, keyword, 1)
        html = requests.get(url=url, headers=self.headers).json()
        count = html['Data']['Count']
        pagen = count / 10 if count // 10 == 0 else int(count / 10) + 1
        return pagen

    def start_requests(self):
        keyword = input('请输入关键字')
        timestamp = self.get_timestamp()
        pagen = self.get_pagen(timestamp, keyword)
        for page in range(1, pagen + 1):
            page_url = self.first_url.format(timestamp, keyword, page)
            yield scrapy.Request(url=page_url, callback=self.parse_first)

    def parse_first(self, response):
        post_list = json.loads(response.text)['Data']['Posts']
        for post in post_list:
            timestamp = self.get_timestamp()
            post_id = post['PostId']
            href = self.second_url.format(timestamp, post_id)
            yield scrapy.Request(url=href, callback=self.parse_second)

    def parse_second(self, response):
        item = TecentItem()
        item['post_name'] = json.loads(response.text)['Data']['RecruitPostName']
        item['location_name'] = json.loads(response.text)['Data']['LocationName']
        item['category'] = json.loads(response.text)['Data']['CategoryName']
        item['update_time'] = json.loads(response.text)['Data']['LastUpdateTime']
        item['responsibility'] = json.loads(response.text)['Data']['Responsibility']
        item['requirement'] = json.loads(response.text)['Data']['Requirement']
        yield item


if __name__ == '__main__':
    spider = TencentSpider()
    print(spider.get_pagen(spider.get_timestamp(), 'python'))
    # print(spider.get_timestamp())
