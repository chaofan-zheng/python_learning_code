《机器学习》周志华

# 概念性内容

推荐引擎

计算机视觉-成熟度高

- 人脸识别
- 图像分类 -是猫是狗，次品检测
- 图像生成
- 目标检测 -自动驾驶技术，有没有障碍。无人机跟拍
- 文字提取 -ORC光学字符识别 拍照搜题
- 图像语义分割 -自动驾驶 哪部分是自己的车道，哪部分是对方车道。

自然语言处理-成熟度相对低一些

- 机器翻译
- 智能问答 机器人客服 Siri
- 文本生成，让机器人写一段报道



## AI的三个基础条件

1. 算力 -云计算
2. 大量数据 -大数据
3. 优秀的算法 ![IMG_6951](/Users/aiden_zcf/Desktop/markdown笔记/IMG_6951.PNG)

## 数学推导的目的

- 消元 
- 降幂
- 用已知量替换未知量
- 变成更好求解、更好得出结论的形式

## 机器学习的一般过程

1. 数据收集
2. 数据清洗
3. 选择模型（算法）
4. 训练模型
5. 模型评估
6. 测试模型
7. 应用模型
8. 模型维护

## 机器学习的基本问题

### 1) 回归问题

根据已知的输入和输出，寻找某种性能最佳的模型，将未知输出的输入代入模型，得到**<u>连续的输出</u>**.例如：

- 根据房屋面积、地段、修建年代以及其它条件预测房屋价格
- 根据各种外部条件预测某支股票的价格
- 根据农业、气象等数据预测粮食收成
- 计算两个人脸的相似度

### 2) 分类问题 -有监督学习

根据已知的输入和输出，寻找性能最佳的模型，将未知输出的输入带入模型，得到**<u>离散的输出</u>**，例如：

- 手写体识别（10个类别分类问题）
- 水果、鲜花、动物识别
- 工业产品瑕疵检测（良品、次品二分类问题）
- 识别一个句子表达的情绪（正面、负面、中性）

### 3) 聚类问题 -无监督学习

根据已知输入的相似程度，将其划分为不同的群落，例如：

- 根据一批麦粒的数据，判断哪些属于同一个品种
- 根据客户在电商网站的浏览和购买历史，判断哪些客户对某件商品感兴趣
- 判断哪些客户具有更高的相似度

### 4) 降维问题

在性能损失尽可能小的情况下，降低数据的复杂度，数据规模缩小都称为降维问题.
