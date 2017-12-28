import cv2
import numpy as np


# http://www.linuxidc.com/Linux/2015-01/111962.htm

# 已知四角坐标手动抠图
def get_image_in_image():
    img = cv2.imread('data/rect.png')
    corners = np.float32([[331, 147], [632, 253], [365, 657], [11, 433]])
    canvas = np.float32([[0, 0], [636, 0], [636, 846], [0, 846]])
    # 投影变换
    M = cv2.getPerspectiveTransform(corners, canvas)
    # 矫正
    result = cv2.warpPerspective(img, M, (0, 0))
    cv2.imshow('origin', img)
    cv2.imshow('result', result)
    cv2.waitKey(0)


# 动态检测边界，再抠图
def get_image_in_image2():
    img = cv2.imread('data/rect.png')
    # 滤波降噪
    img = cv2.pyrMeanShiftFiltering(img, 25, 10)
    # Canny检测边缘
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny_img = cv2.Canny(gray, 30, 150)
    cv2.imshow('origin', img)
    cv2.imshow('canny_img', canny_img)
    cv2.waitKey(0)


get_image_in_image2()
