import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
import seaborn as sns

warnings.filterwarnings("ignore")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data = pd.read_csv('wholesale.csv')
data = data.drop(columns='href')
data_clean = data[data.integer.notnull()][data.rePurchaseRate.notnull()]
for i in data_clean['integer']:
    try:
        i = int(i)
    except:
        # print(data_clean.loc[i,'integer'])
        data_clean = data_clean.drop(data_clean[data_clean['integer'].str.contains(i)].index)
for i in data_clean['rePurchaseRate']:
    try:
        i = float(i)
    except:
        # print(data_clean.loc[i,'integer'])
        data_clean = data_clean.drop(data_clean[data_clean['rePurchaseRate'].str.contains(i)].index)
data_clean.integer = data_clean.integer.astype('int')
data_clean.rePurchaseRate = data_clean.rePurchaseRate.astype('float')
print(data_clean.head())
print(data_clean.describe())
# print(data_clean['rePurchaseRate'])
fig=plt.figure(figsize = (16,12))
ax1=fig.add_subplot(221)
plt.title('复购率频次分布图',fontsize=14)
sns.distplot(data_clean['rePurchaseRate'])

ax1=fig.add_subplot(222)
plt.title('销售量频次分布图',fontsize=14)
sns.distplot(data_clean['integer'])

ax1=fig.add_subplot(223)
plt.title('复购率箱体图',fontsize=14)
sns.boxplot(x='rePurchaseRate',data=data_clean)

ax1=fig.add_subplot(224)
plt.title('销售量箱体图',fontsize=14)
sns.boxplot(x='integer',data=data_clean)
plt.show()


