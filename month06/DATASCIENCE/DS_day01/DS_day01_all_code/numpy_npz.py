# 读取国民经济季度核算数据
import numpy as np
# 课间练习
data=np.load('国民经济核算季度数据.npz'
             ,allow_pickle=True)
print(data)
# 查看数组名称
print(data.files)
# 得到数据列名
print(data['columns'])
# 得到数据的值
print(data['values'])