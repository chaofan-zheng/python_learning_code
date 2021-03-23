# 自己构造数据, 实现线性回归
import numpy as np
import sklearn.linear_model as lm
import sklearn.metrics as sm
import matplotlib.pyplot as mp
import random

x = np.array([[1], [2], [3], [4], [5],
              [6], [7], [8], [9], [10]])
y = 2.0 * x # 计算 y = 2x
noise = np.random.rand(len(y), 1) * 3 # 产生0~3之间噪声
y += noise # 每个y值加上随机噪声
print(y)

# 使用模型三板斧
model = lm.LinearRegression() # 定义模型
model.fit(x, y) # 训练
pred_y = model.predict(x) # 使用模型预测

print("coef_:", model.coef_)  # 系数
print("intercept_:", model.intercept_)  # 截距

# 可视化回归曲线
mp.figure('Linear Regression')
mp.title('Linear Regression')
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')

# 绘制样本点
mp.scatter(x, y, c='blue', alpha=0.8,
           s=60, label='Sample')

# 绘制拟合直线
mp.plot(x,  # x坐标数据
        pred_y,  # y坐标数据
        c='orangered', label='Regression')

mp.legend()
mp.show()