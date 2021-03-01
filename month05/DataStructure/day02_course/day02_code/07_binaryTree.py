"""
python实现二叉树
"""


class Node:
    """节点类"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        """ 初始化一棵空树,树根为None的树为空树 """
        self.root = None

    def add(self, item):
        """二叉树中添加1个节点，使用队列思想"""
        node = Node(item)
        q = [self.root]
        while True:
            # 空树情况,插入为根
            if not self.root:
                self.root = node
                return
            cur = q.pop(0)
            # 判断左孩子
            if cur.left: # 如果是空树，会报错
                q.append(cur.left) # 添加进列表用于左右孩子的判断
            else:
                # 直接添加节点，添加完以后直接return结束
                cur.left = node
                return
            # 判断右孩子
            if cur.right:
                q.append(cur.right)
            else:
                cur.right = node
                return

