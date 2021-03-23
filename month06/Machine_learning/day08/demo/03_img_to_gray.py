# 03_img_to_gray.py
# 彩色图像转换为灰度图像示例
import cv2

im = cv2.imread("../test_img/Linus.png", 1)
cv2.imshow("im", im)

# 彩色图像(BGR --> Gray)
im_gray = cv2.cvtColor(im,# 原图
                       cv2.COLOR_BGR2GRAY)#转换方式
cv2.imshow("im_gray", im_gray)

cv2.waitKey()
cv2.destroyAllWindows()