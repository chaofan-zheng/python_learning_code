# 03_entropy_calc.py
# 计算一批样本,类别为1~10情况下信息熵的变化情况
import math
import numpy as np
import matplotlib.pyplot as mp

class_num = 10 # 类别最大数量

# 根据传入类别数量计算信息熵
def entropy_calc(n):
    p = 1.0 / n # 计算每个类别概率,都是1/n
    entropy_value = 0.0

    for i in range(n):
        p_i = p * math.log(p)
        entropy_value += p_i # 累加

    return -entropy_value

# 循环计算1~10类别信息熵
entropies = []
for i in range(1, class_num + 1):
    ent = entropy_calc(i) # 计算信息熵
    entropies.append(ent)

# 绘图
mp.figure("Entropy")
mp.title("Entropy")
mp.xlabel("Class Num", fontsize=14)
mp.ylabel("Entropy", fontsize=14)
mp.grid(linestyle=":")
x = np.arange(1, 11, 1) # 1~11之间产生均匀数组
mp.plot(x, entropies, c="red", label="entropy")
mp.legend()
mp.show()
