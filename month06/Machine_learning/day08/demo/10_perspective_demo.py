# 10_perspective_demo.py
# 透视变换示例
import cv2
import numpy as np

im = cv2.imread("../test_img/pers.png")
h, w = im.shape[:2] # 取高度,宽度

# 定义透视变换源点, 目标点
pts1 = np.float32(
    [[58, 2], [167, 9], [8, 196], [126, 196]])# 输入图像四个顶点坐标
pts2 = np.float32(
    [[16, 2], [167, 8], [8, 196], [169, 196]])# 输出图像四个顶点坐标

# 生成透视变换矩阵
M = cv2.getPerspectiveTransform(pts1, # 源坐标点
                                pts2) # 目标坐标点
print(M) # 3*3矩阵

# 透视变换
dst = cv2.warpPerspective(im, # 原图
                          M, # 变换矩阵
                          (w, h))#输出图像宽度/高度

# 将矩形变换为平行四边形
M = cv2.getPerspectiveTransform(pts2, # 源坐标点
                                pts1) # 目标坐标点
dst2 = cv2.warpPerspective(dst,# 第一次变换后的图像
                           M,
                           (w, h))

cv2.imshow("im", im)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey()
cv2.destroyAllWindows()