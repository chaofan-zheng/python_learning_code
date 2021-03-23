# 04_channel_oper.py
# 色彩通道操作
import cv2

# 读取图像
im = cv2.imread("../test_img/opencv2.png")
cv2.imshow("im", im)

# 通过切片取出其中一个通道
b = im[:, :, 0] # 索引为0的即蓝色通道
cv2.imshow("b", b)

# 抹掉蓝色通道
im[:, :, 0] = 0
cv2.imshow("im-b0", im)

cv2.waitKey()
cv2.destroyAllWindows()