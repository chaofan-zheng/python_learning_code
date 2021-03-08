"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
只考虑最后一次的情况
"""


class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 2:
            return 2
        if number == 1:
            return 1
        return self.jumpFloor(number - 1) + self.jumpFloor(number - 2)


class Solution2:
    def jumpFloor(self, number):
        # write code here
        a, b = 0, 1
        for i in range(number + 1):
            a, b = b, a + b
        return a


s = Solution2()
print(s.jumpFloor(5))
