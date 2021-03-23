# 11_erode_demo.py
# 图像腐蚀(边沿向内收缩)
import cv2
import numpy as np

im = cv2.imread("../test_img/5.png")
cv2.imshow("im", im)
# 腐蚀 
kernel = np.ones((3, 3), np.uint8)#计算核
im_erode = cv2.erode(im, # 原图
                     kernel, # 计算核
                     iterations=3)#迭代次数
cv2.imshow("im_erode", im_erode)

cv2.waitKey()
cv2.destroyAllWindows()