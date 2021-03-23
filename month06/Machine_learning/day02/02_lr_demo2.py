# 02_lr_demo2.py
# sklearn库线性回归模型示例
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp

# 数据集(输入要求二维的)
train_x = np.array([[0.5], [0.6], [0.8], [1.1], [1.4]])
train_y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])

# 使用模型三板斧
model = lm.LinearRegression() # 定义模型
model.fit(train_x, train_y) # 训练
pred_y = model.predict(train_x) # 使用模型预测

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
mp.scatter(train_x, train_y, c='blue', alpha=0.8, s=60, label='Sample')

# 绘制拟合直线
mp.plot(train_x,  # x坐标数据
        pred_y,  # y坐标数据
        c='orangered', label='Regression')

mp.legend()
mp.show()