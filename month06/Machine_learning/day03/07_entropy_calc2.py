# 07_entropy_calc2.py
"""
一批样本包含A和B两个类别，计算：
当A类别比率依次占0%, 10%, 20%, ..., 100%时,
这批样本信息熵值，并以占比作为x轴数值、
信息熵作为y轴数值绘制图像.
"""
import math
import numpy as np
import matplotlib.pyplot as mp

# 定义A,B类别各自所占比例
arr = np.array([[0.00001, 1.0],
                [0.1, 0.9],
                [0.2, 0.8],
                [0.3, 0.7],
                [0.4, 0.6],
                [0.5, 0.5],
                [0.6, 0.4],
                [0.7, 0.3],
                [0.8, 0.2],
                [0.9, 0.1],
                [1.0, 0.00001]])
result = [] # 存放计算的信息熵
for a in arr:
    v1 = -(a[0] * math.log(a[0]))
    v2 = -(a[1] * math.log(a[1]))
    result.append(v1 + v2)

# 绘图
mp.figure("Entropy")
mp.title("Entropy")
mp.xlabel("x", fontsize=14)
mp.ylabel("entropy", fontsize=14)
mp.grid(linestyle=":")
x = np.arange(0, 1.1, 0.1) # 产生x坐标值
mp.plot(x, result, c="red", label="entropy")
mp.legend()
mp.show()

