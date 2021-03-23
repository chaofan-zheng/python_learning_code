# 03_normalize.py
# 归一化: 将每行每个特征转换为百分比
#        从而更好反映出此消彼长趋势
import numpy as np
import sklearn.preprocessing as sp

# 样本数据
raw_samples = np.array([[10.0, 20.0, 5.0],
                        [8.0, 10.0, 1.0]])
nor_samples = raw_samples.copy() # 拷贝

for row in nor_samples:
    row /= abs(row).sum() # 先求绝对值之和,再除
print(nor_samples)

print("==============")

# 调用sklearn提供的API实现
# l1: l1范数, 除以所有元素绝对值之和
# l2: l2范数, 除以所有元素平方和再开方
nor_samples = sp.normalize(raw_samples,
                           norm="l1")
print(nor_samples)
