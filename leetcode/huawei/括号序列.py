"""
给出一个仅包含字符'(',')','{','}','['和']',的字符串，判断给出的字符串是否是合法的括号序列
括号必须以正确的顺序关闭，"()"和"()[]{}"都是合法的括号序列，但"(]"和"([)]"不合法。
"""


class Solution:
    def isValid(self, s):
        after_list = [')', ']', '}']
        stack_list = []
        for item in s:
            if item not in after_list:
                stack_list.append(item)
            else:
                try:
                    before = stack_list.pop()
                except:
                    return False
                if before == '(' and item == ')':
                    continue
                if before == '[' and item == ']':
                    continue
                if before == '{' and item == '}':
                    continue
                else:
                    return False
        if stack_list:
            return False
        return True


s = Solution()
print(s.isValid('{()[}]}'))
