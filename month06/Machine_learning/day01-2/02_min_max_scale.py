# 02_min_max_scale.py
# 范围缩放: 将每列最大值转换为1, 最小值转换为0
import numpy as np
import sklearn.preprocessing as sp

# 样本
raw_samples = np.array([
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0]]).astype("float64")
mms_samples = raw_samples.copy()  # 拷贝数组

for col in mms_samples.T:  # 遍历每列
    col_min = col.min()  # 求每列最小值
    col_max = col.max()  # 求每列最大值
    col -= col_min  # 减最小值
    col /= (col_max - col_min)  # 除max-min
print(mms_samples)

print("===============")
# 利用sklearn提供的API实现
#  feature_range是设置最大/最小值范围
mms = sp.MinMaxScaler(feature_range=(0,1))
mms_samples = mms.fit_transform(raw_samples)
print(mms_samples)
