# 03_precision_recall_demo.py
# 计算查准率, 召回率, F1得分示例
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

# 划分训练集/测试集
train_x, test_x, train_y, test_y = ms.train_test_split(
    x, y,  # 全体样本输入/输出
    test_size=0.25,  # 测试集占25%
    random_state=7)  # 随机种子,产生随机值使用

# 定义模型
model = nb.GaussianNB()  # 高斯朴素贝叶斯分类器
model.fit(train_x, train_y)  # 使用训练集训练
pred_test_y = model.predict(test_x)  # 使用测试集预测

# 打印相关指标
precision = sm.precision_score(  # 查准率
    test_y,  # 真实类别
    pred_test_y,  # 预测类别
    average="macro")  # 计算平均值不考虑样本权重
print("查准率:", precision)

recall = sm.recall_score(  # 召回率
    test_y,  # 真实类别
    pred_test_y,  # 预测类别
    average="macro")  # 计算平均值不考虑样本权重
print("召回率:", recall)

f1 = sm.f1_score(test_y, pred_test_y, average="macro")
print("F1:", f1)

# 打印混淆矩阵
print("\n 混淆矩阵: \n")
print(sm.confusion_matrix(test_y, pred_test_y))
