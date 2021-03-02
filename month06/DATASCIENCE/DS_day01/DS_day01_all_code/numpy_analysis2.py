import numpy as np
# 使用numpy进行文件写入
# 创建一个数组并保存
arr=np.arange(100).reshape(10,10)
print(arr)
# 单个文件保存 save npy
np.save(file='save_arr',arr=arr)
# 创建两个数组并保存
arr1=np.array([1,2,3,4])
arr2=np.arange(12).reshape(3,4)
# 多个文件保存 savez npz
np.savez('savez_arr',arr1,arr2)




