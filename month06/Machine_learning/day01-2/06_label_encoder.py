# 06_label_encoder.py
# 标签编码: 将字符串转换为数字, 方便模型计算
import numpy as np
import sklearn.preprocessing as sp

# 定义样本
raw_samples = np.array(
    ["audi", "ford", "audi", "bmw", "ford", "bmw"])
# 定义标签编码器
encoder = sp.LabelEncoder()
lb_samples = encoder.fit_transform(raw_samples)
print(lb_samples)
# 逆向转换
print(encoder.inverse_transform(lb_samples))