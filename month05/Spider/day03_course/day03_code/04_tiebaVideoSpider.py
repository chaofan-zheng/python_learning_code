"""
百度贴吧视频抓取
1、向帖子连接发请求，提取视频链接
2、向视频链接发请求，将响应内容以wb的方式保存到本地
"""
import requests
from lxml import etree
from fake_useragent import UserAgent
import re

url = 'https://tieba.baidu.com/f?kw=电气鼠&ie=utf-8&tab=main'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'Cookie': 'BAIDUID=B68D70A628CA22B0E6BD6BD6B28983BD:FG=1; BDUSS=NYMG84TH5RWElTRnFERGRqWWJCY0hKQWZpTmRlUU5ZR3lYN2VzdUZJNHZVT1plRVFBQUFBJCQAAAAAAAAAAAEAAACDqCSm1N3O3sP7uf4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC~Dvl4vw75eb3; BDUSS_BFESS=NYMG84TH5RWElTRnFERGRqWWJCY0hKQWZpTmRlUU5ZR3lYN2VzdUZJNHZVT1plRVFBQUFBJCQAAAAAAAAAAAEAAACDqCSm1N3O3sP7uf4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC~Dvl4vw75eb3; BIDUPSID=B68D70A628CA22B0E6BD6BD6B28983BD; PSTM=1608864265; __yjs_duid=1_bfd078b8cc79a02d617c8cb0122cc3401611574980862; H_PS_PSSID=33423_33581_33344_31254_33570_33585_26350_22158; BDSFRCVID=gltOJexroG3oZkRe2FrUuRpBwtVLSAbTDYLEl6Kb1O_iIF_VNl3oEG0PtfgxAJFbqb_MogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJ4joC8KtDK3qn5zK-QJbDCs5fQEaC62aKDs0bR2BhcqJ-ovQTboW4PwbH5lbqQtLjRGL-bCBUONHxbeWfvph5KU-GQ9y-cA3HOp2J4bah5nhMJmb4JWLfIz-lQayMry523ion3vQpP-OpQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0-nDSHH8DJTLe3q; delPer=0; BDSFRCVID_BFESS=gltOJexroG3oZkRe2FrUuRpBwtVLSAbTDYLEl6Kb1O_iIF_VNl3oEG0PtfgxAJFbqb_MogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJ4joC8KtDK3qn5zK-QJbDCs5fQEaC62aKDs0bR2BhcqJ-ovQTboW4PwbH5lbqQtLjRGL-bCBUONHxbeWfvph5KU-GQ9y-cA3HOp2J4bah5nhMJmb4JWLfIz-lQayMry523ion3vQpP-OpQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0-nDSHH8DJTLe3q; PSINO=3; STOKEN=7a13d7ab0c6aa50b65d1a5640c58ba0f8bceed63fd597f692ccdca73d206b22f; st_key_id=17; 2787420291_FRSVideoUploadTip=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDRCVFR[tox4WRQ4-Km]=mk3SLVN4HKm; BDRCVFR[CLK3Lyfkr9D]=mk3SLVN4HKm; BA_HECTOR=0h05018080ak2g8gkq1g34quj0q; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1613481447,1613917143; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1613917266; ab_sr=1.0.0_NGE0OGI3ZjlmOGYzZTkxMDc1NTliY2VlMTgxYmJhZWIzMjI3NTBkZThjMTBjOTc5ODMxMDE1ZjJiYTRjMWMyNmYyOGEzNmM0NzcwZWU5NTY4ZjQxMzA2ZGYzMmY0MWJmOGJhMTg1OTMxMzczOWI1YWVjNjdjNGM0NWVkYTcyNzg=; st_data=c8cc7f202dfdb2870bb4d2ac3e4437d4741136169d1a4b65c6432c49ab2ecfcdd5751f4bc7a8d48b3549f89e14773029b9345f0ef658a69425a52c34d0b32f68e3cfd32c5564557aebe5ec459c7aee16a23eab1a0e27e382ee27afd35c8b5d7216de536a5eb1ac73899b7e056908f4fe7195a811fde9a2db9bb6bb52048f895e8a0990b160b99a097566a30b25c4a969; st_sign=37c65a98',
    'referer': 'https://tieba.baidu.com/f?kw=%E7%94%B5%E6%B0%94%E9%BC%A0&ie=utf-8&tab=album'}
html = requests.get(url=url, headers=headers).text
# eobj = etree.HTML(html)
# src_list = eobj.xpath('//div[@class="threadlist_video"]//a[@rel="noreferrer"]/@data-video')
src_list = re.findall('data-video="(.*?)"', html, re.S)
if src_list:
    count = 1
    for item in src_list:
        video_url = item
        video = requests.get(video_url, headers=headers).content
        with open(f'电气鼠{count}.mp4', 'wb') as f:
            f.write(video)
        count += 1
else:
    print('提取视频连接失败')

# # 1.提取帖子中视频的链接
# url = 'https://tieba.baidu.com/p/7216913650'
# headers = {'User-Agent' : UserAgent().random}
# html = requests.get(url=url, headers=headers).text
# print(html)
# eobj = etree.HTML(html)
# src_list = eobj.xpath('//embed/@data-video')
# if src_list:
#     video_url = src_list[0]
#     # 向视频链接发请求,并将其保存到本地即可
#     video_html = requests.get(url=video_url, headers=headers).content
#     with open('赵丽颖.mp4', 'wb') as f:
#         f.write(video_html)
# else:
#     print('提取视频链接失败')
