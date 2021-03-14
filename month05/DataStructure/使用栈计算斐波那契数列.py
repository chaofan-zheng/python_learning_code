def fib(n):
    list01 = [1, 1]
    for i in range(n-2):
        pre = list01.pop()
        cur = list01.pop()
        list01.append(cur)
        list01.append(pre + cur)
    return list01[-1]


print(fib(4))