# 08_resize_demo.py
# 图像缩放
import cv2

im = cv2.imread("../test_img/Linus.png")
cv2.imshow("im", im)

# 缩小
h, w = im.shape[:2]  # 取高度,宽度
dst_size = (int(w / 2), int(h / 2))
im_resized1 = cv2.resize(im, dst_size)  # 缩小
cv2.imshow("im_resized1", im_resized1)

# 放大: 最邻近插值
dst_size = (200, 300)
im_resized2 = cv2.resize(
    im,
    dst_size,
    interpolation=cv2.INTER_NEAREST)#最邻近插值
cv2.imshow("im_resized2", im_resized2)

im_resized3 = cv2.resize(
    im,
    dst_size,
    interpolation=cv2.INTER_LINEAR)#双线性插值
cv2.imshow("im_resized3", im_resized3)

cv2.waitKey()
cv2.destroyAllWindows()
