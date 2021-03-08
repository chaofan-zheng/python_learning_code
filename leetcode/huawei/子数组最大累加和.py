"""
给定一个数组arr，返回子数组的最大累加和
例如，arr = [1, -2, 3, 5, -2, 6, -1]，所有子数组中，[3, 5, -2, 6]可以累加出最大的和12，所以返回12.
题目保证没有全为负数的数据
[要求]
时间复杂度为O(n)，空间复杂度为O(1)
"""
# 思路：从索引为1开始往后推，如果当前值和当前值前一个值的和大于当前值，说明有用，当前值等于和。
# 如果小于，说明前面相加起来小于零，没用，就舍弃了，当前值还是等于当前值。这样就能找到最大子组左索引的开始位置。
# 然后用一个max记录最大值，不断更新max，就可以过滤掉右边的无效组

class Solution:
    def maxsumofSubarray(self, arr):
        # write code here
        max = 0
        if len(arr)==1:
            return arr[0]
        for i in range(1, len(arr)):
            if arr[i] + arr[i - 1] > arr[i]:
                arr[i] = arr[i] + arr[i - 1]
            if arr[i] > max:
                max = arr[i]
        return max


s = Solution()
print(s.maxsumofSubarray([1, -2, 3, 5, -2, 6, -1]))
