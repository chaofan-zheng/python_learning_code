"""字符串，小写字母，删除操作，有两个相邻相同 删掉"""
'abbac'


def solution(str):
    if not str:
        return ""
    li = list(str)
    stack = []
    for item in li:
        if not stack:
            stack.append(item)
            continue
        if item == stack[-1]:
            stack.pop()
        else:
            stack.append(item)
    if not stack:
        return ""
    return ''.join(stack)


if __name__ == '__main__':
    str01 = "aaabaaaa"
    res = solution(str01)
    print(res)
