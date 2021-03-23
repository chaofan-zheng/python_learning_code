# 05_aggl_demo2.py
# 凝聚层次(考虑样本分布连续性)
import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as mp
import sklearn.neighbors as nb

# 创建样本
n_sample = 500
# 产生随机角度
t = 2.5 * np.pi * (1 + 2 * np.random.rand(n_sample, 1))
# 根据三角函数计算螺线
x = 0.05 * t * np.cos(t)
y = 0.05 * t * np.sin(t)
n = 0.05 * np.random.rand(n_sample, 2)  # 产生随机噪声
# print(x.shape)
# print(y.shape)
x = np.hstack((x, y)) + n  # 水平合并,并加入噪声
print(x.shape)

# 凝聚层次(不考虑样本连续性)
# model = sc.AgglomerativeClustering(n_clusters=3,
#                                    linkage="average")
# model.fit(x)
# pred_y1 = model.labels_ # 聚类结果

# 凝聚层次(考虑样本分布连续性)
## 先创建每个样本的邻近集合
conn = nb.kneighbors_graph(x, 10, include_self=False)
model = sc.AgglomerativeClustering(
    n_clusters=3, # 聚类数量
    linkage="average", # 计算聚簇间距离方式
    connectivity=conn) # 邻近集合,在凝聚过程中优先考虑连续性好的样本
model.fit(x)
pred_y1 = model.labels_ # 聚类结果

# 可视化
mp.figure("AgglomerativeClustering Cluster",
          facecolor="lightgray")
mp.title("AgglomerativeClustering Cluster")
mp.xlabel("x", fontsize=14)
mp.ylabel("y", fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=":")
mp.axis("equal")
mp.scatter(x[:, 0], x[:, 1], c=pred_y1, cmap="brg", s=80, alpha=0.5)
mp.show()
