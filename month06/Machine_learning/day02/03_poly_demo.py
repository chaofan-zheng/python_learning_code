# 多项式回归示例
# 多项式: 跟线性模型比较,多项式引入了高次项
import numpy as np
import sklearn.linear_model as lm
import sklearn.metrics as sm
import matplotlib.pyplot as mp
import sklearn.pipeline as pl # 管线
import sklearn.preprocessing as sp

# 从样本文件读取数据
train_x, train_y = [], [] # 输入, 输出
with open("../data/poly_sample.txt", "rt") as f:
    for line in f.readlines():
        # 拆分每行,并转换为浮点数
        data = [float(substr)
                for substr in line.split(",")]
        train_x.append(data[:-1])#切片(结果是二维)
        train_y.append(data[-1])#索引(结果是一维)
# 列表转数组
train_x = np.array(train_x)
train_y = np.array(train_y)
# print(train_x.shape)
# print(train_y.shape)

# 定义模型
## 多项式模型实现分为两步: 多项式扩展, 线性回归求解
model = pl.make_pipeline(
    sp.PolynomialFeatures(20), # 多项式扩展,最高次项3
    lm.LinearRegression()) # 线性回归模型
model.fit(train_x, train_y) # 训练
pred_train_y = model.predict(train_x) # 预测

# 打印R2值
r2 = sm.r2_score(train_y, pred_train_y)
print("r2:", r2)

# 可视化
test_x = np.linspace(train_x.min(),
                     train_x.max(),
                     100)  # 在样本x坐标范围内产生100个点
# 将test_x变成二维输入模型执行预测
pre_test_y = model.predict(test_x.reshape(-1, 1))

mp.figure("Polynomial")
mp.title("Polynomial")
mp.xlabel("x", fontsize=14)
mp.ylabel("y", fontsize=14)
mp.grid(linestyle=":")

mp.scatter(train_x, train_y, c="blue", label="sample")
mp.plot(test_x, pre_test_y, c="red", label="poly")

mp.legend()
mp.show()




