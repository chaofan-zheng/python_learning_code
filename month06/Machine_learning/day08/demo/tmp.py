from scipy import misc
from scipy import signal
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import scipy.ndimage as sn
import cv2
import pylab

im = cv2.imread("../test_img/zebra.png", 0)

flt = np.array([[-1, 0, 1],
                [-2, 0, 2],
                [-1, 0, 1]]) / 2
flt2 = np.array([[1, 2, 1],
                 [0, 0, 0],
                 [-1, -2, -1]]) / 2

conv_img1 = cv2.filter2D(im, -1, flt, borderType=1)
conv_img2 = cv2.filter2D(im, -1, flt2, borderType=1)

cv2.imshow("im", im)
cv2.imshow("conv_img1", conv_img1)
cv2.imshow("conv_img2", conv_img2)
cv2.waitKey()
cv2.destroyAllWindows()
