"""
设计LRU缓存结构，该结构在构造时确定大小，假设大小为K，并有如下两个功能
set(key, value)：将记录(key, value)插入该结构
get(key)：返回key对应的value值
[要求]
set和get方法的时间复杂度为O(1)
某个key的set或get操作一旦发生，认为这个key的记录成了最常使用的。
当缓存的大小超过K时，移除最不经常使用的记录，即set或get最久远的。
若opt=1，接下来两个整数x, y，表示set(x, y)
若opt=2，接下来一个整数x，表示get(x)，若x未出现过或已被移除，则返回-1
对于每个操作2，输出一个答案
"""
# LRU缓存，Least Recently Used 最不常使用
"""输入
[[1,1,1],[1,2,2],[1,3,2],[2,1],[1,4,4],[2,2]],3
返回值
复制
[1,-1]
说明
第一次操作后：最常使用的记录为("1", 1)
第二次操作后：最常使用的记录为("2", 2)，("1", 1)变为最不常用的
第三次操作后：最常使用的记录为("3", 2)，("1", 1)还是最不常用的
第四次操作后：最常用的记录为("1", 1)，("2", 2)变为最不常用的
第五次操作后：大小超过了3，所以移除此时最不常使用的记录("2", 2)，加入记录("4", 4)，并且为最常使用的记录，然后("3", 2)变为最不常使用的记录"""


#
class Solution:
    res_dict = {}
    frequency_list = []
    res_list = []
    def LRU(self, operators, k):
        # write code here

        for operation in operators:
            if len(operation) == 3:
                if len(self.frequency_list) < k:
                    self.frequency_list.append(operation[1])
                    self.res_dict[operation[1]] = operation[-1]
                else:
                    key = self.frequency_list.pop(0)
                    del self.res_dict[key]
                    self.frequency_list.append(operation[1])
                    self.res_dict[operation[1]] = operation[-1]
            else:
                res = self.res_dict.get(operation[-1])
                if res:
                    self.res_list.append(self.res_dict[operation[-1]])
                    self.frequency_list.remove(operation[-1])
                    self.frequency_list.append(operation[-1])
                else:
                    self.res_list.append(-1)
        return self.res_list





s = Solution()
res = s.LRU([[1, 1, 1], [1, 2, 2], [1, 3, 2], [2, 1], [1, 4, 4], [2, 2]], 3)
print(res)


# class Solution:
#     # 字典存储键值对；列表实现值常用性更新
#     dict_lru = {}
#     list_lru = []
#
#     def set(self, key, val, k):
#         self.dict_lru[key] = val
#         self.list_lru.append(key)
#         if len(self.list_lru) > k:
#             del self.dict_lru[self.list_lru[0]]
#             del self.list_lru[0]
#
#     def get(self, key):
#         if key in self.dict_lru:
#             self.list_lru.remove(key)
#             self.list_lru.append(key)
#             return self.dict_lru[key]
#         return -1
#
#     def LRU(self, operators, k):
#         ret = []
#         SET = 1
#         GET = 2
#
#         for items in operators:
#             if items[0] == SET:
#                 self.set(str(items[1]), items[2], k)
#
#             elif items[0] == GET:
#                 ret.append(self.get(str(items[1])))
#
#         return ret