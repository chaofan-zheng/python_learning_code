"""
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def merge_linklists(self, head1, head2):
        # 创建游标
        cur1 = head1
        cur2 = head2
        # 确定新列表表头
        if cur1.value >= cur2.value:
            newhead = cur2
            cur2 = cur2.next
        else:
            newhead = cur1
            cur1 = cur1.next
        # 创建新列表游标
        newcur = newhead
        # 进行比较，新链表的下一个节点是两个游标中值比较小的那一个
        while cur1 and cur2:
            if cur1.value <= cur2.value:
                newcur.next = cur1
                newcur = newcur.next
                cur1 = cur1.next
            else:
                newcur.next = cur2
                newcur = newcur.next
                cur2 = cur2.next
        # 循环结束意味着一定有一个列表为空了
        if cur1:
            newcur.next = cur1
        else:
            newcur.next = cur2
        return newhead


if __name__ == '__main__':
    node1 = Node(100)
    node1.next = Node(200)
    node1.next.next = Node(300)
    node1.next.next.next = Node(400)

    node2 = Node(1)
    node2.next = Node(200)
    node2.next.next = Node(600)
    node2.next.next.next = Node(800)

    s = Solution()
    newcur = s.merge_linklists(node1, node2)
    while newcur:
        print(newcur.value)
        newcur = newcur.next

