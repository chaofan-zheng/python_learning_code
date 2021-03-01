def quick_sort(li, first, last):
    # position 基准值正确位置的下表索引，既分割li左右两部分的值
    if first > last:
        return
        # 递归
    position = sort(li, first, last)
    # 左边
    quick_sort(li, first, position - 1)
    quick_sort(li, position + 1, last)


def sort(li, first, last):
    """
    :param li: 无序的数组
    :param first: 基准值所在的位置的下表索引
    :param last: 右游标的索引值
    :return: 基准值正确位置的下表索引
    """
    lcur = first + 1
    rcur = last
    # mid = li[first]#不能写mid
    while True:
        # 左游标右移
        # 如果比基准值大 暂停
        while lcur <= rcur and li[lcur] <= li[first]:
            lcur += 1
        # 右游标左移
        while lcur <= rcur and li[rcur] >= li[first]:
            rcur -= 1
        if lcur < rcur:
            # 左右游标互换位置
            li[lcur], li[rcur] = li[rcur], li[lcur]
        else:
            # 右游标小于等于左游标
            li[rcur], li[first] = li[first], li[rcur]
            # 返回了基准值正确位置的下标索引
            return rcur


li = [6, 5, 3, 1, 8, 7, 2, 4]
print(quick_sort(li, 0, len(li) - 1))
print(li)
