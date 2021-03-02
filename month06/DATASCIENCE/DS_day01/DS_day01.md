[toc]

# numpy数值计算基础

## 一：numpy介绍
安装方法： pip install  numpy

NumPy(Numerical Python) 是 Python 语言的一个扩展程序库，支持大量的维度数组与矩阵运算，此外也针对数组运算提供大量的数学函数库。

1. Numerical Python，数值的Python，补充了Python语言所欠缺的数值计算能力。
2. Numpy是其它数据分析及机器学习库的底层库。
3. Numpy完全标准C语言实现，运行效率充分优化。
4. Numpy开源免费。

## 二：numpy系统学习教程

1. https://www.numpy.org.cn/user/quickstart.html#%E5%85%88%E5%86%B3%E6%9D%A1%E4%BB%B6
2. https://www.runoob.com/numpy/numpy-tutorial.html

## 三：掌握 NumPy 数组对象 ndarray
###  1) ndarray介绍
NumPy最核心的数据类型是N维数组(The N-dimensional array(ndarry))。
1. NumPy 最重要的一个特点是其 N 维数组对象 ndarray，它是一系列同类型数据的集合，以 0 下标为开始进行集合中元素的索引。

2. ndarray 对象是用于存放同类型元素的多维数组。

3. 数组：数组（Array）是有序的元素序列，在程序设计中，为了处理方便， 把具有相同类型的若干元素按有序的形式组织起来的一种形式。这些有序排列的同类数据元素的集合称为数组。

   ![](data\ndarry.png)

###  2) python列表和Numpy数组的区别  
1. 列表list与数组array的定义：
	列表是由一系列按特定顺序排列的元素组成，可以将任何东西加入列表中，其中的元素之间没有任何关系；Python中的列表(list)用于顺序存储结构。它可以方便、高效的的添加删除元素，并且列表中的元素可以是多种类型。
    数组也就是一个同一类型的数据的有限集合。
2. 列表list与数组array的相同点：都可以根据索引来取其中的元素；

3. 列表list与数组array的不同点：
    a.列表list中的元素的数据类型可以不一样。数组array里的元素的数据类型一般是一样的；
    b.列表list不可以进行数学四则运算，数组array可以进行数学四则运算；　
#### 代码练习：demo_numpy.py

区分列表和数组

```python
import numpy as np
lis1=[1,2,3,4]  #lis1是列表类型
a = np.array([1,2,3,4])  #a是数组类型
print("list",lis1,lis1[0],'\n','array',a,a[0])
print("list+list",lis1+lis1,'\n','array+array',a+a)
```

###  3)  创建数组对象ndarray及基本操作

#### 代码练习：numpy_ndarry1.py

1.  创建数组 numpy.array(object，dtype，ndmin)

| 参数名称 | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| object   | 接收array。表示想要创建的数组。无默认。                      |
| dtype    | 接收data-type。表示数组所需的数据类型。如果未给定，则选择保存对象所需的最小类型。默认为None |
| ndmin    | 指定生成数组的最小维数                                       |

2.  数组属性  

| 属性     | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| ndim     | 返回 int。表示数组的维数                                     |
| shape    | 返回 tuple。表示数组的尺寸，对于 n 行 m 列的矩阵，形状为(n,m) |
| size     | 返回 int。表示数组的元素总数，等于数组形状的乘积             |
| dtype    | 返回 data-type。描述数组中元素的类型                         |
| itemsize | 返回 int。表示数组的每个元素的大小（以字节为单位）。         |

```python
import numpy as np
# 创建一维数组
arr1=np.array([1,2,3,4],ndmin=2)
# 创建二维数组
arr2=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr1)
print(arr2)
print('数组类型',arr2.dtype)
print('数组元素个数',arr2.size)
print('数组维度',arr2.ndim)
print('数组形状',arr2.shape)
# 修改数组形状
arr2.shape=4,3
print(arr2)
```

### 4)创建特殊数组

#### 代码练习：numpy_ndarry2.py

1. 使用 arange 函数

创建数组arange(起始值，结束值, 步长)根据起始值与结束值指定的范围以及s设定的步长，生成一个 ndarray。但不包含结束值。

