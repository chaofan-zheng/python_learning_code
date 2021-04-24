## NBA球星数据能力划分

## 一：导入数据

代码目标：导入数据

```Python
import numpy as np
from sklearn.cluster import KMeans
dataSet = np.array([[8.7,9.0],[4.2,3.6],[12.0,7.5],[5.8,4.0],[7.4,4.3],[5,6.5],[5.9,5.8],[8.1,7.3]])
```

##  二：构建并训练模型

```Python
##构建并训练模型
kmeans=KMeans(n_clusters=2,random_state=12).fit(dataSet)
print(kmeans.labels_)
print(kmeans.cluster_centers_)
```

得到模型参数

```python
a=kmeans.labels_
print(a)
import pandas as pd
s=pd.Series(a)
print(s)
```





###  
