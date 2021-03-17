class Solution:
    def maxProfit(self , prices ):
        if len(prices) == 0 or len(prices) == 1:
            return 0
        # write code here
        max_num = max(prices)
        max_index = prices.index(max_num)
        if len(prices[:max_index]) == 0:
            return 0
        min_num = min(prices[:max_index])
        return max_num - min_num

list01 = [1,2]
s = Solution()
print(s.maxProfit(list01))