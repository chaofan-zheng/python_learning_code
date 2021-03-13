class MyRangeIterator:
    def __init__(self, begin, end):
        self.__end = end
        self.__begin = begin
        self.num = self.__begin - 1

    def __next__(self):
        self.num += 1
        if self.num >= self.__end:
            raise StopIteration
        return self.num


class MyRange:
    def __init__(self, begin, end):
        self.end = end
        self.begin = begin

    def __iter__(self):
        return MyRangeIterator(self.begin, self.end)


# for i in MyRange(0, 3):
#     print(i)
iterator = MyRange(0,3).__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except:
        break
