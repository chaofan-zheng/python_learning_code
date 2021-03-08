"""分别按照二叉树先序，中序和后序打印所有的节点。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
#
# @param root TreeNode类 the root of binary tree
# @return int整型二维数组
#
class Solution:

    def threeOrders(self, root):
        # write code here
        left_list = []
        mid_list = []
        right_list = []
        self.pre(root, left_list)
        self.mid(root, mid_list)
        self.after(root, right_list)
        return [left_list, mid_list, right_list]

    def pre(self, root, left_list):
        if not root:
            return
        left = root.left
        right = root.right
        left_list.append(root.val)
        self.pre(left, left_list)
        self.pre(right, left_list)

    def mid(self, root, mid_list):
        if not root:
            return
        left = root.left
        right = root.right
        self.mid(left, mid_list)
        mid_list.append(root.val)
        self.mid(right, mid_list)

    def after(self, root, right_list):
        if not root:
            return
        left = root.left
        right = root.right
        self.after(left, right_list)
        self.after(right, right_list)
        right_list.append(root.val)


s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(s.threeOrders(root))
