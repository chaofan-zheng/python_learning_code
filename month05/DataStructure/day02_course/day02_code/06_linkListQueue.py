"""
python实现链式队列
   队头负责入队，队尾负责出队，对于链式队列来说，哪项功能多的就放在队头。
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkListQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, item):
        """队头入队"""
        node = Node(item)
        node.next = self.head
        self.head = node

    def dequeue(self):
        """队尾出队"""
        if not self.head:
            raise Exception('dequeue from a empty link list queue')
        pre = None
        cur = self.head
        while cur.next:
            pre = cur
            cur = cur.next
        if pre:  # 考虑只有最后一个元素的特殊情况，pre本身就是none
            pre.next = None
        else:
            # 如果pre为空，说明链表只有一个节点，删除后成为空链表
            self.head = None
        return cur.value


if __name__ == '__main__':
    llq = LinkListQueue()
    llq.enqueue(100)
    llq.enqueue(200)
    llq.enqueue(300)
    print(llq.dequeue())
    print(llq.dequeue())
    print(llq.dequeue())
    print(llq.dequeue())
    print(llq.dequeue())
