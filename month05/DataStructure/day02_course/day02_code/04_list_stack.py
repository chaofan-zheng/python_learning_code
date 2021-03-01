"""
python实现顺序栈
    1。目标：实现栈（后进先出）
    2。设计
"""


class ListStack:
    def __init__(self):
        """初始化一个空栈"""
        self.elems = []

    def push(self, item):
        """入栈操作"""
        self.elems.append(item)

    def destack(self):
        """出栈操作"""
        if not self.elems:
            raise Exception('destack from a empty stack!')
        return self.elems.pop()


if __name__ == '__main__':
    ls = ListStack()
    ls.push(100)
    ls.push(200)
    ls.push(300)
    print(ls.destack())
    print(ls.destack())
    print(ls.destack())
    print(ls.destack())
    print(ls.destack())
