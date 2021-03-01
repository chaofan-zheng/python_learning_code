"""
python 快速排序
"""


def quick_sort():
    pass


def sort(li):
    """进行一轮比较，给一个基准值找到一个正确位置的下标索引"""
    mid = li[0]
    l_cur = 1
    r_cur = len(li) - 1

    while True:
        # 左游标遇到比基准值大的停
        while li[l_cur] <= mid and r_cur >= l_cur:
            l_cur += 1
        while li[r_cur] > mid and r_cur >= l_cur:
            r_cur -= 1
        if r_cur < l_cur:
            li[r_cur], li[0] = li[0], li[r_cur]
            return li
        else:
            li[r_cur], li[l_cur] = li[l_cur], li[r_cur]


print(sort([6, 5, 3, 1, 8, 7, 2, 4]))
