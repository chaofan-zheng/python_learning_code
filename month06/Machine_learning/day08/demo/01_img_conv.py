# 01_img_conv.py
# 图像卷积示例
from scipy import signal
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as sn

# 读取图像
im = misc.imread("../test_img/zebra.png",  # 路径
                 flatten=True)  # 灰度图像
# 如果读不出来,尝试下面这句代码
# im = sn.imread("../test_img/zebra.png",#路径
#                  flatten=True)# 灰度图像

# 定义卷积核
flt = np.array([[-1, 0, 1],
                [-2, 0, 2],
                [-1, 0, 1]])
flt2 = np.array([[1, 2, 1],
                 [0, 0, 0],
                 [-1, -2, -1]])
conv_img1 = signal.convolve2d(
    im,  # 原图
    flt,  # 卷积核
    boundary="symm",  # 边沿处理方式
    mode="same").astype("int32")  # 输出图像和输入一样大

conv_img2 = signal.convolve2d(
    im,  # 原图
    flt2,  # 卷积核
    boundary="symm",  # 边沿处理方式
    mode="same").astype("int32")  # 输出图像和输入一样大

plt.figure("Conv2D")
plt.subplot(131)  # 1行3列第1个子图
plt.imshow(im, cmap="gray")  # 显示原图
plt.xticks([])
plt.yticks([])

plt.subplot(132)  # 1行3列第2个子图
plt.imshow(conv_img1, cmap="gray")  # 显示原图
plt.xticks([])
plt.yticks([])

plt.subplot(133)  # 1行3列第3个子图
plt.imshow(conv_img2, cmap="gray")  # 显示原图
plt.xticks([])
plt.yticks([])

plt.show()
