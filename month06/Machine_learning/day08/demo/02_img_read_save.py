# 01_img_read_save.py
# 图像读取, 显示, 保存
import cv2

im = cv2.imread("../test_img/Linus.png", # 图像路径
                1) # 1-彩色图像 0-灰度图像
print(type(im)) # 打印类型: ndarray
print(im.shape) # 打印图像形状
# 显示
cv2.imshow("im", # 窗体名称(如果重复,后面会覆盖前面)
           im) # 图像数据, imread的返回值
# 保存
cv2.imwrite("Linus_new.png", # 保存的图片路径
            im)# 图像数据

cv2.waitKey() # 等待用户敲击按键(阻塞函数)
cv2.destroyAllWindows() # 销毁所有创建的窗体