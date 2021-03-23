# 01_lr_demo1.py
# 自己编写代码,实现梯度下降和线性回归
import numpy as np
import matplotlib.pyplot as mp
import sklearn.preprocessing as sp
from mpl_toolkits.mplot3d import axes3d

# 数据集
train_x = np.array([0.5, 0.6, 0.8, 1.1, 1.4])
train_y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])

n_epochs = 1000 # 迭代次数
lrate = 0.01 # 学习率(控制收敛步幅)
epochs = [] # 记录迭代次数
losses = [] # 记录损失函数值

w0, w1 = [1], [1] # 线性模型参数初始值

for i in range(1, n_epochs + 1):  # 循环执行梯度下降
    epochs.append(i)
    # 计算y = w0 + w1*x
    y = w0[-1] + w1[-1] * train_x
    # 计算损失函数(均方差)
    loss = (((train_y - y)**2).sum()) / 2
    losses.append(loss) # 记录到列表中
    print("%d: w0=%f, w1=%f, loss=%f" %
          (i, w0[-1], w1[-1], loss))

    # 执行梯度下降
    d0 = -(train_y - y).sum() # w0梯度
    d1 = -(train_x * (train_y - y)).sum()# w1梯度

    w0.append(w0[-1] - (d0 * lrate))
    w1.append(w1[-1] - (d1 * lrate))

# 可视化
## 先绘制损失函数收敛过程
w0 = np.array(w0[:-1]) # 去掉多余的一个值(因为有一个初始值)
w1 = np.array(w1[:-1]) # 去掉多余的一个值(因为有一个初始值)

mp.figure("Losses") # 创建窗体
mp.title("Losses") # 图形名称
mp.ylabel("loss")  # y轴显示的文字
mp.grid(linestyle=":")  # 网格线:虚线
mp.plot(epochs, losses, # x,y坐标的数据
        c="blue", label="loss")#颜色,标签
mp.legend() # 图例
mp.tight_layout() # 紧凑格式

## 绘制样本散点图, 回归出的直线
pred_y = w0[-1] + w1[-1]  * train_x # 根据模型算y
mp.figure("Linear")
mp.title("Linear")
mp.xlabel("x", fontsize=14)  # x轴显示 的 文字和大小
mp.ylabel("y", fontsize=14)
mp.grid(linestyle=":")
## 样本散点图
mp.scatter(train_x, train_y, c="blue", label="sample")
## 绘制回归出的直线
mp.plot(train_x, pred_y, c="red", label="Linear")
mp.legend()

# 显示梯度下降过程(复制粘贴即可，不需要编写)
# 计算损失函数曲面上的点 loss = f(w0, w1)
arr1 = np.linspace(0, 10, 500)  # 0~9间产生500个元素的均匀列表
arr2 = np.linspace(0, 3.5, 500)  # 0~3.5间产生500个元素的均匀列表

grid_w0, grid_w1 = np.meshgrid(arr1, arr2)  # 产生二维矩阵

flat_w0, flat_w1 = grid_w0.ravel(), grid_w1.ravel()  # 二维矩阵扁平化
loss_metrix = train_y.reshape(-1, 1)  # 生成误差矩阵（-1,1）表示自动计算维度
outer = np.outer(train_x, flat_w1)  # 求外积（train_x和flat_w1元素两两相乘的新矩阵）
# 计算损失：((w0 + w1*x - y)**2)/2
flat_loss = (((flat_w0 + outer - loss_metrix) ** 2).sum(axis=0)) / 2
grid_loss = flat_loss.reshape(grid_w0.shape)

mp.figure('Loss Function')
ax = mp.gca(projection='3d')
mp.title('Loss Function', fontsize=14)
ax.set_xlabel('w0', fontsize=14)
ax.set_ylabel('w1', fontsize=14)
ax.set_zlabel('loss', fontsize=14)
ax.plot_surface(grid_w0, grid_w1, grid_loss, rstride=10, cstride=10, cmap='jet')
ax.plot(w0, w1, losses, 'o-', c='orangered', label='BGD', zorder=5)
mp.legend(loc='lower left')

mp.show()





