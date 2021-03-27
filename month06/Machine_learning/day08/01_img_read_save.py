# 图像读取，显示，保存
import cv2

im = cv2.imread('../DeepLearning/dataset/data/Linus.png',
                1)  # 1表示读取成灰色头像，0表示读取成灰色头像
print(type(im))  # 打印类型： ndarry
print(im.shape)  # 高度、宽度、通道数

cv2.imshow("im",  # 窗体名称，如果重复，后面会覆盖前面
           im)  # 图像数据
cv2.imwrite("Linus_new.png",  # 保存文件的路径
            im)
cv2.waitKey()  # 阻塞函数，防止直接窗体一闪而过。任意敲一个键就有返回值
cv2.destroyAllWindows()  # 销毁所有创建的窗体
