# 凝聚层次聚类示例
import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as mp
import sklearn.metrics as sm

x = []
with open("../data/multiple3.txt", "r") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        data = [float(substr) for substr in line.split(",")]
        x.append(data)

x = np.array(x)

# 凝聚聚类
model = sc.AgglomerativeClustering(n_clusters=4)  # n_cluster为聚类数量
model.fit(x)  # 训练
pred_y = model.labels_  # 聚类标签（聚类结果）

# 计算并打印轮廓系数
score = sm.silhouette_score(
    x,  # 样本
    pred_y,  # 标签
    sample_size=len(x),  # 样本数量
    metric="euclidean")  # 欧式距
print("轮廓系数:", score)

# 可视化
mp.figure("Agglomerative", facecolor="lightgray")
mp.title("Agglomerative")
mp.xlabel("x", fontsize=14)
mp.ylabel("y", fontsize=14)
mp.tick_params(labelsize=10)
mp.scatter(x[:, 0], x[:, 1], s=80, c=pred_y, cmap="brg")
mp.show()
