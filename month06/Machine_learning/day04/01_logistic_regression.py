# 01_logistic_regression.py
# 逻辑回归示例
# 逻辑回归: 二分类问题, 利用回归模型先预测一个连续值
#         再使用逻辑函数(sigmoid)进行离散化
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp

x = np.array([[3, 1], [2, 5], [1, 8], [6, 4],
              [5, 2], [3, 5], [4, 7], [4, -1]])
y = np.array([0, 1, 1, 0, 0, 1, 1, 0])

model = lm.LogisticRegression()  # 逻辑回归器
model.fit(x, y)  # 训练
test_x = np.array([[3, 9], [6, 1]])  # 测试数据
test_y = model.predict(test_x)  # 预测
print(test_y)  # 打印预测结果

# 计算边界
left = x[:, 0].min() - 1  # 计算左边界
right = x[:, 0].max() + 1  # 计算右边界
buttom = x[:, 1].min() - 1  # 下边界
top = x[:, 1].max() + 1  # 上边界

# 在边界指定矩形区域内产生网格矩阵
grid_x, grid_y = np.meshgrid(
    np.arange(left, right, 0.05),  # x方向数组
    np.arange(buttom, top, 0.05))  # y方向数组
print(grid_x.shape)
print(grid_y.shape)

# 合并x,y坐标
mesh_x = np.column_stack(
    (grid_x.ravel(), grid_y.ravel()))
print(mesh_x.shape)

# 将产生的坐标点输入模型预测
mesh_z = model.predict(mesh_x)
mesh_z = mesh_z.reshape(grid_x.shape)#还原成二维

# 可视化
mp.figure("Logistic Regression")
mp.title("Logistic Regression")
mp.xlabel("x", fontsize=14)
mp.ylabel("y", fontsize=14)
# 绘制背景
mp.pcolormesh(grid_x, grid_y, # 网格矩阵x,y坐标
              mesh_z, # 每个点对应的类别
              cmap="gray") # 根据不同类别涂成不同深浅灰色
# 绘制样本散点图
mp.scatter(x[:, 0], x[:, 1], # 样本的x,y坐标
           c=y, # 样本真实类别
           cmap="brg")# 根据不同类别分配不同色彩
# 绘制测试样本
mp.scatter(test_x[:, 0], test_x[:, 1],
           c="red", marker='s') # 颜色, 形状(正方形)
mp.legend()
mp.show()
