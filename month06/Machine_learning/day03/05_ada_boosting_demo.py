# 05_ada_boosting_demo.py
# 正向激励示例
# 正向激励:
# (1) 一种集成学习算法
# (2) 每个模型根据上一个模型预测结果
#     调整样本权值, 将修改后权值的数据交给下一个模型
#     最后将这些模型预测结果融合起来,从而提升准确率
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
model = se.AdaBoostRegressor(
    st.DecisionTreeRegressor(max_depth=4),#基本模型
    n_estimators=400, # 模型数量
    random_state=7)  # 随机种子

model.fit(train_x, train_y)  # 训练
pre_test_y =  model.predict(test_x) # 预测
print("R2:", sm.r2_score(test_y, pre_test_y))
