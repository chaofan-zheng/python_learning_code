import json
from urllib.parse import urlencode
from ..items import WholesaleItem
import scrapy
import os
import pickle
import re
from pprint import pprint
from concurrent.futures import ThreadPoolExecutor
import requests
from fake_useragent import UserAgent
from tqdm import tqdm
import random


class WholesaleSpider(scrapy.Spider):
    """ 若无效，请修改session_id 和cookies
    访问https://search.1688.com/service/marketOfferResultViewService?keywords=%C5%AE%D7%B0&beginPage={}，
    抓marketOfferResult包"""

    session_id = '&sessionId=34f4204061454344809a9823c67e847e&_bx-v=1.1.20'
    cookies = 'cna=p4vBF6s8S3cCAXAObY5XttFY; ali_ab=39.182.24.103.1618932554145.6; UM_distinctid=178f5153fea28-036f6ed467d773-336b7c08-13c680-178f5153feb3b6; taklid=d4507764513b496b9b000351f3bea4cd; xlly_s=1; _csrf_token=1622818047389; cookie2=163a1ebe056292a5aa941755f8a5b948; hng=CN%7Czh-CN%7CCNY%7C156; t=8d064fb0a2fa048852103cf49cedca1f; _tb_token_=e7a733853ee35; _m_h5_tk=cf8ae4b8b4f2cdf630ecb20cc0b23744_1622883194673; _m_h5_tk_enc=6c880164d83c00ebe56ea71751cd98cc; __cn_logon_id__=tb0914271979; __last_loginid__=tb0914271979; __cn_logon__=true; last_mid=b2b-2211891736071b5ea9; cookie1=WvKepWWrQxKfHl2wCCOEvqEUUIK5tco8jBie84BguHw%3D; cookie17=UUpgR1rU58qns8tRQw%3D%3D; sg=916; csg=3b01b352; lid=tb0914271979; unb=2211891736071; uc4=id4=0%40U2gqyOcE8QTp3GJJmkN3ctXDXUbtJhQ8&nk4=0%40FY4O4HNXCj0Bj1pVpmbjD39Vhl4KWtk%3D; ali_apache_track=c_mid=b2b-2211891736071b5ea9|c_lid=tb0914271979|c_ms=1; ali_apache_tracktmp=c_w_signed=Y; _nk_=tb0914271979; _is_show_loginId_change_block_=b2b-2211891736071b5ea9_false; _show_force_unbind_div_=b2b-2211891736071b5ea9_false; _show_sys_unbind_div_=b2b-2211891736071b5ea9_false; _show_user_unbind_div_=b2b-2211891736071b5ea9_false; __rn_alert__=false; keywordsHistory=%E5%A5%B3%E8%A3%85; alicnweb=touch_tb_at%3D1622874916888%7Clastlogonid%3Dtb0914271979%7Cshow_inter_tips%3Dfalse; tfstk=cl2PB0XcKv4fUDkC6YMeVhQxl4WRajwgpEoIZS7BhDdFv1mE7sjMJmqNPjlsWtcl.; l=eBjAKrdqjB4VkhSkBOfanurza77OYIRYjuPzaNbMiOCPsu5J56-FW6_GVaTvCnhNh6mJR37q3EJuBeYBchYRDNPbydDOgpDmn; isg=BD4-TIii0lLaiwaz6_2dTTdTj1KAfwL5W-NXGehHywF8i95lUA2tCWZhAl9HjvoR'
    while True:
        name = 'wholesale'
        allowed_domains = ['1688.com']
        start_urls = ['http://1688.com/']
        # url = 'https://search.1688.com/service/marketOfferResultViewService?keywords=%C5%AE%D7%B0&beginPage={}&sessionId=34f4204061454344809a9823c67e847e&_bx-v=1.1.20'
        base_url = 'https://search.1688.com/service/marketOfferResultViewService?'
        keyword = input('请输入想要批发的货物名称（准确填写一种货物）：')
        if re.findall("[`~!@#-_$%^&*()+=|{}':;',\\[\\]<>/?~！@#￥%……&*（）——+|{}【】《》 ‘；：”“’。，、？]", keyword):
            print('请输入合法字符')
            continue
        break
        # a = ProxyPool()
        # proxypool = a.useful_ip

    def start_requests(self):
        params2 = {'keywords': f'{self.keyword}'}
        url2 = self.base_url + urlencode(params2, encoding='gbk') + '&beginPage={}' + self.session_id
        # print(url2)
        for page in range(1, 51):
            page_url = url2.format(page)
            # print(page_url)
            response = scrapy.Request(url=page_url, headers={'User-Agent': UserAgent().random,
                                                             'cookie': self.cookies},
                                      callback=self.first_parse)
            print(response)
            yield response

    def first_parse(self, response):
        '''解析提取女装的数据'''
        try:
            html = json.loads(response.text)
            offer_list = html['data']['data']['offerList']
        except Exception as e:
            # print(html)
            print('cookies过期，请登录并且替换程序中的session_id与cookies')
            return
        # print(html)
        for one_html in offer_list:
            item = WholesaleItem()
            item['rePurchaseRate'] = one_html['information']['rePurchaseRate']
            item['price'] = one_html['tradePrice']['offerPrice']['valueString']
            item['title'] = one_html['information']['simpleSubject']
            item['href'] = one_html['information']['detailUrl']
            try:
                item['integer'] = one_html['tradeQuantity']['gmvValue']['integer']
            except:
                item['integer'] = ''
            # yield scrapy.Request(url=href, callback=self.parse_second, meta={'item': item})
            yield item

