# 05_one_hot_demo.py
# 独热编码: 将特征转换为一个1和一串0表示的序列
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([[1, 3, 2],
                        [7, 5, 4],
                        [1, 8, 6],
                        [7, 3, 9]])
# 定义独热编码器
encoder = sp.OneHotEncoder(
    sparse=False, # 是否采用稀疏格式
    dtype="int32", # 元素类型
    categories="auto") # 自动编码
oh_samples = encoder.fit_transform(raw_samples)#编码
print(oh_samples)

# 逆向转换
print(encoder.inverse_transform(oh_samples))
