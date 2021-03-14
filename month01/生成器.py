def g():
    for i in range(3):
        yield i


a = g()
print(next(a))
b = g()
print(next(b))


class MyRangeIterator:
    def __init__(self, end):
        self.num = -1
        self.end = end

    def __next__(self):
        self.num += 1
        if self.num < self.end:
            return self.num
        else:
            raise StopIteration


iterator = MyRangeIterator(3)
print(next(iterator))
print(next(iterator))
print(next(iterator))


# print(next(iterator))


def h():
    for x in range(3):
        print('Wen Chuan')
        yield x
        print('Fighting!')


c = h()
next(c)  # Wen Chuan
next(c)  # Fighting WenChuan


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


a = fib(10)
for i in a:
    print(i)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


a = fib(10)
print(fib(10))

def gen():
    for i in range(5):
        a = yield i
        print(a)
g = gen()
print(g.__next__())
print(g.__next__())
print(g.send(5))
print(g.__next__())
print(g.__next__())


