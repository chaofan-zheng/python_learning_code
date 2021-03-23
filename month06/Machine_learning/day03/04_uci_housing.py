# 04_uci_housing.py
# 利用决策树实现波士顿房价预测
import sklearn.datasets as sd
import sklearn.utils as su
import sklearn.tree as st
import sklearn.metrics as sm

# 加载数据
boston = sd.load_boston()  # 加载数据
# print(boston.feature_names) # 打印特征名称
# print(boston.data) # 打印特征
# print(boston.target) # 打印标签

# 数据集随机化
x, y = su.shuffle(boston.data,  # 特征
                  boston.target,  # 标签
                  random_state=7)  # 随机种子(产生初始值)
# 划分训练集, 测试集
train_size = int(len(x) * 0.8) # 计算训练集大小
# 通过切片操作,分出训练集/测试集
train_x = x[:train_size] # 前80%划入训练集输入
test_x = x[train_size:] # 剩余20%划入测试集输入
train_y = y[:train_size]# 前80%划入训练集输出
test_y = y[train_size:]# 剩余20%划入测试集输出

# 定义模型
model = st.DecisionTreeRegressor(max_depth=4)
model.fit(train_x, train_y) # 训练
pre_test_y = model.predict(test_x) # 预测
# 打印R2值
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