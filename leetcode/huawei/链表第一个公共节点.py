# 双指针法 让走过的长度为a+b即可
# 1234567和34567，找5，123456734567 = 345671234567
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        cur1, cur2 = pHead1, pHead2
        while cur1 != cur2:
            if cur1:
                cur1 = cur1.next
            else:
                cur1 = pHead2
            if cur2:
                cur2 = cur2.next
            else:
                cur2 = pHead1
        return cur1

