# 09_img_crop_demo.py
# 图像裁剪
import numpy as np
import cv2


# 图像随机裁剪
def random_crop(im, w, h):
    # 随机产生裁剪起始位置
    start_x = np.random.randint(0, im.shape[1])
    start_y = np.random.randint(0, im.shape[0])
    # 切片操作
    new_img = im[start_y:start_y + h,
              start_x:start_x + w]
    return new_img


def center_crop(im, w, h):
    # 随机产生裁剪起始位置
    start_x = int(im.shape[1] / 2) - int(w / 2)
    start_y = int(im.shape[0] / 2) - int(h / 2)

    # 切片操作
    new_img = im[start_y:start_y + h,
              start_x:start_x + w]
    return new_img


if __name__ == "__main__":
    im = cv2.imread("../test_img/banana_1.png")
    # 裁剪
    new_img1 = random_crop(im, 200, 200)  # 随机裁剪
    new_img2 = center_crop(im, 200, 200)#中心裁剪

    cv2.imshow("random_crop", new_img1)
    cv2.imshow("center_crop", new_img2)

    cv2.waitKey()
    cv2.destroyAllWindows()
