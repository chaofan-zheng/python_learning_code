# **Day02笔记**

## **作业讲解**

### **链表作业题一**

- **题目描述 + 试题解析**

  ```python
  【1】题目描述
      输入一个链表，输出该链表中倒数第 k 个节点
    
  【2】试题解析
      可将链表中的每一个元素保存到列表中，在列表中寻找倒数第 k 个元素
  ```

- **代码实现**

  ```python
  """
  输入一个链表，输出该链表中倒数第 k 个节点
  思路:
      1、链表只能从头到尾遍历,从尾到头遍历存在难度
      2、从头到尾遍历,将节点数据添加到一个列表中
      3、利用列表的下标索引取出对应的节点数据
  """
  class Node:
      """节点类"""
      def __init__(self, value):
          self.value = value
          self.next = None
  
  class Solution:
      def get_k_node(self, head, k):
          # 1.把链表中节点数据添加到列表中
          li = []
          cur = head
          while cur:
              li.append(cur.value)
              cur = cur.next
          # 2.利用列表的索引取出对应值
          if k > len(li):
              raise IndexError('list index out of range')
  
          return li[-k]
  
  if __name__ == '__main__':
      s = Solution()
      # 创建链表: 100 -> 200 -> 300 -> None
      head = Node(100)
      head.next = Node(200)
      head.next.next = Node(300)
      # 终端1: 200
      print(s.get_k_node(head, 2))
      # 终端2: list index out of range
      print(s.get_k_node(head, 8))
  ```

### **链表作业题二**

- **题目描述 + 试题解析**

  ```python
  【1】题目描述
      输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则
    
  【2】试题解析
      a> 比较两个链表的头节点，确认合成后链表的头节点
      b> 继续依次比较两个链表元素的大小，将元素小的结点插入到新的链表中，直到一个链 表为空
  ```

- **代码实现**

  ```python
  """
  输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则
  思路:
      1、程序最终返回的是: 合并后的链表的头节点
      2、先确定新链表的头节点
      3、互相比较,移动值小的游标
  """
  class Node:
      """节点类"""
      def __init__(self, value):
          self.value = value
          self.next = None
  
  class Solution:
      def merge_two_link_list(self, head1, head2):
          # 1.确定新链表的头节点
          h1 = head1
          h2 = head2
          if h1 and h2:
              if h1.value >= h2.value:
                  merge_head = h2
                  h2 = h2.next
              else:
                  merge_head = h1
                  h1 = h1.next
              # p即为最终返回的结果
              p = merge_head
          elif h1:
              return h1
          else:
              return h2
          # 2.遍历两个链表进行比较合并
          while h1 and h2:
              if h1.value <= h2.value:
                  merge_head.next = h1
                  h1 = h1.next
              else:
                  merge_head.next = h2
                  h2 = h2.next
              # 移动新链表的游标
              merge_head = merge_head.next
  
          # 3.循环结束后,一定有一个游标为None(或者说一定有一个链表遍历完了)
          if h2:
              merge_head.next = h2
          elif h1:
              merge_head.next = h1
  
          # 4.最终返回新链表的头节点
          return p
  
  if __name__ == '__main__':
      s = Solution()
      # 链表1: 100 -> 200 -> 300 -> 400 -> None
      head1 = Node(100)
      head1.next = Node(200)
      head1.next.next = Node(300)
      head1.next.next.next = Node(400)
      # 链表2: 1 -> 200 -> 600 -> 800 -> None
      head2 = Node(1)
      head2.next = Node(200)
      head2.next.next = Node(600)
      head2.next.next.next = Node(800)
      # 合并
      p = s.merge_two_link_list(head1, head2)
      # 结果: 1 100 200 200 300 400 600 800
      while p:
          print(p.value, end=' ')
          p = p.next
  ```

## **线性表 - 栈（LIFO)**

- **定义**

  ```python
  栈是限制在一端进行插入操作和删除操作的线性表（俗称堆栈），允许进行操作的一端称为"栈顶"，另一固定端称为"栈底"，当栈中没有元素时称为"空栈"
  ```

- **特点**

  ```python
  【1】栈只能在一端进行数据操作
  【2】栈模型具有后进先出的规律（LIFO）
  ```

![栈](./img/data2.png)

