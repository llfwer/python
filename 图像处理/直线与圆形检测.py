import cv2
import numpy as np


# 检测直线
def hough_lines():
    img = cv2.imread('data/house.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 获取轮廓
    edges = cv2.Canny(gray, 200, 200)
    # hough变换检测直线
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 260)
    lines1 = lines[:, 0, :]  # 提取为为二维
    for rho, theta in lines1[:]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)
        cv2.line(img, (x1, y1), (x2, y2), (255, 255, 0), 1)

    cv2.imshow('canny_img', edges)
    cv2.imshow('origin', img)
    cv2.waitKey(0)


# 概率直线检测
def hough_lines_p():
    img = cv2.imread('data/house.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 获取轮廓
    edges = cv2.Canny(gray, 200, 200)
    # hough变换检测直线
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 30, minLineLength=60, maxLineGap=10)
    lines1 = lines[:, 0, :]  # 提取为为二维
    for x1, y1, x2, y2 in lines1[:]:
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 1)

    cv2.imshow('canny_img', edges)
    cv2.imshow('origin', img)
    cv2.waitKey(0)


# 圆形检测
def hough_circles():
    img = cv2.imread('data/circle.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 获取轮廓
    edges = cv2.Canny(gray, 200, 200)
    #
    circles1 = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=50, minRadius=100, maxRadius=200)
    circles = circles1[0, :, :]  # 提取为二维
    circles = np.uint16(np.around(circles))  # 四舍五入，取整
    for i in circles[:]:
        cv2.circle(img, (i[0], i[1]), i[2], (255, 0, 0), 5)  # 画圆
        cv2.circle(img, (i[0], i[1]), 2, (255, 0, 255), 10)  # 画圆心

    cv2.imshow('canny_img', edges)
    cv2.imshow('origin', img)
    cv2.waitKey(0)


hough_circles()
