# **数据结构与算法-Day01**

## **算法概述**

- **算法-前序**

  ```python
  【1】Everybody!全场动作必须跟我整齐划一，来，我们一起来做一道题
      若n1+n2+n3=1000,且n1^2+n2^2=n3^2(n1,n2,n3为自然数),求出所有n1、n2、n3可能的组合
  
  【2】解题思路
      n1 = 0
      n2 = 0
      n3 = 0
      判断n1+n2+n3是否等于1000,之后变n3=1,n3=2,n3=3,... 然后再变n2
  
  【3】代码实现
      import time
  
      start_time = time.time()
      for n1 in range(0,1001):
          for n2 in range(0,1001):
              for n3 in range(0,1001):
                  if n1 + n2 + n3 == 1000 and n1**2 + n2**2 == n3**2:
                      print('[%d,%d,%d]' % (n1,n2,n3))
      end_time = time.time()
      print('执行时间:%.2f' % (end_time-start_time))
      
  【4】算法概念
      4.1) 解决问题的方法，是指解题方案的准确而完整的描述，是一系列解决问题的清晰指令
      4.2) 算法代表着用系统的方法描述解决问题的策略机制
  ```


## **时间复杂度概述**

- **时间复杂度 - 前序**

  ```python
  【1】各位，一万年太久，只争朝夕，来提升一下上题的效率吧！！！
      for n1 in range(0,1001):
          for n2 in range(0,1001):
              n3 = 1000 - n1 - n2
              if n1**2 + n2**2 == n3**2:
                  print('[%d,%d,%d]'%(n1,n2,n3))
  
  【2】总结与思考 : 解决同一个问题有多种算法,但是效率有区别,那么如何衡量呢？
      2.1) 执行时间反应算法效率 - 绝对靠谱吗？
           不是绝对靠谱: 因机器配置有高有低,不能冒然绝对去做衡量
    
      2.2) 那如何衡量更靠谱？？？
           运算数量 - 执行步骤的数量
         
  【4】时间复杂度概念
      4.1) 同一个算法，由于机器配置差异,每台机器执行的总时间不同,但是执行基本运算的数量大体相同，所以把算法执行步骤的数量称为时间复杂度
  ```

- **时间复杂度 - 大O表示法前序**

  ```python
  ################################################################
  【1】计算此算法的时间复杂度
      for n1 in range(0,1001):
          for n2 in range(0,1001):
              for n3 in range(0,1001):
                  if n1 + n2 + n3 == 1000 and n1**2 + n2**2 == n3**2:
                      print('[%d,%d,%d]' % (n1,n2,n3))
  ################################################################
  【2】计算步骤                
      T = 1000 * 1000 * 1000 * 2
      T = n * n * n * 2
      T(n) = n ** 3 * 2  即时间复杂度为: T(n)=n**3 * 2
  
  【3】时间复杂度T(n)的 大O表示法
      3.1) 函数1: T(n)=k * n**3 + c
      3.2) 函数2: g(n)=n**3
      3.3) 特点: 在趋向无穷的极限意义下，函数T(n)的增长速度受到函数g(n)的约束，也为函数T(n)与函数g(n)的特征相似，则称 g(n) 是 T(n) 的渐近函数，大O表示法则使用渐近函数来表示
          即: O(g(n)) 
          即: O(n^3)
          即: 上述时间复杂度为 O(n^3)
  
  【4】时间复杂度总结           
      4.1) 假设存在函数g，使得算法A处理规模为n的问题所用时间为T(n)=O(g(n))，则称O(g(n))为算法A的渐近时间复杂度，简称时间复杂度，记为T(n)
      4.2） 对算法进行特别具体细致分析虽然好，但实践中实际价值有限。对我们来说算法的时间性质和空间性质最重要的是数量级和趋势，这些是分析算法效率的主要部分。所以忽略系数，忽略常数，比如5*n^2 和 100*n^2属于一个量级，时间复杂度为O(n^2)
  ```

