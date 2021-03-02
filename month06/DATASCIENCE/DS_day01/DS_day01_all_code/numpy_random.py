import numpy as np
# 定义随机种子
np.random.seed(100)
# 生成符合标准正态分布的数据:3行3列
# 均值为0，标准差为1
data1=np.random.randn(3,3)
print(data1)
# 1-100以内，生成5行5列随机整数
data2=np.random.randint(1,100,[5,5])
print(data2)
# 0-1之间生成10个随机数
# print(np.random.random((2,1)))
print(np.random.random(10))