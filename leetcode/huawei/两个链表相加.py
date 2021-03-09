print(9 // 10)
print(9 % 10)


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 错的
class Solution:
    def addInList(self, head1, head2):
        # write code here
        reversed_head1 = self.reverse_list(head1)
        reversed_head2 = self.reverse_list(head2)
        new_head = ListNode((reversed_head1.val + reversed_head2.val) % 10)
        add = (reversed_head1.val + reversed_head2.val) // 10
        new_head.next = ListNode(0)
        cur = new_head.next
        reversed_head1 = reversed_head1.next
        reversed_head2 = reversed_head2.next
        while reversed_head1 and reversed_head2:
            sum = reversed_head1.val + reversed_head2.val
            cur.val = (sum + add) % 10
            add = (sum + add) // 10
            reversed_head1 = reversed_head1.next
            reversed_head2 = reversed_head2.next
            cur.next = ListNode(0)
            cur = cur.next
        return self.reverse_list(new_head)

    def reverse_list(self, head):
        pre = None
        cur = head
        while cur:
            next = cur.next  # 要预先存储一个next，防止进不去下一个
            cur.next = pre  # 反向
            pre = cur  # 前进一个
            cur = next  # 前进一个
        return pre

    def travel(self, head):
        """遍历整个链表"""
        cur = head
        while cur:
            print(cur.val, end=',')
            cur = cur.next
        print()


node1 = ListNode(9)
node1.next = ListNode(3)
node1.next.next = ListNode(7)

node2 = ListNode(6)
node2.next = ListNode(3)

s = Solution()
s.travel(s.addInList(node1, node2))


# public class Solution {
#     /**
#      *
#      * @param head1 ListNode类
#      * @param head2 ListNode类
#      * @return ListNode类
#      */
#     public ListNode addInList (ListNode head1, ListNode head2) {
#         // write code here
#         head1 = reverse(head1);
#         head2 = reverse(head2);
#         ListNode head = new ListNode(-1);
#         ListNode cur = head;
#         int carry = 0;
#         while(head1 != null || head2 != null) {
#             int val = carry;
#             if (head1 != null) {
#                 val += head1.val;
#                 head1 = head1.next;
#             }
#             if (head2 != null) {
#                 val += head2.val;
#                 head2 = head2.next;
#             }
#             cur.next = new ListNode(val % 10);
#             carry = val / 10;
#             cur = cur.next;
#         }
#         if (carry > 0) {
#             cur.next = new ListNode(carry);
#         }
#         return reverse(head.next);
#     }
#
#     private ListNode reverse(ListNode head) {
#         ListNode cur = head;
#         ListNode pre = null;
#         while(cur != null) {
#             ListNode temp = cur.next;
#             cur.next = pre;
#             pre = cur;
#             cur = temp;
#         }
#         return pre;
#     }
# }