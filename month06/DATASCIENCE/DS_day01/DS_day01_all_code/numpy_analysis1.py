import numpy as np
# 创建一维数组
# arr=np.arange(10)
# print(arr)
# # print(arr.ndim)
# # print(arr.shape)
# # 访问单个值
# print(arr[3])
# print(arr[-1])
# # 访问范围 (起始值0，结束值，步长1)
# print(arr[2:6:2])
# print(arr[7:1:-1])
# 二维数组的创建
arr2=np.array([[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12]])
print(arr2)
# 得到前两行,前两列 行列都有要求
print(arr2[0:2,0:2])
# 按照行进行选择
print(arr2[0:2])
# 按照列进行选择
print(arr2[:,1:3])
# 得到某一个值
print(arr2[1][2])
print(arr2[1,2])