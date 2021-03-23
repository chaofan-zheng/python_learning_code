# 03_dt_classfier_demo.py
# 决策树分类器示例
import numpy as np
import sklearn.preprocessing as sp
import sklearn.ensemble as se
import sklearn.model_selection as ms

# 1. 读取样本, 标签编码
raw_samples = []  # 保存样本列表
with open("../data/car.txt", "r") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        raw_samples.append(line.split(","))
# 列表转数组,并转置
data = np.array(raw_samples).T
encoders = []  # 记录标签编码器
train_x = []  # 编码后的输入

for row in range(len(data)):
    encoder = sp.LabelEncoder()  # 每行创建一个编码器
    encoders.append(encoder)  # 将编码器添加到列表
    if row < len(data) - 1:  # 不是最后一行, 样本特征
        lbl_code = encoder.fit_transform(data[row])
        train_x.append(lbl_code)
    else:  # 最后一行, 样本标签
        train_y = encoder.fit_transform(data[row])

train_x = np.array(train_x).T  # 转置回来
train_y = np.array(train_y)
print(train_x)
print(train_y)

# 2. 模型定义, 训练
model = se.RandomForestClassifier(
    max_depth=8,  # 最大树高
    n_estimators=150,  # 树数量
    random_state=7)  # 随机种子
model.fit(train_x, train_y)  # 训练
print("准确率:", model.score(train_x, train_y))

# 3. 对测试数据编码, 预测
## 待预测数据
data = [['high', 'med', '5more', '4', 'big', 'low'],
        ['high', 'high', '4', '4', 'med', 'med'],
        ['low', 'low', '2', '2', 'small', 'high'],
        ['low', 'med', '3', '4', 'med', 'high']]
## 对待预测数据标签编码
data = np.array(data).T  # 转数组, 再转置
test_x = []

for row in range(len(data)):
    encoder = encoders[row]  # 根据row取出对应的编码器
    # transform是直接编码, fit_transform是生成字典并编码
    test_x.append(encoder.transform(data[row]))
test_x = np.array(test_x).T  # 转置回来

pred_test_y = model.predict(test_x)  # 预测
print(pred_test_y)

# 将预测结果由编码转换为字符串
print("预测结果:",
      encoders[-1].inverse_transform(pred_test_y))

import matplotlib.pyplot as mp

fi = model.feature_importances_  # 获取特征重要性
print("fi:", fi)

# 特征重要性可视化
mp.figure("Feature importances")
mp.plot()
mp.title("DT Feature", fontsize=16)
mp.ylabel("Feature importances", fontsize=14)
mp.grid(linestyle=":", axis=1)
x = np.arange(fi.size)

feature_names = np.array(["buying", "maint", "doors",
                          "persons", "lug_boot", "safety"])
sorted_idx = fi.argsort()[::-1]  # 重要性排序(倒序)
fi = fi[sorted_idx]  # 根据排序索引重新排特征值
mp.xticks(x, feature_names[sorted_idx])
mp.bar(x, fi, 0.4, color="dodgerblue",
       label="DT Feature importances")

mp.legend()
mp.tight_layout()
mp.show()
