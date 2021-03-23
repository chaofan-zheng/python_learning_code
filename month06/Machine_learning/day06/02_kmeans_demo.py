# 02_kmeans_demo.py
# k-means聚类示例
import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as mp

x = [] # 样本输入(无监督学习没有标签)
with open("../data/multiple3.txt", "r") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        data = [float(substr)
                for substr in line.split(",")]
        x.append(data)
x = np.array(x)

model = sc.KMeans(n_clusters=4) # 参数为聚类数量
model.fit(x) # 训练(执行聚类)

pred_y = model.labels_ # 取出聚类结果
centers = model.cluster_centers_ # 取出聚类的中心
print("聚类结果:", pred_y)
print("聚类中心:", centers)

# 可视化
mp.figure("K-Means")
mp.title("K-Means")
mp.xlabel("x", fontsize=14)
mp.ylabel("y", fontsize=14)
mp.scatter(x[:, 0], x[:, 1], # 散点x,y坐标
           s=80, c=pred_y, cmap="brg")
mp.scatter(centers[:, 0], centers[:,1],# 中心x,y坐标
           marker="+", # 形状
           c="black", s=200, linewidths=1)#颜色，尺寸，线条宽度
mp.show()