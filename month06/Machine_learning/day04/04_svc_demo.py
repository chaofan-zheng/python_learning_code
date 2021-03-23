# 04_svc_demo.py
# 支持向量机分类示例
import numpy as np
import sklearn.svm as ms
import sklearn.metrics as sm
import matplotlib.pyplot as mp

x, y = [], [] # 输入, 输出
with open("../data/multiple2.txt", "r") as f:
    for line in f.readlines():
        data = [float(substr)
                for substr in line.split(",")]
        x.append(data[:-1]) # 输入部分
        y.append(data[-1]) # 输出部分
x = np.array(x)
y = np.array(y)

# 线性核函数
# model = ms.SVC(kernel="linear")

#多项式核函数
# model = ms.SVC(kernel="poly", degree=3)#最高次项为3

# 径向基核函数
model = ms.SVC(kernel="rbf",# 径向基核函数
               gamma=0.01, # 标准差
               C=200) # 概率强度

model.fit(x, y) # 训练

# 计算图形边界
l, r, h = x[:, 0].min() - 1, x[:, 0].max() + 1, 0.01
b, t, v = x[:, 1].min() - 1, x[:, 1].max() + 1, 0.01

# 生成网格矩阵
grid_x = np.meshgrid(np.arange(l, r, h),
                     np.arange(b, t, v))
flat_x = np.c_[grid_x[0].ravel(),grid_x[1].ravel()]  # 合并
flat_y = model.predict(flat_x)  # 根据网格矩阵预测分类
grid_y = flat_y.reshape(grid_x[0].shape)  # 还原形状

mp.figure("SVM Classifier", facecolor="lightgray")
mp.title("SVM Classifier", fontsize=14)

mp.xlabel("x", fontsize=14)
mp.ylabel("y", fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap="gray")

C0, C1 = (y == 0), (y == 1)
mp.scatter(x[C0][:, 0], x[C0][:, 1], c="orangered", s=80)
mp.scatter(x[C1][:, 0], x[C1][:, 1], c="limegreen", s=80)
mp.show()