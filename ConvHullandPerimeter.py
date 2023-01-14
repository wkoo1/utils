import cv2
import numpy as np

img = cv2.imread('D:/oukai/crazy/mycode/unet++-Camus/miou_out/detection-results/patient0001_4CH_ES.png')
ret,thresh = cv2.threshold(img,0,10,0)

_,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#得到轮廓信息

#情况一，传入list，元素是numpy数组，函数将会画出相邻两点之间的连线
imgnew = cv2.drawContours(img, contours, 1, (0,255,0), 3)#第三个参数是1，代表了取出contours中index为1的array
cv2.imshow('contour',imgnew)

#情况二，传入numpy数组，函数将仅仅会画出这些点，而不会将他们依次连接
imgnew = cv2.drawContours(img, contours[1], -1, (0,255,0), 3)#第三个参数为-1，代表了画出contours[0]中所有的点
cv2.imshow('contour',imgnew)
