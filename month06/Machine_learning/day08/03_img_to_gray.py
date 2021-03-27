# 去掉彩色图像
import cv2

im = cv2.imread('../DeepLearning/dataset/data/Linus.png',
                1)  # 1表示读取成灰色头像，0表示读取成灰色头像
print(im.shape)  # 高度、宽度、通道数

# 彩色图像是BGR的，先蓝色通道
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)  # 转换方式，对颜色的处理一般都是这个cvt函数

cv2.imshow("im",  # 窗体名称，如果重复，后面会覆盖前面
           im_gray)  # 图像数据
cv2.waitKey()  # 阻塞函数，防止直接窗体一闪而过。任意敲一个键就有返回值
cv2.destroyAllWindows()  # 销毁所有创建的窗体
