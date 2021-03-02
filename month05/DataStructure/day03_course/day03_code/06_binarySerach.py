"""
python实现二分查找
"""


# 1 2 3 4 5 6 7
def binary_search(li, item):
    first = 0
    last = len(li) - 1
    while first < last:
        mid = (last + first) // 2
        if li[mid] > item:
            last = mid - 1
        elif li[mid] < item:
            first = mid + 1
        else:
            return True
    return False


print(binary_search([1, 2, 3, 4, 5], 6))
