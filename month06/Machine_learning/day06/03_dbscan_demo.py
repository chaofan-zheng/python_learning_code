# 03_dbscan_demo.py
# 噪声密度聚类示例
import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as mp
import sklearn.metrics as sm

# 读取样本
x = []
with open("../data/perf.txt", "r") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        data = [float(substr)
                for substr in line.split(",")]
        x.append(data)
x = np.array(x)

# 创建模型
model = sc.DBSCAN(eps=0.8, # 邻域半径
                  min_samples=5) # 最小样本数量
model.fit(x) # 训练(执行聚类)
pred_y = model.labels_ # 聚类结果
print(pred_y)

# 区分核心点, 边界点, 噪声点
## 挑选出核心样本
core_mask = np.zeros(len(x), dtype=bool)
#print(core_mask)
core_mask[model.core_sample_indices_] = True
#print(core_mask)

## 挑选出噪声点
offset_mask = (pred_y == -1)
# print(offset_mask)

## 边界点(既不是核心点,又不是噪声点)
periphery_mask = ~(core_mask | offset_mask)
print(periphery_mask)

# 可视化
mp.figure('DBSCAN Cluster', facecolor='lightgray')
mp.title('DBSCAN Cluster', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=14)
mp.grid(linestyle=':')
labels = set(pred_y) # 取出聚簇编号并去重
print(labels)
cs = mp.get_cmap('brg', len(labels))(range(len(labels)))
print("cs:", cs)

# 核心点
mp.scatter(x[core_mask][:, 0],  # x坐标值数组
           x[core_mask][:, 1],  # y坐标值数组
           c=cs[pred_y[core_mask]],
           s=80, label='Core')
# 边界点
mp.scatter(x[periphery_mask][:, 0],
           x[periphery_mask][:, 1],
           edgecolor=cs[pred_y[periphery_mask]],
           facecolor='none', s=80, label='Periphery')
# 噪声点
mp.scatter(x[offset_mask][:, 0],
           x[offset_mask][:, 1],
           marker='D', c=cs[pred_y[offset_mask]],
           s=80, label='Offset')
mp.legend()
mp.show()