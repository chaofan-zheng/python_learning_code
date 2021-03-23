# 05_dump_demo.py
# 模型定义,训练,保存示例
import numpy as np
import sklearn.linear_model as lm # 线性模型
import pickle

x = np.array([[0.5], [0.6], [0.8], [1.1], [1.4]])  # 输入集
y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])  # 输出集

model =lm.LinearRegression()
model.fit(x, y) # 训练
print("训练完成.")

# 保存模型
with open("linear_model.pkl", "wb") as f:
    pickle.dump(model, f) # 保存
    print("保存模型成功.")



