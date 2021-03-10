"""
找出指定瑕疵度的最长元音字符串，输出其长度
"""
yuanyin = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    try:
        flaw = int(input())
        str_list = list(input())
        i, j = 0, 0
        list_length = len(str_list)
        max_len=0
        fcount = 0
        while i < len(str_list):
            if j >= len(str_list):
                fcount = 0
                i += 1
                j = i
                continue
            if str_list[i] not in yuanyin:
                i += 1
                j += 1
                continue
            else:
                if str_list[j] not in yuanyin:
                    j += 1
                    fcount += 1
                    continue
                else:
                    if fcount == flaw:
                        if max_len <len(str_list[i:j + 1]):
                            max_len = len(str_list[i:j + 1])
                    j += 1
        print(max_len)
    except Exception as e:
        break
