# 07_affine_demo.py
# 图像仿射变换(旋转,平移)
import cv2
import numpy as np

def translate(im, x, y):
    """
    平移
    :param im: 原图
    :param x: 水平方向移动的值
    :param y: 垂直方向移动的值
    :return: 经过平移后的图像
    """
    h, w = im.shape[:2] # 取图像高度,宽度
    # 定义平移矩阵
    M = np.float32([[1, 0, x],
                    [0, 1, y]])
    # 使用平移矩阵执行仿射变换
    shifted = cv2.warpAffine(im, # 原图
                             M,# 变换矩阵
                             (w, h))# 输出图像大小
    return shifted


def rotate(im, angle, center=None, scale=1.0):
    """
    图像旋转
    :param im: 原图
    :param angle: 角度
    :param center: 中心
    :param scale: 缩放比率
    :return: 经过旋转的图像
    """
    h, w = im.shape[:2] # 取出图像高度,宽度

    if center is None:
        center = (w / 2, h / 2) # 计算原图中心
    # 生成旋转矩阵
    M = cv2.getRotationMatrix2D(center, # 中心
                                angle,# 角度
                                scale)# 缩放比率
    rotated = cv2.warpAffine(im, M, (w, h))
    return rotated



if __name__ == "__main__":
    im = cv2.imread("../test_img/Linus.png")
    cv2.imshow("im", im)

    # 平移
    im_shifted = translate(im, 40, 60)
    cv2.imshow("im_shifted", im_shifted)

    # 旋转
    im_rotated = rotate(im, -45)
    cv2.imshow("im_rotated", im_rotated)

    cv2.waitKey()
    cv2.destroyAllWindows()







