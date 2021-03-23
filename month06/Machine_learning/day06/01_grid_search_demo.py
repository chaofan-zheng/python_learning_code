# 01_grid_search_demo.py
# 网格搜索示例
""" 网格搜索
 1) 寻找超参数组合的一种方式
 2) 利用穷举法, 将可选的参数组合, 选择最优者
 3) 能够简化对参数选择过程
"""
import numpy as np
import sklearn.model_selection as ms
import sklearn.svm as svm
import sklearn.metrics as sm
import matplotlib.pyplot as mp

# 读取数据
x, y = [], []
with open("../data/multiple2.txt", "r") as f:
    for line in f.readlines():
        data = [float(substr)
                for substr in line.split(",")]
        x.append(data[:-1])
        y.append(data[-1])
x = np.array(x)
y = np.array(y)

# 定义需要挑选的参数
params = [
    {
        "kernel": ["linear"],
        "C": [1, 10, 100, 1000]
    },
    {
        "kernel": ["poly"],
        "C": [1],
        "degree": [2, 3]
    },
    {
        "kernel": ["rbf"],
        "C": [1, 10, 100, 1000],
        "gamma": [1, 0.1, 0.01, 0.001]
    }
]

model = ms.GridSearchCV(svm.SVC(),  # 原模型
                        params,  # 待验证的参数
                        cv=5)  # 折叠数量
model.fit(x, y) # 训练

print("最好成绩:", model.best_score_)
print("最优组合:", model.best_params_)


l, r, h = x[:, 0].min() - 1, x[:, 0].max() + 1, 0.005
b, t, v = x[:, 1].min() - 1, x[:, 1].max() + 1, 0.005
grid_x = np.meshgrid(np.arange(l, r, h), np.arange(b, t, v))
flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]
flat_y = model.predict(flat_x)
grid_y = flat_y.reshape(grid_x[0].shape)

mp.figure("SVM RBF Classifier", facecolor="lightgray")
mp.title("SVM RBF Classifier", fontsize=14)
mp.xlabel("x", fontsize=14)
mp.ylabel("y", fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap="gray")

C0, C1 = (y == 0), (y == 1)
mp.scatter(x[C0][:, 0], x[C0][:, 1], c="orangered", s=80)
mp.scatter(x[C1][:, 0], x[C1][:, 1], c="limegreen", s=80)

mp.show()