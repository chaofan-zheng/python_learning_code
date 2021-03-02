import numpy as np
list1=[1,2,3,4]
list2=[2,3,4,5]
print(list1+list2)
# for q,r in zip(list1,list2):
#     print(q+r)
data=[q+r for q,r in zip(list1,list2)]
print(data)
arr1=np.array(list1)
arr2=np.array(list2)
print(arr1*9)