- **顺序栈代码实现**

  ```python
  """
  顺序存储的方式实现栈
  思路：
      1、栈 ：LIFO 后进先出
      2、设计
         列表尾部作为栈顶（入栈、出栈操作）
         列表头部作为栈底（不进行任何操作）
  """
  class Stack:
      def __init__(self):
          """初始化一个空栈"""
          self.elems = []
  
      def is_empty(self):
          """判断栈是否为空栈"""
          return self.elems == []
  
      def push(self, item):
          """入栈: 相当于在链表尾部添加1个元素"""
          self.elems.append(item)
  
      def destack(self):
          """出栈: 相当于在列表尾部弹出1个元素"""
          if self.is_empty():
              raise Exception('destack from empty stack')
          return self.elems.pop()
  
  if __name__ == '__main__':
      s = Stack()
      # 栈(栈底->栈顶): 100 200 300
      s.push(100)
      s.push(200)
      s.push(300)
      # 终端1: 300 200 100 异常
      print(s.destack())
      print(s.destack())
      print(s.destack())
      print(s.destack())
  ```

- **链式栈代码实现**

  ```python
  """
  链式存储方式实现栈
  思路：
      1、栈：LIFO 后进先出
      2、设计
         链表头部作为栈顶（入栈、出栈操作）
         链表尾部作为栈底（不进行任何操作）
  """
  class Node:
      """节点类"""
      def __init__(self, value):
          self.value = value
          self.next = None
  
  class LinkListStack:
      def __init__(self):
          """初始化一个空栈"""
          self.head = None
  
      def is_empty(self):
          """判断是否为空栈"""
          return self.head == None
  
      def push(self, item):
          """入栈操作: 相当于在链表的头部添加一个节点"""
          node = Node(item)
          node.next = self.head
          self.head = node
  
      def pop(self):
          """出栈操作: 相当于删除链表头节点"""
          if self.is_empty():
              raise Exception('pop from empty LinkListStack')
          item = self.head.value
          self.head = self.head.next
  
          return item
  
  if __name__ == '__main__':
      s = LinkListStack()
      # 栈（栈底->栈顶）：300 200 100
      s.push(100)
      s.push(200)
      s.push(300)
      # 终端1: 300
      print(s.pop())
      # 终端2: False
      print(s.is_empty())
  ```

## **线性表 - 队列（FIFO）**

- **定义**

  ```python
  队列是限制在两端进行插入操作和删除操作的线性表，允许进行存入操作的一端称为"队尾"，允许进行删除操作的一端称为"队头"
  ```

- **特点**

  ```python
  1) 队列只能在队头和队尾进行数据操作
  2) 队列模型具有先进先出规律（FIFO）
  ```

![队列](./img/data3.png)

- **顺序队列代码实现** 

  ```python
  """
  顺序存储方式去实现队列模型
  思路：
      1、队列：FIFO 先进先出,队尾负责入队,队头负责出队
      2、设计：
         列表头部作为队头,负责出队
         列表尾部作为队尾,负责入队
  """
  class Queue:
      def __init__(self):
          """初始化一个空队列"""
          self.elems = []
  
      def is_empty(self):
          """判断队列是否为空"""
          return self.elems == []
  
      def enqueue(self, item):
          """队尾入队: append(item)"""
          self.elems.append(item)
  
      def dequeue(self):
          """队头出队: pop(0)"""
          if self.is_empty():
              raise Exception('dequeue from empty Queue')
          return self.elems.pop(0)
  
  if __name__ == '__main__':
      q = Queue()
      # 队列: 100 200 300
      q.enqueue(100)
      q.enqueue(200)
      q.enqueue(300)
      # 终端1: 100
      print(q.dequeue())
      # 终端2: False
      print(q.is_empty())
  ```