np.arange(起始值(0),终止值,步长(1))

```python
import numpy as np
a = np.arange(0, 5, 1)
print(a)
b = np.arange(0, 10, 2)
print(b)
```

2. np.zeros(数组元素个数)

```python
import numpy as np
a = np.zeros(10)
print(a)
print('使用zeros函数创建二维数组:\n',np.zeros((2,3)))
```

3. np.ones(数组元素个数)

```python
import numpy as np
b = np.ones(10)
print(b)
print('使用ones函数创建全是1的数组:\n',np.ones((3,4)))
```

### 5)  数据类型  

1. NumPy基本数据类型与其取值范围，后面的数字就代表这个数据类型占据的空间。


| 类型名       | 类型表示符                              |
| ------------ | --------------------------------------- |
| 布尔型       | bool_                                   |
| 有符号整数型 | int8(-128~127) / int16 / int32 / int64  |
| 无符号整数型 | uint8(0~255) / uint16 / uint32 / uint64 |
| 浮点型       | float16 / float32 / float64             |
| 复数型       | complex64 / complex128                  |
| 字串型       | str_，每个字符用32位Unicode编码表示     |
| 日期类型     | datetime64                              |

在计算机内部，信息都是釆用二进制的形式进行存储，计算机的基本的存储单元有：

位（bit）：二进制数中的一个数位，可以是0或者1，是计算机中数据的最小单位。二进制的一个“0”或一个“1”叫一位。

字节（Byte，B）：计算机中数据的基本单位，每8位组成一个字节。各种信息在计算机中存储、处理至少需要一个字节。

字（Word）：两个字节称为一个字。汉字的存储单位都是一个字。

2. 数据类型取值范围分析

- int8占1个字节(byte) 也就是8个二进制位(bit)
- 每个二进制位 可以存储0 和 1 两个数 ，8个二进制位就有2^8 = 256种组合(可以存储256个数)
- int8为有符号，所以正数和负数将平分256个数。256 / 2 = 128
- 负数为128个数 最小值为-128 
- 正数为128个数，0占一个数 最大值为+127 
- 如果是uint8(8bit无符号-没有负数) 2^8 = 256
- 0 占一个数 ，所以最大是255

### 6)  随机数模块 

####  代码练习：numpy_random.py

random模块常用随机数生成函数

| 函数                       | 说明                   | 备注                                      |
| -------------------------- | ---------------------- | ----------------------------------------- |
| seed                       | 确定随机数生成器的种子 | 参数一般为整数                            |
| randn(d0, d1, …, dn)       | 产生标准正态分布随机数 | 生成一维/二维数组                         |
| randint(low，high, [size]) | 产生随机整数           | low：最小值；high：最大值；size：数据个数 |
| random()                   | 随机返回数据           | 返回随机生成的一个实数，它在[0,1)范围内。 |

```python
import numpy as np
# 随机数模块
# 生成三行三列符合标准正态分布的数据
np.random.seed(234)
print(np.random.randn(3,3))
# 1-100以内生成5行5列随机整数
print(np.random.randint(1,100,[5,5]))
# 0-1之间生成10个随机数
print(np.random.random(10))
```

## 四： 利用 NumPy 进行统计分析

### 1)  通过索引访问数组  

####  代码练习：numpy_analysis1.py

 一维数组的索引访问

```python
import numpy as np
# 创建一维数组
arr=np.arange(10)
print(arr)
# 访问单个值
print(arr[3])
print(arr[-1])
# 访问范围
print(arr[2:8])
print(arr[8:2:-2])
# 数组的修改
arr[2:4]=10,11
print(arr)
```

 二维数组的索引访问

 ```python
import numpy as np
# 创建二维数组
arr=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr)
arr=np.arange(12).reshape(3,4)
print(arr)
# 对于行列都有要求
print(arr[0:2,1:3])
# 按照行的条件选择数据
print(arr[0:2])
# 按照列选择数据
print(arr[:,2:4])
print(arr[1][1])
 ```

### 2)  使用numpy进行文件读写

#### 代码练习：numpy_analysis2.py

1. NumPy文件存储

   save函数保存数据。 np.save(“save_arr”,创建的数组名称)

   savez函数可以将多个数组保存到一个文件中。 np.savez('savez_arr',arr1,arr2)

