# 05_validation_curve_demo.py
# 验证曲线: 验证不同的参数对模型的影响
import numpy as np
import sklearn.preprocessing as sp
import sklearn.ensemble as se
import sklearn.model_selection as ms
import matplotlib.pyplot as mp

data = []
with open("../data/car.txt", "r") as f:
    for line in f.readlines():
        data.append(line.replace("\n", "").split(","))

data = np.array(data).T  # 转置
encoders, train_x = [], []

# 对样本数据进行标签编码
for row in range(len(data)):
    encoder = sp.LabelEncoder()  # 创建标签编码器
    encoders.append(encoder)
    if row < len(data) - 1:  # 不是最后一行，为样本特征
        lbl_code = encoder.fit_transform(data[row])  # 编码
        train_x.append(lbl_code)
    else:  # 最后一行，为样本输出
        train_y = encoder.fit_transform(data[row])

train_x = np.array(train_x).T  # 转置回来，变为编码后的矩阵

#  定义随机森林模型(n_estimators不设置)
model = se.RandomForestClassifier(
    n_estimators=150, # 树的棵树
    random_state=7) # 随机种子
max_depth = np.arange(5, 11, 1)
print(max_depth)

# 通过验证曲线函数,验证不同参数n_estimators下准确率
train_scores, test_scores = ms.validation_curve(
    model, # 待验证的模型(随机森林)
    train_x, train_y, # 全体样本
    "max_depth", # 待验证参数
    max_depth, # 待验证参数的可选则范围
    cv=5) # 折叠数量
# 求均值
train_scores = train_scores.mean(axis=1)#行方向
test_scores = test_scores.mean(axis=1)
print(train_scores)
print(test_scores)

# 可视化
mp.figure("Validation Curve")
mp.title("Validation Curve")
mp.xlabel("max_depth", fontsize=14)
mp.ylabel("F1 Score", fontsize=14)
mp.grid(linestyle=":")
mp.plot(max_depth, test_scores,
        "o-", # 线条风格
        c="blue", label="Test") # 颜色,文字
mp.plot(max_depth, train_scores,
        "o-", # 线条风格
        c="red", label="Train") # 颜色,文字
mp.legend()
mp.show()
