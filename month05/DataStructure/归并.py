def merge_sort(original_list):
    if len(original_list) == 1:
        return original_list  # 递归出口
    mid = len(original_list) // 2
    left_list = original_list[:mid]
    right_list = original_list[mid:]
    left = merge_sort(left_list)
    right = merge_sort(right_list)
    return merge(left, right)


def merge(left, right):
    res = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            res.append(right.pop(0))
        else:
            res.append(left.pop(0))
    res += left
    res += right
    return res


if __name__ == '__main__':
    list01 = [1, 2, 45, 65456, 423, 4, 14, 3, 2, 4, 3]
    res = merge_sort(list01)
    print(res)