2. NumPy文件读取

   load函数是从二进制的文件中读取数据。 np.load("save_arr.npy") 

   存储时可以省略扩展名，但读取时不能省略扩展名。

   ```python
   import numpy as np
   #使用numpy读写文件
   # 创建一个数组并保存
   arr=np.arange(100).reshape(10,10)
   # np.save(file='save_arr',arr=arr)
   # load_data=np.load('save_arr.npy')
   # print(load_data)
   
   # 创建两个数组并保存
   arr1=np.array([1,2,3,4])
   np.savez('savez_arr',arr,arr1)
load_data2=np.load('savez_arr.npz')
   print(load_data2.files)
   # 读取第一个数组
   arr_data1=load_data2['arr_0']
   # 读取第二个数组
   arr_data2=load_data2['arr_1']
   print(arr_data1,arr_data2)
   ```
   
   作业：读取国民生产总值.npz文件  
   
   代码：numpy_npz.py

 ### 3)  使用numpy进行简单统计分析  

 #### 代码练习：numpy_analysis3.py

1. 直接排序

   sort函数是最常用的排序方法。 arr.sort()

   sort函数也可以指定一个axis参数，使得sort函数可以沿着指定轴对数据集进行排序。axis=1为沿横轴排序； axis=0为沿纵轴排序，如图所示：


2. 间接排序

   argsort函数返回值为重新排序值的下标。 arr.argsort()

3.  numpy常用的统计函数  

    (1)、当axis=0时，表示沿着纵轴计算。当axis=1时，表示沿着横轴计算。默认时计算一个总值,如图所示![](data\sort.png)
    | **函数**    | **说明**                 |
   | ----------- | ------------------------ |
   | **sum**     | 计算数组的和             |
   | **mean**    | 计算数组均值             |
   | **std**     | 计算数组标准差           |
   | **var**     | 计算数组方差             |
   | **min**     | 计算数组最小值           |
   | **max**     | 计算数组最大值           |
   | **argmin**  | 返回数组最小元素的索引   |
   | **argmax**  | 返回数组最大元素的索引   |
   | **cumsum**  | **计算所有元素的累计和** |
   | **cumprod** | **计算所有元素的累计积** |

    (2)、标准差和方差概念理解

   ![](data\analysis.png)

  ![case1](data\case1.png)

   ![1](H:\脱产2008班备课\day01\DS_day01_student\data\1.png)

   ![](H:\脱产2008班备课\day01\DS_day01_student\data\2.png)

   ![3](H:\脱产2008班备课\day01\DS_day01_student\data\3.png)

  标准差和平均数的量纲（单位）是一致的，在描述一个波动范围时标准差比方差更方便，方差被标准化了。开根号，统一单位，取名标准差   

   简单来说，标准差是一组数值自平均值分散开来的程度的一种测量观念。一个较大的标准差，代表大部分的数值和其平均值之间差异较大；一个较小的标准差，代表这些数值较接近平均值。

   标准差通常是相对于样本数据的平均值而定的，表示距离平均值的平均距离

```python
# 排序算法
import numpy as np
data=np.array([2,5,6,9,1,8,7])
# 返回最小元素的索引
print(np.argmin(data))
# 对数据进行排序
data.sort()
print(data)
# 返回排序之后的索引
data_arg=data.argsort()
print(data_arg)
data=np.array([[1,5,2,7]
              ,[4,8,3,6]
              ,[7,8,11,10]])
print(data)
# 横向排序
data.sort(axis=1)
print(data)

# 基本统计分析
arr=np.arange(20).reshape(4,5)
print(arr)
# 计算每一行的平均值 横向计算
print(arr.mean(axis=1))
# 计算每一列的平均值 纵向计算
print(arr.mean(axis=0))
# 整组数据的标准差
print(arr.std())
# 数据每一行的标准差
print(arr.std(axis=1))
# 数据每一列的标准差
print(arr.std(axis=0))
# 计算数据的累积和
print(np.cumsum(arr,axis=0))
# 计算数据的累积积
print(np.cumprod(arr,axis=1))
```

# scipy高级科学计算库

## 一：scipy介绍

