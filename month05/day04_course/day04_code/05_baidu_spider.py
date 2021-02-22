"""
百度翻译破解案例 - JS 逆向
"""
import execjs
import requests
import re


class BaiduSpider:
    def __init__(self):
        self.headers = {
            '''Accept''': '''*/*''',
            '''Accept-Encoding''': '''gzip, deflate, br''',
            '''Accept-Language''': '''en,zh;q=0.9,zh-CN;q=0.8''',
            '''Connection''': '''keep-alive''',
            '''Content-Length''': '''136''',
            '''Content-Type''': '''application/x-www-form-urlencoded; charset=UTF-8''',
            '''Cookie''': '''BAIDUID=B68D70A628CA22B0E6BD6BD6B28983BD:FG=1; BDUSS=NYMG84TH5RWElTRnFERGRqWWJCY0hKQWZpTmRlUU5ZR3lYN2VzdUZJNHZVT1plRVFBQUFBJCQAAAAAAAAAAAEAAACDqCSm1N3O3sP7uf4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC~Dvl4vw75eb3; BDUSS_BFESS=NYMG84TH5RWElTRnFERGRqWWJCY0hKQWZpTmRlUU5ZR3lYN2VzdUZJNHZVT1plRVFBQUFBJCQAAAAAAAAAAAEAAACDqCSm1N3O3sP7uf4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC~Dvl4vw75eb3; BIDUPSID=B68D70A628CA22B0E6BD6BD6B28983BD; PSTM=1608864265; __yjs_duid=1_bfd078b8cc79a02d617c8cb0122cc3401611574980862; H_PS_PSSID=33423_33581_33344_31254_33570_33585_26350_22158; delPer=0; PSINO=3; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDRCVFR[tox4WRQ4-Km]=mk3SLVN4HKm; BDRCVFR[CLK3Lyfkr9D]=mk3SLVN4HKm; BAIDU_WISE_UID=wapp_1613918368967_350; BA_HECTOR=al04248k00a18k2l4q1g36j0v0q; BCLID=10392685419358595798; BDSFRCVID=NcIOJexroG3VnU3e-P_xuRpBw_weG7bTDYLEOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJ4joC8KtDK3qn5zK-QJbDCs5fQEaC62aKDs0bR2BhcqJ-ovQTboW4PwbH5lbqQtLjRGL-bCBUONHxbeWfvph5KU-GQ9y-cA3HOp2J4bah5nhMJmb4JWLfIz-lQayMry523ion3vQpP-OpQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0DjPVKgTa54cbb4o2WbCQBJOz8pcN2b5oQTtZhR_eKCrTX5btbtJPbM7beq06-lOUWfAkXpJvQnJjt2JxaqRCWJ5TMl5jDh3MKToDb-otexQ7bIny0hvctn3cShPCyUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQh-p52f60qtbPq3f; BCLID_BFESS=10392685419358595798; BDSFRCVID_BFESS=NcIOJexroG3VnU3e-P_xuRpBw_weG7bTDYLEOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJ4joC8KtDK3qn5zK-QJbDCs5fQEaC62aKDs0bR2BhcqJ-ovQTboW4PwbH5lbqQtLjRGL-bCBUONHxbeWfvph5KU-GQ9y-cA3HOp2J4bah5nhMJmb4JWLfIz-lQayMry523ion3vQpP-OpQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0DjPVKgTa54cbb4o2WbCQBJOz8pcN2b5oQTtZhR_eKCrTX5btbtJPbM7beq06-lOUWfAkXpJvQnJjt2JxaqRCWJ5TMl5jDh3MKToDb-otexQ7bIny0hvctn3cShPCyUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQh-p52f60qtbPq3f; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1613974565,1613976310; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1613976310; __yjsv5_shitong=1.0_7_180d7bbb674dd0dd7f772374cb6aab6f4b1b_300_1613976310137_223.104.244.202_ec01fade; ab_sr=1.0.0_YWI0NDVmZGFhNDdjYTYwMDNiODIyYjI5NTEwMDc0OGYzYmI4MGU2N2VkMzU0YmRlYWI0ODFjOGFkZWU5OTdlYzU0NTg2YjhjN2Y3OTcwNWEyNGRlMTZiNjAxMDZhMDEw''',
            '''Host''': '''fanyi.baidu.com''',
            '''Origin''': '''https://fanyi.baidu.com''',
            '''Referer''': '''https://fanyi.baidu.com/?aldtype=16047''',
            '''sec-ch-ua''': '''"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"''',
            '''sec-ch-ua-mobile''': '''?0''',
            '''Sec-Fetch-Dest''': '''empty''',
            '''Sec-Fetch-Mode''': '''cors''',
            '''Sec-Fetch-Site''': '''same-origin''',
            '''User-Agent''': '''Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36''',
            '''X-Requested-With''': '''XMLHttpRequest''',
        }
        self.url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

        self.get_headers={
            '''Accept-Encoding''': '''gzip, deflate, br''',
            '''Accept-Language''': '''en,zh;q=0.9,zh-CN;q=0.8''',
            '''Connection''': '''keep-alive''',
            '''Cookie''': '''BAIDUID=B68D70A628CA22B0E6BD6BD6B28983BD:FG=1; BDUSS=NYMG84TH5RWElTRnFERGRqWWJCY0hKQWZpTmRlUU5ZR3lYN2VzdUZJNHZVT1plRVFBQUFBJCQAAAAAAAAAAAEAAACDqCSm1N3O3sP7uf4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC~Dvl4vw75eb3; BDUSS_BFESS=NYMG84TH5RWElTRnFERGRqWWJCY0hKQWZpTmRlUU5ZR3lYN2VzdUZJNHZVT1plRVFBQUFBJCQAAAAAAAAAAAEAAACDqCSm1N3O3sP7uf4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC~Dvl4vw75eb3; BIDUPSID=B68D70A628CA22B0E6BD6BD6B28983BD; PSTM=1608864265; __yjs_duid=1_bfd078b8cc79a02d617c8cb0122cc3401611574980862; H_PS_PSSID=33423_33581_33344_31254_33570_33585_26350_22158; delPer=0; PSINO=3; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDRCVFR[tox4WRQ4-Km]=mk3SLVN4HKm; BDRCVFR[CLK3Lyfkr9D]=mk3SLVN4HKm; BAIDU_WISE_UID=wapp_1613918368967_350; BCLID=10392685419358595798; BDSFRCVID=NcIOJexroG3VnU3e-P_xuRpBw_weG7bTDYLEOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJ4joC8KtDK3qn5zK-QJbDCs5fQEaC62aKDs0bR2BhcqJ-ovQTboW4PwbH5lbqQtLjRGL-bCBUONHxbeWfvph5KU-GQ9y-cA3HOp2J4bah5nhMJmb4JWLfIz-lQayMry523ion3vQpP-OpQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0DjPVKgTa54cbb4o2WbCQBJOz8pcN2b5oQTtZhR_eKCrTX5btbtJPbM7beq06-lOUWfAkXpJvQnJjt2JxaqRCWJ5TMl5jDh3MKToDb-otexQ7bIny0hvctn3cShPCyUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQh-p52f60qtbPq3f; BCLID_BFESS=10392685419358595798; BDSFRCVID_BFESS=NcIOJexroG3VnU3e-P_xuRpBw_weG7bTDYLEOwXPsp3LGJLVJeC6EG0Pts1-dEu-EHtdogKK0gOTH6KF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tJ4joC8KtDK3qn5zK-QJbDCs5fQEaC62aKDs0bR2BhcqJ-ovQTboW4PwbH5lbqQtLjRGL-bCBUONHxbeWfvph5KU-GQ9y-cA3HOp2J4bah5nhMJmb4JWLfIz-lQayMry523ion3vQpP-OpQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xXj_0DjPVKgTa54cbb4o2WbCQBJOz8pcN2b5oQTtZhR_eKCrTX5btbtJPbM7beq06-lOUWfAkXpJvQnJjt2JxaqRCWJ5TMl5jDh3MKToDb-otexQ7bIny0hvctn3cShPCyUjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQh-p52f60qtbPq3f; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1613974565,1613976310; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1613986878; __yjsv5_shitong=1.0_7_180d7bbb674dd0dd7f772374cb6aab6f4b1b_300_1613986877652_223.104.244.202_dc999445; ab_sr=1.0.0_ZGI1ZGY5MmU2OWZlY2NmYTBkZDZiYTVhNTBhN2QwZThkYzRlZmMyYTg4MjY2NGRjYmFjNTMwYWNjOWZmYzI5N2NiY2NkYjllMjA3NTI2M2ZkNWE0MjdkZWE0M2Y0MTQ5''',
            '''Host''': '''fanyi.baidu.com''',
            '''sec-ch-ua''': '''"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"''',
            '''sec-ch-ua-mobile''': '''?0''',
            '''Sec-Fetch-Dest''': '''document''',
            '''Sec-Fetch-Mode''': '''navigate''',
            '''Sec-Fetch-Site''': '''none''',
            '''Sec-Fetch-User''': '''?1''',
            '''Upgrade-Insecure-Requests''': '''1''',
            '''Accept''': '''text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9''',
        }
        self.get_url='https://fanyi.baidu.com/'

    def get_translate(self, word, gtk, token):
        with open('translate.js', 'r') as f:
            jscode = f.read()
        jsobj = execjs.compile(jscode)  # 根据jscode创建编译对象
        sign = jsobj.eval(f'e("{word}","{gtk}")')  # eval是把一个字符串当作表达式来执行
        data = {
            "from": "en",
            "to": "zh",
            "query": f"{word}",
            "transtype": "realtime",
            "simple_means_flag": "3",
            "sign": str(sign),
            "token": f"{token}",
            "domain": "common",
        }
        json_obj = requests.post(url=self.url, data=data, headers=self.headers).json()
        # print(json_obj)
        res = json_obj['trans_result']['data'][0]['dst']
        print(res)

    # 为了写的健壮一些可以把gtk和token从响应内容中获取gtk和token，然后传参传进去
    def get_gtk_token(self):
        html = requests.get(url=self.get_url, headers=self.get_headers).text
        gtk = re.findall("window.gtk = '(.*?)'", html, re.S)[0]
        token = re.findall("token: '(.*?)'", html, re.S)[0]
        return gtk, token

    def run(self):
        word = input("请输入要翻译的单词")
        gtk, token = self.get_gtk_token()
        self.get_translate(word, gtk, token)


if __name__ == '__main__':
    spider = BaiduSpider()
    spider.run()
