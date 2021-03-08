# 根据3的余数的大小排序
from functools import reduce

list01 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
list01.sort(key=lambda x: x % 3)
print(list01)


#
def multipliers():
    return [lambda x, i=i: i * x for i in range(4)]


m = multipliers()
for i in m:
    print(i(5))

# lambda的本质是一个匿名函数。就是业务逻辑很简单的函数。
print(list(map(lambda x: x * x, range(1, 21))))  # map 函数：根据一定的功能，把一个可迭代对象映射出来，返回值是一个可迭代对象
"""
map(func, *iterables) --> map object

Make an iterator that computes the function using arguments from
each of the iterables.  Stops when the shortest iterable is exhausted.
"""
print(list(filter(lambda x: x % 2 == 0, range(1, 21))))  # 返回function里条件为true的情况
"""
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
"""

print(reduce(lambda x, y: x + y, range(1, 101)))
""" Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the sequence in the calculation, and serves as a default when the
    sequence is empty."""
print(sum(list(range(1, 101))))  # 好像和累加没有什么区别...
