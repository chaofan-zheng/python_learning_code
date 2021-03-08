"""
将两个有序的链表合并为一个新链表，要求新的链表是通过拼接两个链表的节点来生成的，且合并后新链表依然有序。
"""


class Solution:
    def mergeTwoLists(self, l1, l2):
        cur1 = l1
        cur2 = l2
        if not l1:
            return l2
        if not l2:
            return l1
        if cur2.val > cur1.val:
            head = cur1
            cur1 = cur1.next
        else:
            head = cur2
            cur2 = cur2.next
        while cur1 and cur2:
            if cur1.val > cur2.val:
                head.next = cur1
                head = head.next
            else:
                head.next = cur2
                head = head.next
        return head


# 递归法
class Solution2:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: return l2
        if not l2: return l1
        if l1.val <= l2.val:
            ret = l1
            ret.next = self.mergeTwoLists(l1.next, l2)
        else:
            ret = l2
            ret.next = self.mergeTwoLists(l1, l2.next)
        return ret
