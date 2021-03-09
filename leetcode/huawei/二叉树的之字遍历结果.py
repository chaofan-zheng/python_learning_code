"""给定一个二叉树，返回该二叉树的之字形层序遍历，（第一层从左向右，下一层从右向左，一直这样交替）"""

# 思路：和二叉树广度遍历差不多，用flag标记结果是否倒序打印

def zigzagLevelOrder(self, root):
    # write code here
    if root is None:
        return []
    result = []
    tmp = [root]
    flag = False
    while len(tmp) > 0:
        temp = []
        res = []
        for i in tmp:
            if i.left:
                temp.append(i.left)
            if i.right:
                temp.append(i.right)
            if not flag:
                res.append(i.val)
            else:
                res.insert(0, i.val)
        tmp = temp
        flag = not flag
        result.append(res)
    return result
