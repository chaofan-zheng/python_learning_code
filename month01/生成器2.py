class MyNumGenerator:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > 5:
            raise StopIteration
        self.num += 1
        return self.num


g = MyNumGenerator(2)
for i in g:
    print(i)
for i in g:
    print(i)
