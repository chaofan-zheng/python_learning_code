"""
递归示例
"""


# 求n一直加到1的和
def s(n):
    if n == 1:
        return 1
    return n + s(n - 1)


print(s(998))


# n的阶乘
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(5))
