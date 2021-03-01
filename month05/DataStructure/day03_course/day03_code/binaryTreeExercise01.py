"""给定一棵二叉搜索树，找出其中第k小的节点"""

# 思路：搜索二叉树的中序遍历出来的是递增数列
#         所以在中序遍历的print步骤count一下，第k个的print就是最小的，那就可以让其他的不打印，让count=k的时候打印

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    count = 0

    def find_k_smallest(self, node, k):
        if not node:
            return
        self.find_k_smallest(node.left, k)
        self.count += 1
        if k == self.count:
            print(node.value)
        self.find_k_smallest(node.right, k)