- **时间复杂度分类**

  ```python
  【1】最优时间复杂度 - 最少需要多少个步骤
  【2】最坏时间复杂度 - 最多需要多少个步骤
  【3】平均时间复杂度 - 平均需要多少个步骤
  
  我们平时所说的时间复杂度,指的是最坏时间复杂度
  ```

## **时间复杂度 - 计算规则**

- **计算原则**

  ```python
  【1】基本操作,只有常系数，认为其时间复杂度为O(1)
      顺序 - 基本步骤之间的累加
      print('abc') -> O(1)
      print('abc') -> O(1)
  
  【2】循环: 时间复杂度按乘法进行计算
      
  【3】分支: 时间复杂度取最大值(哪个分支执行次数多算哪个)
  
  【4】练习:请计算如下代码的时间复杂度
      for n1 in range(0,1001):
          for n2 in range(0,1001):
              n3 = 1000 - n1 - n2
              if n1**2 + n2**2 == n3**2:
                  print('[%d,%d,%d]'%(n1,n2,n3))
              
  T(n) = n * n * (1+1+max(1,0))
  T(n) = n**2 * 3
  T(n) = n**2
  T(n) = O(n**2)
  用大O表示法表示为 Tn = O(n^2)
  ```

- **常见时间复杂度**

  | 执行次数           | 时间复杂度 | 阶     |
  | ------------------ | ---------- | ------ |
  | 20（20个基本步骤） | O(1)       | 常数阶 |
  | 8n+6               | O(n)       | 线性阶 |
  | 2n^2 + 4n + 2      | O(n^2)     | 平方阶 |
  | 8logn + 16         | O(logn)    | 对数阶 |
  | 4n + 3nlogn + 22   | O(nlog(n)) | nlog阶 |
  | 2n^3 + 2n^2 + 4    | O(n^3)     | 立方阶 |
  | 2 ^ n              | O(2^n)     | 指数阶 |

- **O(1)**

  ```python
  【1】O(1)
      print('全场动作必须跟我整齐划一')
  
  【2】O(1)
      print('左边跟我一起画个龙')
      print('在你右边画一道彩虹')
      print('走起')
      print('左边跟我一起画彩虹')
      print('在你右边再画一条龙')
  ```

- **O(n)**

  ```python
  for i in range(n):
    print('在胸口比划一个郭富城')
  ```

- **O(n^2)**

  ```python
  【1】O(n^2)
      for i in range(n):
          for j in range(n):
              print('左边右边摇摇头')
      
  【2】O(n^2)
      for i in range(n):
          print('两根手指就像两个窜天猴')
          for j in range(n):
              print('指向闪耀的灯球')
  ```
  
- **O(n^3)**

  ```python
  for i in range(n):
      for j in range(n):
          for k in range(n):
              print('走你')
  ```

- **O(logn)**

  ```python
  # 【此生铭记】: 循环减半,时间复杂度为logn
  n = 64
  while n > 1:
      print(n)
      n = n // 2
  
  【解释】
  2的6次方 等于 64，log264 = 6，所以循环减半的时间复杂度为O(log2n)，即O(logn)
  如果是循环减半的过程，时间复杂度为O(logn)或O(log2n)
  ```

- **O(nlogn)**

  ```python
  for j in range(n):
      i = 1
      while i <= n:
          i = i * 2
  ```
  
- **常见时间复杂度排序**

  ```python
  O(1)<O(logn)<O(n)<O(nlogn)<O(n2)<O(n2logn)<O(n3)
  ```

- **练习: 写出如下的时间复杂度**

  ```python
  O(5)          --> O(1)
  O(2n+1)       --> O(n)
  O(n**2+n+1)   --> O(n**2)
  O(3n**3+1)    --> O(n**3)
  ```

- **终极总结两句话**

  ```python
  【1】时间复杂度是多少： T(n) = O(???)
  【2】去掉系数、去掉常数、去掉低次幂，最终得到时间复杂度
  ```

## **数据结构概述**

