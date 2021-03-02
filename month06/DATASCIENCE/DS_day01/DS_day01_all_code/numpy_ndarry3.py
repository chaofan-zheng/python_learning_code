import numpy as np
# 使用numpy读取npy文件
load_data=np.load('save_arr.npy')
print(load_data)
# 使用numpy读取npz文件
load_data2=np.load('savez_arr.npz')
print(load_data2)
# 查看数组名称
print(load_data2.files)
# 读取第一个数组
print(load_data2['arr_0'])
# 读取第二个数组
print(load_data2['arr_1'])