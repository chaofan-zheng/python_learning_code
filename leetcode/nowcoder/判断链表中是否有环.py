"""快慢指针的解法， 一个指针走两步 一个指针走一步，如果快指针直接到了null 说明没有环， 如果有环的话 总有一次结果会让快指针和慢指针相等。"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
#
# @param head ListNode类
# @return bool布尔型
#
class Solution:
    def hasCycle(self, head):
        if head == None:
            return False
        quick_cur = head
        slow_cur = head
        if slow_cur.next == None:
            # 防止单个元素的链表进来
            return False
        while quick_cur != None and quick_cur.next != None:# 快慢指针要防止快指针走太快了溢出
            quick_cur = quick_cur.next.next
            slow_cur = slow_cur.next
            if quick_cur == None:
                return False
            if quick_cur == slow_cur:
                return True
