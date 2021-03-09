"""
有一个数组a[N]顺序存放0~N-1，要求每隔两个数删掉一个数，到末尾时循环至开头继续进行，求最后一个被删掉的数的原始下标位置。以8个数(N=7)为例:｛0，1，2，3，4，5，6，7｝，0->1->2(删除)->3->4->5(删除)->6->7->0(删除),如此循环直到最后一个数被删除。
"""


def recure(arr):
    if len(arr) == 1:
        return arr[0]
    list01 = arr
    index = 2
    for i in range(2, len(arr), 3):
        list01[i]=-1
        index += 3
    list_next = arr[index + 1:] + list(str(list01[:index]).replace('-1',''))
    recure(list_next)


while True:
    n = int(input())
    if n > 1000:
        n = 999
    list01 = list(range(n))
    num = recure(list01)
    print(num)

# 答案
while True:
    try:
        n = int(input())
    except:
        exit()
    a = range(n)
    i = 0
    while len(a) > 1:
        i = (i+2) % len(a)
        if i != len(a) - 1:
            a = a[:i] + a[i+1:]
        else:
            a = a[:i]
            i = 0
    print (a[0])
