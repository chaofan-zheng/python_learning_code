# 01_scale.py
# 均值移除(标准化)预处理
# 均值移除: 将每列数值转换为均值为0
#          标准差为1的分布
import numpy as np
import sklearn.preprocessing as sp

# 定义样本
raw_samples = np.array([[3.0, -1.0, 2.0],
                        [0.0, 4.0, 3.0],
                        [1.0, -4.0, 2.0]])
# 复制样本
std_samples = raw_samples.copy()
for col in std_samples.T: # 遍历转置矩阵(遍历原矩阵列)
    col_mean = col.mean() # 求每列均值
    col_std = col.std() # 求每列标准差
    col -= col_mean # 减均值
    col /= col_std # 除标准差
print(std_samples)
print(std_samples.mean(axis=0)) # 计算每列均值并打印
print(std_samples.std(axis=0)) # 计算每列标准差并打印

print("==============")

# 利用sklearn提供的API实现
std_samples = sp.scale(raw_samples) # 标准化
print(std_samples)
print(std_samples.mean(axis=0)) # 计算每列均值并打印
print(std_samples.std(axis=0)) # 计算每列标准差并打印
