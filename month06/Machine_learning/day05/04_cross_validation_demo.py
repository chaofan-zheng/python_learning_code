# 04_cross_validation_demo.py
# 交叉验证示例
# 交叉验证: 将样本划分成K个子集(每个子集称为一个折叠)
#          每次训练采用其中一个折叠作为测试集
#          其它折叠作为训练集, 主要用于数据较少情况下
#          的模型测试与评估
import numpy as np
import sklearn.naive_bayes as nb
import matplotlib.pyplot as mp
import sklearn.metrics as sm
import sklearn.model_selection as ms

x, y = [], []  # 输入, 输出

# 读取样本
with open("../data/multiple1.txt", "r") as f:
    for line in f.readlines():
        data = [float(substr)
                for substr in line.split(",")]
        x.append(data[:-1])
        y.append(data[-1])
x = np.array(x)
y = np.array(y)

model = nb.GaussianNB()

# 直接交给交叉验证函数
precision = ms.cross_val_score(
    model, # 模型
    x, y, # 数据集
    cv=5, # 折叠数量
    scoring="precision_weighted") # 查准率
print("precesion: \n", precision)

recall = ms.cross_val_score(
    model, # 模型
    x, y, # 数据集
    cv=5, # 折叠数量
    scoring="recall_weighted") # 召回率
print("recall: \n", recall)

f1 = ms.cross_val_score(
    model, # 模型
    x, y, # 数据集
    cv=5, # 折叠数量
    scoring="f1_weighted") # f1
print("f1: \n", f1)