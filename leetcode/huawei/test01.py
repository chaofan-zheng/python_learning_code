""" 有两个链表，判断链表是否相交，True，False"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def solution(self, head1, head2):
        # a+b 就一样长了
        cur1, cur2 = head1, head2
        if cur1 == None or cur2 == None:
            return False
        count = 0
        while 1:
            if count == 2:
                return False
            if not cur1:
                cur1 = head2
                count += 1
            if not cur2:
                cur2 = head1
            if cur1 != cur2:
                cur1 = cur1.next
                cur2 = cur2.next
            else:
                return True


if __name__ == '__main__':
    # head1 = ListNode(1)
    # head1.next = ListNode(2)
    # head1.next.next = ListNode(3)
    # head1.next.next.next = ListNode(7)
    # head2 = ListNode(4)
    # head2.next = ListNode(5)
    # head2.next.next = ListNode(6)
    head1 = ListNode(1)
    head2 = head1

    s = Solution()
    print(s.solution(head1, head2))
