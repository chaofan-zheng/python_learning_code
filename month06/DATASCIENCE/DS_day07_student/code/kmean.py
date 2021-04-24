import numpy as np
np.random.seed(1)

# 随机生成质心
def randCent(dataSet, k):
    n = dataSet.shape[1]
    centroids = np.zeros((k, n))
    for j in range(n):
        minj = np.min(dataSet[:, j])
        maxj = np.max(dataSet[:, j])
        rangej = maxj - minj
        centroids[:, j] = minj + rangej * np.random.rand(k)
    return centroids

# 计算欧式距离
def distEclud(vecA, vecB):
    return np.sqrt(np.sum(np.power((vecA - vecB), 2)))

# 按照欧式距离进行聚类
def cluster(dataSet,k,cenBefor):
    m = dataSet.shape[0]
    clusterAssment = np.zeros(m)
    for i in range(m):
        minDist = np.inf
        for j in range(k):
            distValus = distEclud(dataSet[i, :], cenBefor[j, :])
            if distValus < minDist:
                minDist = distValus
                clusterAssment[i] = j
    return clusterAssment

# 重新计算质心
def calCent(dataSet,k,clusterAssment):
    cenAfter = np.array([[np.inf, np.inf],[np.inf, np.inf]])
    for cen in range(k):
        ptsInCluset = dataSet[clusterAssment[:] == cen]
        cenAfter[cen, :] = np.mean(ptsInCluset, axis=0)
    return cenAfter

# K均值算法实现
def KMeans(dataSet, k, createCent=randCent):
    # 随机生成两个点，假定为两类球员的平均能力
    cenBefor = createCent(dataSet,k)
    while True:
        # print(cenBefor)
        # 类别划分
        clusterAssment = cluster(dataSet,k,cenBefor)
        # print(clusterAssment)
        # 计算每类球员的真实平均能力，即质心
        cenAfter = calCent(dataSet,k,clusterAssment)
        # 判断聚类是否结束
        if (cenAfter != cenBefor).all():
            cenBefor = cenAfter
        else:
            return cenAfter,clusterAssment

if __name__ == '__main__':
    # 待聚类数据
   dataSet = np.array([[8.7,9.0],[4.2,3.6],[12.0,7.5],[5.8,4.0],[7.4,4.3],[5,6.5],[5.9,5.8],[8.1,7.3]])
    # 类别个数
   k = 2
   cen0,clu0 = KMeans(dataSet,k)
   print(cen0)
   print(clu0)
   print('---------------------')
