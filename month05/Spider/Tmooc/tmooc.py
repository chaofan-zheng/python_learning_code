import requests


def download(url, filepath, filename):
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": """gzip, deflate, br""",
        "Accept-Language": """en,zh;q=0.9,zh-CN;q=0.8""",
        "Connection": "keep-alive",
        "Host": "c.it211.com.cn",
        "Origin": "http://tts.tmooc.cn",
        "Referer": "http://tts.tmooc.cn/",
        "sec-ch-ua": """"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99" """,
        "sec-ch-ua-mobile": "?0",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": """Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"""
    }

    html = requests.get(url, headers=headers).content

    path = filepath + filename

    with open(path, 'wb') as output:
        output.write(html)
        #
        # while True:
        #
        #     buffer = html.read(1024 * 256)
        #
        #     if not buffer:
        #         break

            # received += len(buffer)



    print('下载文件成功' + path)


if __name__ == '__main__':
    url = 'https://c.it211.com.cn/aid20101106am/aid20101106am.m3u8?_time=1618724866630&sign=D5426FFA328C8E0DBDEB7E795AA99D21'
    file_path = '/Users/aiden_zcf/PycharmProjects/Tmooc/python_leanring_code/month05/Spider/Tmooc/'
    file_name = 'test.mp4'
    download(url, file_path, file_name)
