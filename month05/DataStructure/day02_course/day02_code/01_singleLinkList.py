"""python实现单链表"""


class Node:
    """节点类，生成节点的工厂"""

    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinklist:
    """单链表类：数学模型"""

    def __init__(self):
        """初始化一个空链表：头节点为None的链表为空链表"""
        # self.head 为头节点
        self.head = None

    def is_empty(self):
        """判断是否为空链表"""
        return self.head == None

    def travel(self):
        """遍历整个链表"""
        cur = self.head
        while cur:
            print(cur.value, end=',')
            cur = cur.next
        print()

    def append(self, *arg):  # 修改成使用*arg传参（元组）
        # In[1]:
        # def func01(*arg):
        #     ...: print(arg)
        #     ...:
        # In[2]: func01(1, 2, 3, 4, 5)
        # (1, 2, 3, 4, 5)
        # In[3]: func01(1)
        # (1,)
        """在链表尾部添加一个或节点"""
        if not arg:
            raise Exception('append 不能为空')
        for data in arg:
            node = Node(data)
            if self.is_empty():
                self.head = node
            else:
                cur = self.head
                while cur.next is not None:
                    cur = cur.next
                cur.next = node
                node.next = None

    def add(self, data):
        """在链表头部添加一个节点"""
        if not data:
            raise Exception('add 不能为空')
        node = Node(data)
        node.next = self.head
        self.head = node

    def length(self):
        """返回列表的长度"""
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count

    def search(self, data):
        """查看链表中是否存在某值，返回布尔值"""
        cur = self.head
        while cur:
            if cur.value == data:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, data):
        """删除链表中第一个值为data的节点"""
        # 方法一
        if not self.search(data):
            raise Exception(f'链表中没有值为{data}的节点')
        cur = self.head
        while True:
            if cur.next.value == data:
                cur.next = cur.next.next
                print('删除成功')
                break
            else:
                cur = cur.next
        # # 方法二
        # pre = None
        # cur = self.head
        # while cur:  # 遍历完了都没有就不删了
        #     if cur.value == data:
        #         pre.next = cur.next
        #         print('删除成功')
        #         break
        #     else:
        #         pre = cur
        #         cur = cur.next

    def reverse(self):
        pre = None
        cur = self.head
        while cur:
            next = cur.next  # 要预先存储一个next，防止进不去下一个
            cur.next = pre  # 反向
            pre = cur  # 前进一个
            cur = next  # 前进一个
        return pre.value


if __name__ == '__main__':
    linklist = SingleLinklist()
    linklist.append(1)
    linklist.append(2)
    linklist.append(3, 5, 6, 7)
    linklist.add(4)
    print(linklist.length())  # 4
    linklist.travel()  # 4,1,2,3,
    linklist.remove(2)
    linklist.travel()  # 4,1,3,
    print(linklist.search(2))  # False
    print(linklist.reverse())
