# 06_binary_demo.py
# 二值化与反二值化处理
import cv2

im = cv2.imread("../test_img/lena.jpg", 0)
cv2.imshow("im", im)

# 二值化处理
t, im_bin = cv2.threshold(im, # 原图
                          127, # 阈值
                          255, # 最大值
                          cv2.THRESH_BINARY)#二值化
cv2.imshow("im_bin",  im_bin)

# 返二值化
t, im_bin2 = cv2.threshold(im,
                           127, 255,
                           cv2.THRESH_BINARY_INV)#反二值化
cv2.imshow("im_bin2", im_bin2)

cv2.waitKey()
cv2.destroyAllWindows()