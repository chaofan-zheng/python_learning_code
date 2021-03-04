# import re
#
#
# class Solution:
#     res_dict = {}
#
#     def solution(self, input_str):
#         # 把输入处理成行
#         lines = input_str.split('\n')
#         for line in lines:
#             if self.is_full(Solution.res_dict):
#                 break
#             # 得到文件名和行数
#             path = line.split(' ')[0]
#             row = line.split(' ')[1]
#             filename = re.findall('.*\\\(.*?)$', path)[0]
#             # 结果字典
#             key = filename + ' ' + row
#             count = Solution.res_dict.get(key)
#             if count:
#                 Solution.res_dict[key] += 1
#             else:
#                 Solution.res_dict[key] = 1
#             # 输出结果
#         for key, value in Solution.res_dict.items():
#             yield key + ' ' + str(value)
#
#     def is_full(self, res_dict):
#         """判断结果字典是否已经为8"""
#         count = 0
#         for key in res_dict:
#             count += 1
#         if count < 8:
#             return False
#         else:
#             return True
#
#
# if __name__ == '__main__':
#     s = Solution()
#     input_str = r"""e:\1\aa3.txt 3
# e:\3\aa1.txt 2"""
#     res = s.solution(input_str)
#     for item in res:
#         print(item)
import re



def print_res(res_dict):
    # 只输出前八个
    for k, v in res_dict.items():
        print(k, v)


count = 0
res_dict = {}
while True:
    try:
        str = input().split()
        path, row = str[0], str[1]
        filename = re.findall('\\\?([^\\\]*)$', path)[0]
        key = filename + ' ' + row
        if res_dict.get(key):
            res_dict[key] += 1
        else:
            res_dict[key] = 1
        print_res(res_dict)
    except:
        break
#
# 链接：https://www.nowcoder.com/questionTerminal/67df1d7889cf4c529576383c2e647c48
# 来源：牛客网
#
# import sys
# import collections
# lst = []
# dct = collections.OrderedDict()
# #循环读取输入，将输入的出现次数计入有序字典里面
# for line in sys.stdin:
#     ele = line.split('\\')[-1].strip('\n')
#     if ele not in lst:
#         lst.append(ele)
#     if ele in dct:
#         dct[ele] = dct[ele] + 1
#     else:
#         dct[ele] = 1
# #对字典按照出现次数(value)排序
# lstTuple = sorted(dct.items(), key = lambda d:d[1], reverse = True)
# #输出不超过8行的结果
# count = 0
# for key in lstTuple:
#     if count > 7:
#         break
#     count = count + 1
#     #文件名取后16位
#     if len(key[0].split(' ')[0]) > 16:
#         print key[0].split(' ')[0][-16:], key[0].split(' ')[1], key[1]
#     else:
#         print key[0].split(' ')[0], key[0].split(' ')[1], key[1]