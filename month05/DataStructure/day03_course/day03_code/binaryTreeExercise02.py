"""一个青蛙一次可以跳1级台阶或2级台阶，一共有n级台阶，问青蛙跳到顶部有几种跳法？（递归）"""


# 思路：找规律
# t=1 1
# t = 2 2
# t = 3 3
# t = 4 5
# t = 5 8
# 发现是一个斐波那契数列

# 思路2 递归f(n)
# 考虑最后一跳
# 最后一跳 跳1级台阶，有f(n-1)种跳法
# 最后一跳 跳2级台阶，有f(n-2)种跳法
# 总的跳法种类f(n)=f(n-1)+f(n-2)
def f(n):
    # 递归的出口
    # 因为有两个递归，所以要写两个递归的出口
    if n == 1:
        return 1
    if n == 2:
        return 2
    return f(n - 1) + f(n - 2)


print(f(5))
