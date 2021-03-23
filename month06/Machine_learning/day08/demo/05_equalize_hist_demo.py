# 05_equalize_hist_demo.py
# 直方图均衡化处理示例
import cv2
from matplotlib import pyplot as plt

im = cv2.imread("../test_img/sunrise.jpg", #路径
                0)# 读取成灰度图像
cv2.imshow("im", im)
# 直方图均衡化处理
im_equ = cv2.equalizeHist(im)
cv2.imshow("im_equ", im_equ)

cv2.waitKey()
cv2.destroyAllWindows()

# 绘制原图, 均衡化处理后的图像统计直方图
plt.subplot(2, 1, 1) # 2行1列第1个子图
plt.hist(im.ravel(), # 数组(转成一维的数组)
         256, # 柱体数量
         [0, 255], # 范围
         label="orig") # 显示文字
plt.subplot(2, 1, 2)
plt.hist(im_equ.ravel(), # 数组(转成一维的数组)
         256, # 柱体数量
         [0, 255], # 范围
         label="equ") # 显示文字
plt.legend()
plt.show()