- **数据结构描述**

  ```python
  【1】概述
      1.1) 在工作中，我们为了解决问题，需要将数据保存下来，然后根据数据存储方式设计算法进行处理，根据数据的存储方式我们使用不同的算法处理，而我们现在需要考虑算法解决问题的效率问题，所以需要考虑数据究竟如何保存，这就是数据结构
    
  【2】概念
      2.1) 数据是一个抽象的概念，将其进行分类后得到程序设计语言中的基本类型，如：list、tuple等。数据元素之间不是独立的，存在特定的关系，这些关系便是结构。数据结构指数据对象中数据元素之间的关系
      2.2) Python提供了很多现成的数据结构类型，如列表、元组、字典等，无须我们自己去定义，而Python没有定义的，就需要我们自己去定义实现这些数据的组织方式，称为Python扩展数据结构，如：栈、队列等
  
  【3】为什么学习数据结构
     在真正的项目开发中，大部分时间都是从数据库取数据 -> 数据操作和结构化 -> 返回给前端，在数据操作过程中需要合理地抽象，组织、处理数据，如果选用了错误的数据结构，就会造成代码运行低效
  ```
  
- **数据结构分类**

  ```python
  【1】线性结构 : n个数据元素的有序集合
      1.2) 顺序表 : 将数据结构中各元素按照其逻辑顺序存放于存储器一片连续的存储空间中
      1.3) 链表   : 将数据结构中各元素分布到存储器的不同点，用记录下一个结点位置的方式建立它们之间的联系
      1.4) 栈 : 后进先出
      1.5) 队列 : 先进先出
      
  【2】非线性结构
      2.1) 树形结构
      2.2) 图状结构
  ```

- **数据结构+算法总结**

  ```python
  【1】数据结构只是静态描述了数据元素之间的关系
  【2】高效的程序需要在数据结构的基础上设计和选择算法
  【3】程序 = 数据结构 + 算法
  【4】算法是为了解决实际问题而设计的，数据结构是算法需要处理的问题载体
  ```

## **抽象数据类型**

- **概念**

  ```python
  【1】定义
      抽象数据类型是指一个数学模型以及定义在此数学模型上的一组操作，及把数据类型和数据类型上的运算捆在一起进行封装。引入抽象数据类型的目的是把数据类型的表示和数据类型上的运算的实现与这些数据类型和运算在程序中的引用隔开，使他们相互独立
  
  【2】描述
      把原有的基本数据和这个数据所支持的操作放到一起，形成一个整体
  
  【3】最常用的数据运算
      3.1) 插入
      3.2) 删除
      3.3) 修改
      3.4) 查找
      3.5) 排序
  ```

## **线性表 - 顺序表**


- **顺序表的基本形式**

  ```python
  【1】特点 : 内存连续
  【2】分类
      2.1) 基本形式: 数据元素本身连续存储,每个元素所占存储单元大小固定相同
      2.2) 元素外置: 数据元素不连续存储，地址单元连续存储
  ```

## **线性表 - 链表**

- **定义**

  ```python
  【1】特点:
      1.1) 内存不连续的，而是一个个串起来的，需要每个链表的节点保存一个指向下一个节点的指针
    
  【2】和顺序表的对比
      2.1) 顺序表的构建需要预先知道数据大小来申请连续的存储空间，而在进行扩充时又需要进行数据的搬迁，使用起来不灵活，而链表结构可以充分利用计算机的内存空间，实现灵活的内存动态管理
  ```

- **示例 - 强化理解**

  ```python
  将线性表L=(a0,a1,……,an-1)中各元素分布在存储器的不同存储块，称为结点，每个结点（尾节点除外）中都持有一个指向下一个节点的引用，这样所得到的存储结构为链表结构
  ```

  ![链表结构](./img/data1.png)

