"""
给定一个矩形网络，机器人每次只可以向右移动或者向下移动，问从左上角移动到右下角一共有多少种移动方法？
"""
n = 7  # 列
m = 8  # 行
results = [[1] * n for i in range(m)]
print(results)


def solution(r, c):
    results = [[1] * c for i in range(r)]
    for i in range(1, r):
        for j in range(1, c):
            results[i][j] = results[i - 1][j] + results[i][j - 1]
    return results[r - 1][c - 1]


print(solution(3, 4))

"""递归问法：有哪些移动路径？"""


def recur_solution(r, c):
    if r == 1:
        return ['x' * c]
    elif c == 1:
        return ['y' * r]
    elif r == 1 and r == 1:
        return ''
    else:
        res = [item + 'x' for item in recur_solution(r, c - 1)]
        res += [item + 'y' for item in recur_solution(r - 1, c)]
        return res


print(set(recur_solution(3, 4)))
