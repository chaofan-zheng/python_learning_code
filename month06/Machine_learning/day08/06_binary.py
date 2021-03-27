# 二值化与反二值化

import cv2

im = cv2.imread("../DeepLearning/dataset/data/lena.jpg", 0)
cv2.imshow("orig", im)

t, im_bin = cv2.threshold(im,
                          127,  # 阈值
                          255,  # 最大值
                          cv2.THRESH_BINARY)
cv2.imshow("threshold", im_bin)
# 用在主体图像的提取，把无关紧要的地方去掉
t1, im_bin_inv = cv2.threshold(im,
                               127,  # 阈值
                               255,  # 最大值
                               cv2.THRESH_BINARY_INV)
cv2.imshow("threshold_inv", im_bin_inv)
cv2.waitKey()
cv2.destroyAllWindows()
