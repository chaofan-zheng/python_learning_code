# 考虑最后一步
def merge_sort(li):
    if len(li) <= 1:
        return li
    mid = len(li) // 2
    left_li = li[:mid]
    right_li = li[mid:]
    left = merge_sort(left_li)
    right = merge_sort(right_li)
    return merge(left, right)


def merge(left_li, right_li):
    result = []
    while len(left_li) > 0 and len(right_li) > 0:
        if left_li[0] < right_li[0]:
            result.append(left_li.pop(0))
        else:
            result.append(right_li.pop(0))
    # 循环结束时，一定有一个列表为空
    result += left_li
    result += right_li
    return result


print(merge([5, 6], [1, 3]))
print(merge_sort([6, 5, 3, 1,1,2,2,999, 8, 7, 2, 4]))
