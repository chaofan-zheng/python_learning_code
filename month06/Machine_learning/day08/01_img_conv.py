"""
图像卷积实例
斑马图像位置
../DeepLearning/dataset/data/zebra.png
"""
from scipy import signal
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as sn
import imageio

# 读取图像
# im = misc.imread('../DeepLearning/dataset/data/zebra.png',
#                  flatten=True)  # 灰度图像

# 如果读不出来，就用下面的代码
# im=sn.imread()
im = imageio.imread('../DeepLearning/dataset/data/zebra.png', as_gray=True)  # 灰度图像

# 定义卷积核
flt = np.array([[-1, 0, 1],
                [-2, 0, 2],
                [-1, 0, 1]])  # 这个卷积核能够加强垂直纹理，对水平纹理进行压制

flt2 = np.array([[1, 2, 1],
                 [0, 0, 0],
                 [-1, -2, -1]])  # 这个卷积核能够加强水平纹理，对垂直纹理进行压制
conv_img1 = signal.convolve2d(im,
                              flt,
                              boundary='symm',  # 边沿处理方式
                              mode='same').astype('int32')  # 输出图像核输入图像一样大

conv_img2 = signal.convolve2d(im,
                              flt2,
                              boundary='symm',  # 边沿处理方式
                              mode='same').astype('int32')  # 输出图像核输入图像一样大

plt.figure('Conv2D')
plt.subplot(131)
plt.imshow(im, cmap="gray")  # 第一个原图
plt.xticks([])
plt.yticks([])

plt.subplot(132)
plt.imshow(conv_img1, cmap="gray")  # 卷积后的图像
plt.xticks([])
plt.yticks([])

plt.subplot(133)
plt.imshow(conv_img2, cmap="gray")  # 卷积后的图像
plt.xticks([])
plt.yticks([])

plt.show()
