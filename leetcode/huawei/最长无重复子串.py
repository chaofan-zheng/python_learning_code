"""
给定一个数组arr，返回arr的最长无的重复子串的长度(无重复指的是所有数字都不相同)。
"""

# 使用双指针，如果新的元素 与起止指针范围内的元素重复，就暂存当前的无重复序列长度， 并将起始指针移动到重复元素后
# 重复元素要在列表里面
# 双指针：
class Solution:
    def maxLength(self, arr):
        pre = 0
        cur = 1
        max_len = 0
        while pre <= len(arr)-1 and cur<=len(arr)-1:
            if arr[cur] in arr[pre:cur]:
                if max_len < len(arr[pre:cur]):
                    max_len = len(arr[pre:cur])
                index = arr[pre:cur].index(arr[cur])
                pre += index+1
            cur += 1
        if max_len < len(arr[pre:cur]):
            max_len = len(arr[pre:cur])
        return max_len

arr = [3,7,8,7,6,6,5,3,2]
s = Solution()
print(s.maxLength(arr))

class Solution:
    def maxLength(self, arr):
        longest_length,i,j = 0, 0, 0
        arr_length = len(arr)
        while j < arr_length:
            try:
                index = arr[i:j].index(arr[j])
                longest_length = max(longest_length, j-i)
                i = index+1
            except ValueError:
                pass
            j += 1

        return max(longest_length, j-i)