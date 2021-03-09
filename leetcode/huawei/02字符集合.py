"""
每组数据输入一个字符串，字符串最大长度为100，且只包含字母，不可能为空串，区分大小写。
每组数据一行，按字符串原有的字符顺序，输出字符集合，即重复出现并靠后的字母不输出。
"""

while True:
    try:
        res=[]
        str = input()
        for item in str:
            if item in res:
                continue
            else:
                res.append(item)
        res = ''.join(res)
        print(res)
    except:
        break