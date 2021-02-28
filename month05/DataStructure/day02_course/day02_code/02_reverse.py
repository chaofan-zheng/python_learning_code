"""
输入一个链表，反转链表后，输出新链表的表头
输入一个链表的意思就是输入一个表头
"""


class Node:
    """节点类"""

    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def reverse(self, head_node):
        pre = None
        cur = head_node
        while cur:
            next = cur.next  # 要预先存储一个next，防止进不去下一个
            cur.next = pre  # 反向
            pre = cur  # 前进一个
            cur = next  # 前进一个
        return pre


if __name__ == '__main__':
    s = Solution()
    # 手动创建链表,做一个简单的测试
    head = Node(100)
    head.next = Node(200)
    head.next.next = Node(300)
    node = s.reverse(head)
    print(node.value)
