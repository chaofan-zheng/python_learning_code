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
    max_depth=8, # 最大深度
    random_state=7) # 随机种子
n_estimators = np.arange(50, 550, 50) # 产生50~500列表
print(n_estimators)

# 通过验证曲线函数,验证不同参数n_estimators下准确率
train_scores, test_scores = ms.validation_curve(
    model, # 待验证的模型(随机森林)
    train_x, train_y, # 全体样本
    "n_estimators", # 待验证参数
    n_estimators, # 待验证参数的可选则范围
    cv=5) # 折叠数量
# 求均值
train_scores = train_scores.mean(axis=1)#行方向
test_scores = test_scores.mean(axis=1)
print(train_scores)
print(test_scores)

# 可视化
mp.figure("Validation Curve")
mp.title("Validation Curve")
mp.xlabel("n_estimators", fontsize=14)
mp.ylabel("F1 Score", fontsize=14)
mp.grid(linestyle=":")
mp.plot(n_estimators, test_scores,
        "o-", # 线条风格
        c="blue", label="Test") # 颜色,文字
mp.legend()
mp.show()