- **链式队列代码实现**

  ```python
  """
  链式存储方式去实现队列
  思路：
      1、队列：FIFO 先进先出
      2、设计：
         链表头部作为队头,负责出队操作
         链表尾部作为队尾,负责入队操作
  """
  class Node:
      def __init__(self, value):
          self.value = value
          self.next = None
  
  class LinkListQueue:
      def __init__(self):
          """初始化一个空队列"""
          self.head = None
  
      def is_empty(self):
          """判断队列是否为空"""
          return self.head == None
  
      def enqueue(self, item):
          """队尾入队: 相当于在链表尾部添加一个节点"""
          node = Node(item)
          # 空队列情况
          if self.is_empty():
              self.head = node
              return
          # 非空队列
          cur = self.head
          while cur.next:
              cur = cur.next
          # 循环结束后,cur一定是指向了原链表尾节点
          cur.next = node
          node.next = None
  
      def dequeue(self):
          """队头出队: 相当于删除链表头节点"""
          if self.is_empty():
              raise Exception('dequeue from empty LinkListQueue')
          cur = self.head
          # 删除头节点
          self.head = self.head.next
  
          return cur.value
  
  if __name__ == '__main__':
      q = LinkListQueue()
      # 队列: 100 200 300
      q.enqueue(100)
      q.enqueue(200)
      q.enqueue(300)
      # 终端1: 100
      print(q.dequeue())
      # 终端2: False
      print(q.is_empty())
  ```


## **树形结构**

- **定义**

  ```python
  树（Tree）是n（n≥0）个节点的有限集合T，它满足两个条件：有且仅有一个特定的称为根（Root）的节点；其余的节点可以分为m（m≥0）个互不相交的有限集合T1、T2、……、Tm，其中每一个集合又是一棵树，并称为其根的子树（Subtree）
  ```

![tree](./img/tree1.png)

- **基本概念** 

  ```python
  # 1. 树的特点
  * 每个节点有零个或者多个子节点
  * 没有父节点的节点称为根节点
  * 每一个非根节点有且只有一个父节点
  * 除了根节点外,每个子节点可以分为多个不相交的子树
  
  # 2. 相关概念
  1) 节点的度: 一个节点的子树的个数
  2) 树的度: 一棵树中,最大的节点的度成为树的度
  3) 叶子节点: 度为0的节点
  4) 父节点
  5) 子节点
  6) 兄弟节点
  7) 节点的层次: 从根开始定义起,根为第1层
  8) 深度: 树中节点的最大层次
  ```

![](./img/tree2.png)

## **二叉树**

- **定义**

  ```python
  二叉树（Binary Tree）是n（n≥0）个节点的有限集合，它或者是空集（n＝0），或者是由一个根节点以及两棵互不相交的、分别称为左子树和右子树的二叉树组成。二叉树与普通有序树不同，二叉树严格区分左孩子和右孩子，即使只有一个子节点也要区分左右
  ```

![](./img/tree3.png)

- **二叉树的分类 - 见图**

  ```python
  【1】完全二叉树
      对于一颗二叉树，假设深度为d，除了d层外，其它各层的节点数均已达到最大值，并且第d层所有节点从左向右连续紧密排列
  
  【2】满二叉树
      所有叶节点都在最底层的完全二叉树
      
  【3】二叉排序树('二叉搜索树')
      任何一个节点，所有左边的值都会比此节点小，所有右边的值都会比此节点大
      
  【4】平衡二叉树
      当且仅当任何节点的两棵子树的高度差不大于1的二叉树
  ```

- **二叉树 - 添加元素代码实现**

  ```python
  """
  二叉树
  """
  
  class Node:
      def __init__(self, value):
          self.value = value
          self.left = None
          self.right = None
  
  class Tree:
      def __init__(self, node=None):
          """创建了一棵空树或者是只有树根的树"""
          self.root = node
  
      def add(self, value):
          """在树中添加一个节点"""
          node = Node(value)
          # 空树情况
          if self.root is None:
              self.root = node
              return
  
          # 不是空树的情况
          node_list = [self.root]
          while node_list:
              cur = node_list.pop(0)
              # 判断左孩子
              if cur.left is None:
                  cur.left = node
                  return
              else:
                  node_list.append(cur.left)
  
              # 判断右孩子
              if cur.right is None:
                  cur.right = node
                  return
              else:
                  node_list.append(cur.right)
  ```

### **广度遍历 - 二叉树**



- **广度遍历 - 代码实现**

  ```python
      def breadth_travel(self):
          """广度遍历 - 队列思想（即：列表的append()方法 和 pop(0) 方法"""
          # 1、空树的情况
          if self.root is None:
              return
          # 2、非空树的情况
          node_list = [self.root]
          while node_list:
              cur = node_list.pop(0)
              print(cur.value, end=' ')
              # 添加左孩子
              if cur.left is not None:
                  node_list.append(cur.left)
              # 添加右孩子
              if cur.right is not None:
                  node_list.append(cur.right)
  
          print()
  ```

