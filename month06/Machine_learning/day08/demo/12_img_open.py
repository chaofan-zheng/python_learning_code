# 12_img_open.py
# 图像开运算
import cv2
import numpy as np

# 读取图像
im1 = cv2.imread("../test_img/7.png")
im2 = cv2.imread("../test_img/8.png")

kernel = np.ones((10, 10), np.uint8)#计算核
r1 = cv2.morphologyEx(im1, # 原图
                      cv2.MORPH_OPEN,#开运算选项
                      kernel)#计算核
r2 = cv2.morphologyEx(im2,# 原图
                      cv2.MORPH_OPEN,#开运算选项
                      kernel)#计算核
cv2.imshow("im1", im1)
cv2.imshow("im2", im2)
cv2.imshow("r1", r1)
cv2.imshow("r2", r2)
cv2.waitKey()
cv2.destroyAllWindows()