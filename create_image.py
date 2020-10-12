import cv2
import numpy as np

src1 = cv2.imread('input.jpg')
src2 = cv2.imread('mask.png')
src2 = cv2.resize(src2, src1.shape[1::-1])
dst = cv2.bitwise_and(src1, src2)
dst[np.where((dst == [0, 0, 0]).all(axis=2))] = [0, 0, 255]
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imwrite("result.jpg", dst)
