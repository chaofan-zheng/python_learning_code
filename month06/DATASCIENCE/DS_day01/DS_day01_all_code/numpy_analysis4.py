import numpy as np
# 排序:一维数组
data=np.array([2,5,6,9,1,8,7])
# data.sort()
# 从大到小排序
# data_sort=np.abs(np.sort(-data))
# print(data_sort)
# # print(data)
# # 间接排序 得到索引
# data_arg=data.argsort()
# print(data_arg)
# 排序:二维数组
# data2=np.array([[1,5,2,7],
#                 [4,8,3,6],
#                 [7,8,11,10]])
# print(data2)
# 纵向排序
# data2.sort(axis=0)
# print(data2)
# 横向排序
# data2.sort(axis=1)
# print(data2)

# 使用numpy进行统计分析
arr=np.arange(20).reshape(4,5)
print(arr)
# 求整个数组的总和
# print(arr.sum())
# # 计算每一行数据的和
# print(arr.sum(axis=1))
# # 计算每一列数据的和
# print(arr.sum(axis=0))
# # 求整组数据的标准差
# print(np.std(arr))
# # 每一行的标准差
# print(np.std(arr,axis=1))
# # 每一列的标准差
# print(np.std(arr,axis=0))
# 计算数据的累积和
# print(np.cumsum(arr))
# # 按列计算数据累积和
# print(np.cumsum(arr,axis=0))
# 计算数据的累积积
print(np.cumprod(arr))
# 按行计算
print(np.cumprod(arr,axis=1))
# 得到最大元素的索引位置
print(np.argmax(arr))
print(np.argmax(arr,axis=0))
# 得到最小元素的索引位置
print(np.argmin(arr))
print(np.argmin(arr,axis=1))




