"""
python实现链式栈模型
   链式栈把链尾设计成栈底，因为头部比较好操作，尾部要遍历进去
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkListStack:
    def __init__(self):
        # 头节点为none的链表为空链表
        self.head = None

    def push(self, item):
        """在链表的头部添加一个节点"""
        node = Node(item)
        node.next = self.head
        self.head = node

    def pop(self):
        """删除链表头部节点，返回链表头部value"""
        if self.head == None:
            raise Exception('pop from a empty list stack')
        value = self.head.value
        self.head = self.head.next
        return value

if __name__ == '__main__':
    lls = LinkListStack()
    lls.push(100)
    lls.push(200)
    lls.push(300)
    lls.push(400)
    print(lls.pop())
    print(lls.pop())
    print(lls.pop())
    print(lls.pop())
    print(lls.pop())
    print(lls.pop())
