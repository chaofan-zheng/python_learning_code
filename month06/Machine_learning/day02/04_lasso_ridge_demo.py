# Lasso回归和岭回归示例
# Lasso回归: 标准线性回归损失函数上添加了L1范数
# 岭回归: 标准线性回归损失函数上添加了L2范数
import numpy as np
import sklearn.linear_model as lm
import sklearn.metrics as sm
import matplotlib.pyplot as mp

x, y = [], []  # 输入,输出
with open("../data/abnormal.txt", "rt") as f:
    for line in f.readlines():
        data = [float(substr)
                for substr in line.split(",")]
        x.append(data[:-1])  # 输入
        y.append(data[-1])  # 输出
# 列表转数组
x = np.array(x)
y = np.array(y)

# 标准线性回归
model = lm.LinearRegression()
model.fit(x, y)
pred_y = model.predict(x)  # 预测

# 岭回归
model_2 = lm.Ridge(alpha=200,  # 正则强度
                   max_iter=1000)  # 最大迭代次数
model_2.fit(x, y)
pred_y2 = model_2.predict(x)

# lasso回归
model_3 = lm.Lasso(alpha=0.5, max_iter=1000)
model_3.fit(x, y)
pred_y3 = model_3.predict(x)

# 可视化回归曲线
mp.figure('Linear & Ridge & Lasso', facecolor='lightgray')
mp.title('Linear & Ridge & Lasso', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x, y, c='dodgerblue', alpha=0.8, s=60, label='Sample')
sorted_idx = x.T[0].argsort()

mp.plot(x[sorted_idx], pred_y[sorted_idx],
        c='orangered', label='Linear')  # 线性回归
mp.plot(x[sorted_idx], pred_y2[sorted_idx],
        c='limegreen', label='Ridge')  # 岭回归
mp.plot(x[sorted_idx], pred_y3[sorted_idx],
        c='blue', label='Lasso')  # Lasso回归

mp.legend()
mp.show()