和Numpy联系很密切，Scipy一般都是操控Numpy数组来进行科学计算，所以可以说是基于Numpy之上了。 由一些特定功能的子模块组成.介绍了一些常数和特殊函数，如贝塞尔函数，这对物理学问题的计算提供了方便；如图所示

![scipy](data\scipy.png)

参考教程：https://docs.scipy.org/doc/scipy/reference/index.html

安装方法： pip install  scipy  

## 二：基于scipy完成拟合与优化实例

#### 代码练习：demo_scipy.py

#### 目标：拟合数据并预测

已知一组样本数据如下所示，根据样本图像大致形状确定函数形式 可能是 满足 f(x)=kx+b 线性关系，请绘制线性函数将其进行拟合：即一条光滑的曲线把数据近似连接起来，预测在x为10，y的值

Xi=[6.19,2.51,7.29,7.01,5.7,2.66,3.98,2.5,9.1,4.2] 

Yi=[5.25,2.83,6.41,6.71,5.1,4.23,5.05,1.98,10.5,6.3] 

![scatter](data\scatter.png)

1. 对于平面中的这n个点，可以使用无数条曲线来拟合。要求函数尽可能好地拟合这组值  

2. 既然是「猜测」的 f(x)=kx+b 线性关系，那么就存在误差。会有很多点不在f(x)=kx+b 上，那么我们将这个函数关系稍加修正为：y=f(x)+e  y=kx+b+e  e=y-kx-b的值叫做残差/误差 
3. 根据已有的数值行为，预测未知的数据，是回归问题，这也是最基础的简单一元线性回归模型e=y-kx-b，描述y如何依赖x和误差项的方程 
4. 目标应用算法及相应的函数来解决问题--估计模型参数 k和b
5. 综合起来看，这条直线处于样本数据的中心位置最合理。 选择最佳拟合曲线的标准可以确定为：使总的拟合误差（即总残差）达到最小。  最常用的是普通最小二乘法（ Ordinary Least Square，OLS）：最小二乘法的原则是以“残差平方和最小”确定直线位置， （Q为残差平方和）- 即采用平方损失函数。如图所示

![OLS](data\OLS.png)

#### 解决方案：采用最小二乘法

最小二乘法（least square method）是一种数学优化技术。它通过最小化误差的平方和寻找数据的最佳函数匹配。利用最小二乘法可以简便地求解模型参数，预测出未知的数据

在scipy的optimize子函数库中，提供了leastsq函数用于实现最小二乘法  

leastsq(func, x0, args=(), Dfun=None, full_output=0, col_deriv=0, ftol=1.49012e-08, xtol=1.49012e-08, gtol=0.0, maxfev=0, epsfcn=0.0,factor=100, diag=None)

一般我们只要指定前三个参数就可以了。

1、func 是我们自己定义的一个计算误差的函数， 指出了待拟合函数的函数形状。

2、x0里放的是k、b的初始值，这个值可以随意指定。往后随着迭代次数增加，k、b将会不断变化，使得error函数的值越来越小。

3、error函数为误差函数，我们的目标就是不断调整k和b使得error不断减小。这里的error函数和神经网络中常说的cost函数实际上是一回事，只不过这里更简单些而已。

4、必须注意一点，传入leastsq函数的参数可以有多个，但必须把参数的初始值p0和其它参数分开放。其它参数应打包到args中。

```py
import numpy as np
from scipy.optimize import leastsq
Xi = np.array([6.19,2.51,7.29,7.01,5.7,2.66,3.98,2.5,9.1,4.2])
Yi = np.array([5.25,2.83,6.41,6.71,5.1,4.23,5.05,1.98,10.5,6.3])
# 定义拟合函数
def func(p,x):
    k,b=p
    return k*x+b
# 定义误差函数
def error(p,x,y,s):
    print(s)
    return func(p,x)-y
# 设置初始值
p0=[1,1]
s='test the number of interation'
# 主函数
result=leastsq(error,p0,args=(Xi,Yi,s))
print(result)
k,b=result[0]
print('k=',k,'\n','b=',b)
# 预测x=10,y的值
y=k*10+b
print(y)
y1=np.round(y,2)
print(y1)
```

































