### **深度遍历 - 二叉树**

```python
【1】遍历
    沿某条搜索路径周游二叉树，对树中的每一个节点访问一次且仅访问一次。

【2】遍历方式
    2.1) 前序遍历： 先访问树根，再访问左子树，最后访问右子树 - 根 左 右
    2.2) 中序遍历： 先访问左子树，再访问树根，最后访问右子树 - 左 根 右
    2.3) 后序遍历： 先访问左子树，再访问右子树，最后访问树根 - 左 右 根
```



![](./img/完全二叉树.jpg)



```python
【1】前序遍历结果: 1 2 4 8 9 5 10 3 6 7
【2】中序遍历结果: 8 4 9 2 10 5 1 6 3 7
【3】后序遍历结果: 8 9 4 10 5 2 6 7 3 1
```

- **深度遍历 - 代码实现**

  ```python
  # 前序遍历
      def pre_travel(self, node):
          """前序遍历 - 根左右"""
          if node is None:
              return
  
          print(node.value, end=' ')
          self.pre_travel(node.left)
          self.pre_travel(node.right)
  
  # 中序遍历
      def mid_travel(self, node):
          """中序遍历 - 左根右"""
          if node is None:
              return
  
          self.mid_travel(node.left)
          print(node.value, end=' ')
          self.mid_travel(node.right)
  
  # 后续遍历
      def last_travel(self, node):
          """后序遍历 - 左右根"""
          if node is None:
              return
  
          self.last_travel(node.left)
          self.last_travel(node.right)
          print(node.value, end=' ')
  ```

- **二叉树完整代码**

  ```python
  """
  python实现二叉树
  """
  
  class Node:
      def __init__(self, value):
          self.value = value
          self.left = None
          self.right = None
  
  class Tree:
      def __init__(self, node=None):
          """创建了一棵空树或者是只有树根的树"""
          self.root = node
  
      def add(self, value):
          """在树中添加一个节点"""
          node = Node(value)
          # 空树情况
          if self.root is None:
              self.root = node
              return
  
          # 不是空树的情况
          node_list = [self.root]
          while node_list:
              cur = node_list.pop(0)
              # 判断左孩子
              if cur.left is None:
                  cur.left = node
                  return
              else:
                  node_list.append(cur.left)
  
              # 判断右孩子
              if cur.right is None:
                  cur.right = node
                  return
              else:
                  node_list.append(cur.right)
  
      def breadth_travel(self):
          """广度遍历 - 队列思想（即：列表的append()方法 和 pop(0) 方法"""
          # 1、空树的情况
          if self.root is None:
              return
          # 2、非空树的情况
          node_list = [self.root]
          while node_list:
              cur = node_list.pop(0)
              print(cur.value, end=' ')
              # 添加左孩子
              if cur.left is not None:
                  node_list.append(cur.left)
              # 添加右孩子
              if cur.right is not None:
                  node_list.append(cur.right)
  
          print()
  
      def pre_travel(self, node):
          """前序遍历 - 根左右"""
          if node is None:
              return
  
          print(node.value, end=' ')
          self.pre_travel(node.left)
          self.pre_travel(node.right)
  
      def mid_travel(self, node):
          """中序遍历 - 左根右"""
          if node is None:
              return
  
          self.mid_travel(node.left)
          print(node.value, end=' ')
          self.mid_travel(node.right)
  
      def last_travel(self, node):
          """后序遍历 - 左右根"""
          if node is None:
              return
  
          self.last_travel(node.left)
          self.last_travel(node.right)
          print(node.value, end=' ')
  
  if __name__ == '__main__':
      tree = Tree()
      tree.add(1)
      tree.add(2)
      tree.add(3)
      tree.add(4)
      tree.add(5)
      tree.add(6)
      tree.add(7)
      tree.add(8)
      tree.add(9)
      tree.add(10)
      # 广度遍历：1 2 3 4 5 6 7 8 9 10
      tree.breadth_travel()
      # 前序遍历：1 2 4 8 9 5 10 3 6 7
      tree.pre_travel(tree.root)
      print()
      # 中序遍历:8 4 9 2 10 5 1 6 3 7
      tree.mid_travel(tree.root)
      print()
      # 后序遍历：8 9 4 10 5 2 6 7 3 1
      tree.last_travel(tree.root)
  ```



