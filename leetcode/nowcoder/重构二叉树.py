import tools.binary_tree as btree

class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # 出口
        if len(pre) == 1:
            head = TreeNode(pre[0])
            head.left = None
            head.right = None
            return head
        root_num = pre[0]
        index = tin.index(root_num)
        length = len(tin[:index])
        head = TreeNode(root_num)
        if index == 0:
            head.left = None
        else:
            head.left = self.reConstructBinaryTree(pre[1:length + 1], tin[:index])
        if index == len(pre)-1:
            head.right = None
        else:
            head.right = self.reConstructBinaryTree(pre[length + 1:], tin[index + 1:])
        return head

s =Solution()
res =s.reConstructBinaryTree([1, 2, 3, 4, 5, 6, 7], [3, 2, 4, 1, 6, 5, 7])
b = btree.BinaryTree(res)
b.breadth_travel()