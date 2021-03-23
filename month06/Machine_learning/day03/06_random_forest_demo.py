# 随机森林示例
import sklearn.datasets as sd
import sklearn.utils as su
import sklearn.tree as st
import sklearn.ensemble as se
import sklearn.metrics as sm

boston = sd.load_boston()  # 加载boston地区房价数据
print(boston.feature_names)
print(boston.data.shape)
print(boston.target.shape)

random_seed = 7  # 随机种子，计算随机值，相同的随机种子得到的随机值一样
x, y = su.shuffle(boston.data,
                  boston.target,
                  random_state = random_seed)
# 计算训练数据的数量
train_size = int(len(x) * 0.8) # 以boston.data中80%的数据作为训练数据
# 构建训练数据、测试数据
train_x = x[:train_size]  # 训练输入, x前面80%的数据
test_x = x[train_size:]   # 测试输入, x后面20%的数据
train_y = y[:train_size]  # 训练输出
test_y = y[train_size:]   # 测试输出

# 定义模型(集成模型,将多个决策树集成到一起)
model = se.RandomForestRegressor(
    max_depth=10, # 最大 深度
    n_estimators=1000,  # 数数量
    min_samples_split=2) # 最小样本数量,小于该数不再划分子节点

model.fit(train_x, train_y)  # 训练
pre_test_y =  model.predict(test_x) # 预测
print("R2:", sm.r2_score(test_y, pre_test_y))

import matplotlib.pyplot as mp
import numpy as np
fi = model.feature_importances_  # 获取特征重要性
print("fi:", fi)

# 特征重要性可视化
mp.figure("Feature importances")
mp.plot()
mp.title("DT Feature", fontsize=16)
mp.ylabel("Feature importances", fontsize=14)
mp.grid(linestyle=":", axis=1)
x = np.arange(fi.size)

sorted_idx = fi.argsort()[::-1]  # 重要性排序(倒序)
fi = fi[sorted_idx]  # 根据排序索引重新排特征值
mp.xticks(x, boston.feature_names[sorted_idx])
mp.bar(x, fi, 0.4, color="dodgerblue",
       label="DT Feature importances")

mp.legend()
mp.tight_layout()
mp.show()