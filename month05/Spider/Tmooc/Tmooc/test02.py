import requests
import os
from Crypto.Cipher import AES


def m3u8(url):
    # base_url = url[:url.rfind('/') + 1]  # 如果需要拼接url,则启用 , +1 把 / 加上
    base_url = url # 如果需要拼接url,则启用 , +1 把 / 加上
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
    rs = requests.get(url, headers=headers).text
    list_content = rs.split('\n')
    player_list = []
    # 如果没有merge文件夹则新建merge文件夹，用于存放ts文件
    if not os.path.exists('merge'):
        os.system('mkdir merge')
    key = ''
    for index, line in enumerate(list_content):
        # 判断视频是否经过AES-128加密
        if "#EXT-X-KEY" in line:
            method_pos = line.find("METHOD")
            comma_pos = line.find(",")
            method = line[method_pos:comma_pos].split('=')[1]  # 获取加密方式
            print("Decode Method：", method)
            uri_pos = line.find("URI")
            quotation_mark_pos = line.rfind('"')
            key_path = line[uri_pos:quotation_mark_pos].split('"')[1]
            key_url = key_path
            res = requests.get(key_url)
            key = res.content  # 获取加密密钥
            print("key：", key)
        # 以下拼接方式可能会根据自己的需求进行改动
        if '#EXTINF' in line:
            # href = ''
            # 如果加密，直接提取每一级的.ts文件链接地址
            if 'http' in list_content[index + 1]:
                href = list_content[index + 1]
                player_list.append(href)
            # 如果没有加密，构造出url链接
            elif ('ad0.ts' not in list_content[index + 1]):
                href = base_url + list_content[index + 1]
                player_list.append(href)
    if (len(key)):
        print('此视频经过加密')
        print(player_list)  # 打印ts地址列表
        for i, j in enumerate(player_list):
            cryptor = AES.new(key, AES.MODE_CBC, key)
            res = requests.get(j, headers=headers)
            with open('merge/' + str(i + 1) + '.ts', 'wb') as file:
                file.write(cryptor.decrypt(res.content))  # 将解密后的视频写入文件
                print('正在写入第{}个文件'.format(i + 1))
    else:
        print('此视频未加密')
        print(player_list)  # 打印ts地址列表
        for i, j in enumerate(player_list):
            res = requests.get(j, headers=headers)
            with open('merge/' + str(i + 1) + '.ts', 'wb') as file:
                file.write(res.content)
                print('正在写入第{}个文件'.format(i + 1))
        print('下载完成')


# 当全写下载完之后合并文件并删除所有.ts文件
def merge_ts():
    path = os.getcwd() + '\merge'  # 获取视频存放路径
    # merge_cmd = 'copy /b ' + path + '\*.ts ' + path + '\\new.mp4'
    # del_cmd = 'del ' + path + '\*.ts'
    # os.system(merge_cmd)  # 执行合并命令
    # os.system(del_cmd)  # 执行删除命令
    # print('合并完成')


if __name__ == '__main__':
    url = 'https://c.it211.com.cn/aid20101106am/aid20101106am.m3u8?_time=1618724866630&sign=D5426FFA328C8E0DBDEB7E795AA99D21'
    # 下载视频
    m3u8(url)
    # 合并视频
    merge_ts()
