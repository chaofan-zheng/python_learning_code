# 航空公司客户价值分析

## 一：导入数据

代码目标：导入数据

```Python
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
airline_data=pd.read_csv('../data/air_data.csv',encoding='gb18030')
airline_data.head()
```

##  二：数据描述性统计分析

```Python
airline_data.info()
airline_data.describe()
```

##  三：数据预处理

```python
# 1. 去除票价为空的数据
exp1=airline_data['SUM_YR_1'].notnull()
exp2=airline_data['SUM_YR_2'].notnull()
exp=exp1&exp2
airline_notnull=airline_data.loc[exp,:]
# airline_notnull=airline_data[exp]
# 删除缺失记录后的数据
airline_notnull.shape
#2.只保留票价不为0，平均折扣率不为0，总飞行公里数大于0的记录
index1=airline_notnull['SUM_YR_1']!=0
index2=airline_notnull['SUM_YR_2']!=0
index3=(airline_notnull['avg_discount']!=0)&(airline_notnull['SEG_KM_SUM']>0)
airline=airline_notnull[(index1 | index2)&index3]
airline.shape
```

##  四：构建特征

```python
# 选取需求特征
airline_selection=airline[['LOAD_TIME','FFP_DATE','LAST_TO_END','FLIGHT_COUNT','SEG_KM_SUM','avg_discount']]
airline_selection.head()
airline_selection['LOAD_TIME']=pd.to_datetime(airline_selection['LOAD_TIME'])
airline_selection['FFP_DATE']=pd.to_datetime(airline_selection['FFP_DATE'])
# 构建L特征
L=airline_selection['LOAD_TIME']-airline_selection['FFP_DATE']
L=L.astype('str').str.split().str[0]
L=L.astype('int')/30
L=np.round(L,2)
# L
# 合并特征
airline_features=pd.concat(objs=[L,airline_selection.iloc[:,2:]],axis=1)
airline_features.head()
airline_features=airline_features.rename(columns={0:'L'})
airline_features.head()
airline_features_scaled=(airline_features-airline_features.mean())/(airline_features.std())
airline_features_scaled.describe()
# 不打印科学计数法
np.set_printoptions(suppress=True)
```
##  五：构建模型并训练
```python
# 导入算法
from sklearn.cluster import KMeans
# 确定聚类中心数据
k=5
# 构建模型，训练模型
kmeans_model=KMeans(n_clusters=k,random_state=123).fit(airline_features_scaled)
# 聚类标签
# kmeans_model.labels_
# 聚类中心
kmeans_model.cluster_centers_
# 统计不同类别样本数目
r1=pd.Series(kmeans_model.labels_).value_counts()
r1
# 保存数据
airline_features['id']=airline['MEMBER_NO']
airline_features['label']=kmeans_model.labels_
airline_features.head()
airline_0=airline_features[airline_features['label']==0]
airline_1=airline_features[airline_features['label']==1]
airline_2=airline_features[airline_features['label']==2]
airline_3=airline_features[airline_features['label']==3]
airline_4=airline_features[airline_features['label']==4]
writer=pd.ExcelWriter('airline_output.xlsx')
airline_0.to_excel(writer,'Sheet1')
airline_1.to_excel(writer,'Sheet2')
airline_2.to_excel(writer,'Sheet3')
airline_3.to_excel(writer,'Sheet4')
airline_4.to_excel(writer,'Sheet5')
writer.save()
```

###  
