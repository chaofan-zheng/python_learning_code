# 色彩通道操作
import cv2

# 省略掉1就是默认彩色
im = cv2.imread('../DeepLearning/dataset/data/opencv2.png')
print(im)  # 一个三维数组
cv2.imshow('im', im)
# 通过切片操作取出其中一个通道
b = im[:, :, 0]  # 即蓝色通道
cv2.imshow('b', b)

# 抹掉蓝色通道
im[:, :, 0] = 0
cv2.imshow('im~b0', im)

cv2.waitKey()  # 阻塞函数，防止直接窗体一闪而过。任意敲一个键就有返回值
cv2.destroyAllWindows()  # 销毁所有创建的窗体
# ?为什么会这样？
# 单通道的图片一律按灰度图像来处理
