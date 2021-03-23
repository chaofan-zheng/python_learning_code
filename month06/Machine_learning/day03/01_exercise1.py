# 02_lr_demo2.py
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp

# 数据集(输入要求二维的)
train_x = np.array([[230.1], [44.5], [17.2], [151.5],
                    [180.0], [57.5], [120.2], [8.6]])
train_y = np.array(
    [22.1, 10.4, 9.3, 18.5, 12.9, 11.8, 13.2, 4.8])

# 使用模型三板斧
model = lm.LinearRegression()  # 定义模型
model.fit(train_x, train_y)  # 训练
#pred_y = model.predict(train_x)  # 使用模型预测

# 待预测数据
test_x = np.array([[10],[300],[400],[500]])
pred_y = model.predict(test_x)

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
mp.plot(test_x,  # x坐标数据
        pred_y,  # y坐标数据
        c='orangered', label='Regression')

mp.legend()
mp.show()
