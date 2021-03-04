"""给定一个数组，请你编写一个函数，返回该数组排序后的形式。"""


class Solution:
    def MySort(self, arr):
        for r in range(len(arr) - 1):
            min = arr[r]
            for c in range(r + 1, len(arr)):
                if arr[c] < min:
                    min = arr[c]
                    arr[c], arr[r] = arr[r], arr[c]


s = Solution()
arr = [4, 5, 2,2, 3, 1]
s.MySort(arr)
print(arr)