- **单链表 - 代码实现**

  ```python
  """
  创建单链表的数据结构：
  1、节点类 - 数据区、链接区
  2、单链表类(数学模型): 增加、删除... ...
  """
  
  class Node:
      """节点类"""
      def __init__(self, value):
          self.value = value
          self.next = None
  
  class SingleLinkList:
      """单链表类"""
      def __init__(self, node=None):
          """创建链表时: s=SingleLinkList()表示空链表,s=SingleLinkList(Node(100)) 表示有1个节点的单链表"""
          self.head = node
  
      def is_empty(self):
          """判断链表是否为空"""
          return self.head == None
  
      def lengh(self):
          """获取链表长度"""
          # 游标：从头节点开始,一直往后移动,移动一次,+1
          current = self.head
          count = 0
          while current is not None:
              count += 1
              current = current.next
  
          return count
  
      def travel(self):
          """遍历整个链表"""
          current = self.head
          while current is not None:
              print(current.value,end=" ")
              current = current.next
          # 因为上面是end=" ",所以此处打印一个换行
          print()
  
      def add(self, item):
          """链表头部添加1个节点"""
          node = Node(item)
          # 1、把新添加的节点指针指向原来头节点
          node.next = self.head
          # 2、添加的节点设置为新的头
          self.head = node
  
      def append(self, item):
          """链表尾部添加1个节点,考虑空链表特殊情况"""
          node = Node(item)
          if self.is_empty():
              self.head = node
          else:
              current = self.head
              while current.next is not None:
                  current = current.next
              # 循环结束后,current指向尾节点
              current.next = node
              node.next = None
  
      def search(self, item):
          """查看在链表中是否存在"""
          current = self.head
          while current != None:
              if current.value == item:
                  return True
              else:
                  current = current.next
  
          return False
  
      def insert(self, pos, item):
          """在指定索引添加一个节点,索引值从0开始"""
          if pos < 0:
              self.add(item)
          elif pos > self.lengh() - 1:
              self.append(item)
          else:
              pre = self.head
              count = 0
              while count < (pos - 1):
                  count += 1
                  pre = pre.next
  
              # 循环结束后,pos指向(pos-1)位置
              node = Node(item)
              node.next = pre.next
              pre.next = node
  
  if __name__ == '__main__':
      s = SingleLinkList()
      # 终端1：True
      print(s.is_empty())
      # 链表：Node(100) -> Node(200) -> Node(300)
      s.add(200)
      s.add(100)
      s.append(300)
      # 终端2：3
      print(s.lengh())
      # 终端3：100 200 300
      s.travel()
      # 100 666 200 300
      s.insert(1, 666)
      # 终端4: 100 666 200 300
      s.travel()
      # 终端5: True
      print(s.search(666))
  ```
  

### **链表练习**

- **题目**

  ```python
  【1】题目描述
      输入一个链表，反转链表后，输出新链表的表头
    
  【2】试题解析
      可以将链表的每一个节点取出来，插入到新的链表表头，同时要保存原链表的下一个节点
  ```

- **代码实现**

  ```python
  """
  输入一个链表，反转链表后，输出新链表的表头
  思路:
      1、创建2个游标,代表要进行反转操作的节点 和 上一个节点
      2、代码逻辑:
         当前节点指针指向上一个节点
         两个游标同时往后移动
         结束标准: 当要操作的节点为None时,结束! 此时pre代表的是新链表的头节点
  """
  class Node:
      def __init__(self, value):
          self.value = value
          self.next = None
  
  class Solution:
      def reverse_link_list(self, head):
          # 1、空链表情况
          if head == None:
              return
          # 2、非空链表情况
          pre = None
          cur = head
          while cur:
              # 记录下一个要操作反转的节点
              next_node = cur.next
              # 反转节点cur,并移动两个游标
              cur.next = pre
              pre = cur
              cur = next_node
  
          return pre.value
  
  if __name__ == '__main__':
      s = Solution()
      # 1、空链表情况
      head = None
      print(s.reverse_link_list(head))
      # 2、只有1个节点情况
      head = Node(100)
      print(s.reverse_link_list(head))
      # 3、有多个节点情况
      head = Node(100)
      head.next = Node(200)
      head.next.next = Node(300)
      print(s.reverse_link_list(head))
  ```

## **今日作业**

```python
【1】手写单链表
【2】输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则
```

