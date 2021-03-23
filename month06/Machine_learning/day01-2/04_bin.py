# 04_bin.py
# 二值化: 将特征值转换为0或1两个值中的一个
import numpy as np
import sklearn.preprocessing as sp

raw_samples = np.array([[65.5, 89.0, 73.0],
                        [55.0, 99.0, 98.5],
                        [45.0, 22.5, 60.0]])
bin_samples = raw_samples.copy()  # 复制数组

mask1 = bin_samples < 60 # 挑选出小于60的
mask2 = bin_samples >= 60 # 挑选出小于等于60的
# 通过掩码运算进行二值化处理
bin_samples[mask1] = 0 # mask1中为True的设置0
bin_samples[mask2] = 1 # mask2中为True的设置1
print(bin_samples)

print("================")
# 利用sklearn提供的API实现
bin = sp.Binarizer(threshold=59)
bin_samples = bin.transform(raw_samples)#二值转换
print(bin_samples)