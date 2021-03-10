"""

1、数字涂色，涂相同色的数字都可以被同色的最小数整除，问最少需要多少种颜色？
2、输入一个K，从1到100报数，报到K后移除K，然后下一个从1开始继续报数，直到剩下的人数比K小，问剩下的人原来的编号是多少？
二星题：
3、服务器广播问题，输入一个二维数组，1和0组成，array[i][j]==1表示i和j直接相连，不等于1是间接链接，直接和间接连接的服务器都可以互通广播，
比如：A和B直接连接，B和C直接连接，则A和C间接连接。问初始需要给几台服务器，才能使所有服务器收到广播？
"""

# T1
# nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # 考虑空和1
# bases = [2]
# for num in nums:
#     con_sign = 0
#     for base in bases:
#         if num % base == 0:
#             con_sign = 1
#     if con_sign == 1:
#         continue
#     else:
#         bases.append(num)
# print(len(bases))

# T2
# k = int(input())
# list01 = list(range(1, 101))
# res_list = list01
# i = 0
# while len(res_list) >= k:
#     i = (i + k-1) % len(res_list)
#     if i != len(res_list) - 1:
#         res_list = res_list[:i] + res_list[i + 1:]
#     else:  # 防止越界的情况
#         res_list = res_list[:i]
#         i = 0
# print(res_list)

# T3

map = [
    [1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
]
res_map = {}
count = len(map)
for i in range(len(map)):
    res_map[i] = set()
    for j in range(len(map)):
        if map[i][j] == 1:
            res_map[i].add(j)

print(res_map)
count = 0
pool = set()
for key1 in res_map:
    if pool.intersection(res_map[key1]) == set():
        pool = pool.union(res_map[key1])
        count += 1
    else:
        pool.union(res_map[key1])
print(count)



# 图片排序
while True:
    try:
        print("".join(sorted(input())))
    except:break
