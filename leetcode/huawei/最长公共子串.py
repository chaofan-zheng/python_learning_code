"""
给定两个字符串str1和str2,输出两个字符串的最长公共子串
题目保证str1和str2的最长公共子串存在且唯一。
"""


class Solution:
    def LCS(self, str1, str2):
        # write code here
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        res = ""
        maxLen = 0 # 最长字符串的起点位置
        for i in range(len(str1)):
            if str1[i - maxLen:i + 1] in str2:
                res = str1[i - maxLen:i + 1]
                maxLen += 1
        return res
