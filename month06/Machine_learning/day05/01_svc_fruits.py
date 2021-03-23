# 05_svc_fruits.py
# 利用SVC(支持向量分类器)实现水果图像分类
import os
import numpy as np
import cv2 as cv
import sklearn.metrics as sm
import sklearn.preprocessing as sp
import sklearn.svm as svm

name_dict = {"apple": 0, "banana": 1, "grape": 2}


# 读取所有图像路径, 并存入字段
# 字典键值对格式如: "apple":["1.jpg","2.jpg"]
def search_samples(dir_path):  # 参数为数据集路径
    img_samples = {}  # 新建一个空字典

    dirs = os.listdir(dir_path)  # 列出子目录
    for d in dirs:  # 遍历子目录
        # 拼接子目录完整路径
        sub_dir_path = dir_path + "/" + d

        if not os.path.isdir(sub_dir_path):
            continue

        # 如果是目录, 列出目录下所有的图片
        imgs = os.listdir(sub_dir_path)
        for img_file in imgs:
            # 拼接图片完整路径
            img_path = sub_dir_path + "/" + img_file

            # 存入字典
            if d in img_samples:  # 类别已经在字典中
                img_samples[d].append(img_path)
            else:  # 类别不在字典中
                img_list = []  # 创建空列表
                img_list.append(img_path)  # 图像存入列表
                img_samples[d] = img_list  # 列表存入字典
    return img_samples  # 返回字典


train_samples = search_samples("fruits_tiny/train")

# 存放输入(图像特征向量),输出(类别)
train_x, train_y = [], []

for label, img_list in train_samples.items():  # 遍历字典
    descs = np.array([])  # 图像特征

    for img_file in img_list:  # 读取每个图像路径
        # 根据路径,读取图像
        print("读取样本:", img_file)

        im = cv.imread(img_file)  # 读取并返回图像数据
        # 将彩色图像转换为灰度图像
        im_gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)

        # 图像缩放
        h, w = im_gray.shape[:2]  # 取出高度,宽度
        f = 200 / min(h, w)  # 计算缩放比率
        im_gray = cv.resize(
            im_gray,  # 原图
            None,  # 输出图像大小
            fx=f, fy=f)  # 设置两个方向缩放比率

        # 特征提取(图像 ==> 特征向量)
        sift = cv.xfeatures2d.SIFT_create()
        keypoints = sift.detect(im_gray) # 提取关键点
        # 计算特征值
        _, desc = sift.compute(im_gray, keypoints)
        # 将特征矩阵合并成特征向量
        desc = np.sum(desc, axis=0) # 在列方向求和

        train_x.append(desc) # 将特征向量加入train_x
        train_y.append(name_dict[label]) # 取类别并存入train_y

train_x = np.array(train_x)
train_y = np.array(train_y)
print(train_x.shape)
print(train_y.shape)

# 定义模型, 训练
model = svm.SVC(kernel="poly", degree=2)
model.fit(train_x, train_y)
print("训练结束.")
print("精确度:", model.score(train_x, train_y))


############## 模型评估 ###############
# 使用测试集的数据,进行预测
test_samples = search_samples("fruits_tiny/test")
test_x, test_y = [], [] # 测试数据输入, 输出

for label, filenames in test_samples.items():
    for img_file in filenames:
        print("读取测试样本:", img_file)

        # 读取图像数据
        img = cv.imread(img_file)
        # 彩色图像转灰度图像
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # 图像缩放成统一大小
        h, w = gray.shape[:2] # 取出图像高度,宽度
        f = 200 / min(h, w) # 计算缩放比率
        gray = cv.resize(gray, None, fx=f, fy=f)

        # 提取特征
        sift = cv.xfeatures2d.SIFT_create()
        keypoints = sift.detect(gray)
        _, desc = sift.compute(gray, keypoints)
        # desc是特征矩阵, 扁平化处理成特征向量
        desc = np.sum(desc, axis=0) # 合并成1行

        test_x.append(desc) # 将图片特征向量存入test_x
        test_y.append(name_dict[label])

print("开始预测...")
pred_test_y = model.predict(test_x) # 预测
# 打印预测准确率
print(sm.accuracy_score(test_y, pred_test_y))












