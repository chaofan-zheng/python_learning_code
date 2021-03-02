import numpy as np
# 创建一维数组
# arr1=np.array([1,2,3,4],ndmin=2)
arr1=np.array([1,2,3,4])
print('一维数组',arr1)
# 创建二维数组
arr2=np.array([[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12]],dtype='uint8')
print('二维数组 \n',arr2)
# 查看数组维度
print(arr2.ndim)
# 查看数组形状
print(arr2.shape)
# 查看数组元素个数
print(arr2.size)
# 查看数组类型
print(arr2.dtype)
# 查看数组每个元素大小
print(arr2.itemsize)
# 修改数组形状
arr2.shape=4,3
print(arr2)