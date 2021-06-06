class Node:
    """节点类"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def mid(head):
    """
    使用递归的方法中序遍历二叉树
    """
    if not head:
        return
    mid(head.left)
    print(head.value)
    mid(head.right)


def left_root_right(head):
    """
    非递归的中序遍历法
    """
    p = head
    stack = list()
    while p or stack:
        if p:
            stack.append(p)
            p = p.left
        else:
            p = stack.pop()
            print(p.value)
            p = p.right


def root_left_right(head):
    """
    非递归的前序遍历法
    """
    p = head
    stack = list()
    while p or stack:
        if p:
            print(p.value)
            stack.append(p)
            p = p.left
        else:
            p = stack.pop()
            p = p.right


def left_right_root(head):
    """
    非递归的后序遍历法
    """
    p = head
    stack = list()
    visited_right = []
    while p or stack:
        if p:
            stack.append(p)
            p = p.left
        else:
            p = stack.pop()
            stack.append(p)
            if p.right and p.right not in visited_right:
                p = p.right
                visited_right.append(p)
            else:
                stack.pop()
                print(p.value)
                p = None


def queue_search(head):
    """
    层次遍历
    """
    my_queue = [head]
    while my_queue:
        q = my_queue.pop(0)
        print(q.value)
        if q.left:
            my_queue.append(q.left)
        if q.right:
            my_queue.append(q.right)


class TreeNode(object):
    def __init__(self, val=-1):
        self.val = val
        self.left = None
        self.right = None
        # 新增类型指针
        # 规定：
        # 如果left_type==0 表示指向的是左子树，如果是1 则表示指向前驱结点
        # 如果right_type==0 表示指向的是右子树，如果是1 怎表示指向后继结点
        self.left_type = 0  # 注意这里必须写0，不能写空值
        self.right_type = 0


class ThreadedBinaryTree(object):
    def __init__(self):
        self.root = None
        # 在递归进行线索化，总是保留前一个结点
        self.pre = None  # 为实现线索化，需要创建给指向当前结点的前驱结点指针

    # 添加结点测试
    def add(self, val):
        node = TreeNode(val)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            temp_node = queue.pop(0)
            if temp_node.left is None:
                temp_node.left = node
                return
            else:
                queue.append(temp_node.left)
            if temp_node.right is None:
                temp_node.right = node
                return
            else:
                queue.append(temp_node.right)

    # 中序遍历测试
    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.left)
        print(node.val, end=' ')
        self.in_order(node.right)

    # 二叉树进行中序线索化的方法
    def threaded_node(self, node):  # node: 就是当前需要线索化的结点
        if node is None:
            return
        # 先线索化左子树
        self.threaded_node(node.left)

        # 线索化当前结点
        # 处理当前结点的前驱结点
        if node.left is None:  # 如果当前结点左子结点为空
            node.left = self.pre  # 让当前结点的左指针指向前驱结点
            node.left_type = 1  # 修改当前结点的左指针类型 为 前驱结点
        # 处理当前结点的后继结点
        if self.pre and self.pre.right is None:
            self.pre.right = node  # 让前驱结点的右指针指向当前结点
            self.pre.right_type = 1  # 修改前驱结点的右指针类型
        self.pre = node  # 每处理一个结点后，让当前结点是下一个结点的前驱结点

        # 线索化右子树
        self.threaded_node(node.right)

    def threaded_pre_node(self, node):  # node: 就是当前需要线索化的结点
        if not node:
            return
        # 线索化当前结点
        # 处理当前结点的前驱结点
        """这很重要。。一定要先拿出来！！"""
        left_node = node.left
        right_node = node.right
        if node.left is None:  # 如果当前结点左子结点为空
            node.left = self.pre  # 让当前结点的左指针指向前驱结点
            node.left_type = 1  # 修改当前结点的左指针类型 为 前驱结点
        # 处理当前结点的后继结点
        if self.pre and self.pre.right is None:
            self.pre.right = node  # 让前驱结点的右指针指向当前结点
            self.pre.right_type = 1  # 修改前驱结点的右指针类型
        self.pre = node  # 每处理一个结点后，让当前结点是下一个结点的前驱结点

        # 先线索化左子树
        self.threaded_pre_node(left_node)
        # 线索化右子树
        self.threaded_pre_node(right_node)

    def threaded_in_order(self, node):
        """
        循环遍历线索二叉树办法
        """
        if node is None:
            return
        temp_node = node
        while temp_node:
            # 循环的找到left_type=1的结点，第一个找到就是值为8的结点
            # 后面随着遍历而变化，因为当left_type=1时，说明该结点是按照线索化处理后的有效结点
            while temp_node.left_type == 0:  # 从根结点开始向左找，找到第一个1停止
                temp_node = temp_node.left
            # 打印当前这个结点
            print(temp_node.val, end=" ")
            # 如果当前结点的右指针指向的是后继结点，就一直输出
            while temp_node.right_type == 1:
                # 获取到当前结点的后继结点
                temp_node = temp_node.right
                print(temp_node.val, end=" ")
            # 如果不等于1了，就替换这个遍历的结点
            temp_node = temp_node.right
    def thread_pre_order(self,node):
        if node is None:
            return
        temp_node = node
        while temp_node:
            print(temp_node.val)
            if temp_node.left_type ==0 and temp_node.left:
                temp_node = temp_node.left
            else:
                while temp_node.right_type ==1:
                    temp_node = temp_node.right
                    print(temp_node.val)
                break
                temp_node = temp_node.right


if __name__ == '__main__':
    # head = Node('A')
    # head.left = Node('B')
    # head.right = Node('C')
    # head.left.left = Node('D')
    # head.left.right = Node('E')
    # left_root_right(head)
    # root_left_right(head
    # left_right_root(head)
    # queue_search(head)
    # mid(head)
    t = ThreadedBinaryTree()
    t1 = TreeNode(1)
    t2 = TreeNode(3)
    t3 = TreeNode(6)
    t4 = TreeNode(8)
    t5 = TreeNode(10)
    t6 = TreeNode(14)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    # print("原来的二叉树中序遍历为：")
    # t.in_order(t1)
    # # 线索化二叉树
    # t.threaded_node(t1)
    # # 测试：以值为10 的结点来测试
    # left_node = t5.left
    # print()
    # print("10 的前驱结点是：%d" % left_node.val)  # 3
    # right_node = t5.right
    # print("10 的后继结点是：%d" % right_node.val)  # 1
    # print("线索化二叉树的中序遍历结果为：")
    # t.threaded_in_order(t1)
    t.threaded_pre_node(t1)
    left_node = t4.left
    print()
    print("8 的前驱结点是：%d" % left_node.val)  # 3
    right_node = t4.right
    print("8 的后继结点是：%d" % right_node.val)  # 1
    t.thread_pre_order(t1)

