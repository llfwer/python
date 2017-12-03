import cv2
import numpy as np
from matplotlib import pyplot as plt


# 拉普拉斯检测
def laplace_test():
    img = cv2.imread('data/edge.jpg')
    lap = cv2.Laplacian(img, cv2.CV_16S)  # 拉普拉斯边缘检测
    lap = np.uint8(np.absolute(lap))  # 对lap去绝对值

    plt.figure(figsize=(18, 10))
    plt.subplot(1, 2, 1), plt.imshow(img), plt.title('origin')
    plt.subplot(1, 2, 2), plt.imshow(lap), plt.title('laplace')
    plt.xticks([]), plt.yticks([])

    plt.show()


# Soble边缘检测
def soble_test():
    img = cv2.imread('data/edge.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)  # x方向的梯度
    sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1)  # y方向的梯度
    sx = np.uint8(np.absolute(sx))  # x方向梯度的绝对值
    sy = np.uint8(np.absolute(sy))  # y方向梯度的绝对值
    combine = cv2.bitwise_or(sx, sy)

    plt.figure(figsize=(18, 10))
    plt.subplot(2, 3, 1), plt.imshow(img), plt.title('origin')
    plt.subplot(2, 3, 2), plt.imshow(gray), plt.title('gray')
    plt.subplot(2, 3, 3), plt.imshow(sx), plt.title('sx')
    plt.subplot(2, 3, 4), plt.imshow(sy), plt.title('sy')
    plt.subplot(2, 3, 5), plt.imshow(combine), plt.title('combine')
    plt.xticks([]), plt.yticks([])

    plt.show()


# Canny边缘检测
def canny_test():
    img = cv2.imread('data/edge.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny_img = cv2.Canny(gray, 30, 150)

    plt.figure(figsize=(18, 10))
    plt.subplot(1, 2, 1), plt.imshow(img), plt.title('origin')
    plt.subplot(1, 2, 2), plt.imshow(canny_img), plt.title('canny')
    plt.xticks([]), plt.yticks([])

    plt.show()


# Laplace 算法
def laplace():
    img = cv2.imread('data/edge.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Laplace on origin
    lap_origin = cv2.Laplacian(img, cv2.CV_16S)  # 拉普拉斯边缘检测
    lap_origin = np.uint8(np.absolute(lap_origin))  # 对lap去绝对值
    # Laplace on a gray scale picture
    lap_gray = cv2.Laplacian(gray, cv2.CV_16S)  # 拉普拉斯边缘检测
    lap_gray = np.uint8(np.absolute(lap_gray))  # 对lap去绝对值
    # Laplace on color
    r, g, b = cv2.split(img)
    lap_r = cv2.Laplacian(r, cv2.CV_16S)
    lap_r = np.uint8(np.absolute(lap_r))
    lap_g = cv2.Laplacian(g, cv2.CV_16S)
    lap_g = np.uint8(np.absolute(lap_g))
    lap_b = cv2.Laplacian(b, cv2.CV_16S)
    lap_b = np.uint8(np.absolute(lap_b))
    lap_color = cv2.merge([lap_r, lap_g, lap_b])
    # 灰度轮廓二值化
    gray_threshold = cv2.threshold(lap_gray, 50, 255, cv2.THRESH_BINARY_INV)[1]
    cv2.imshow('laplace_origin', lap_origin)
    cv2.imshow('laplace_gray', lap_gray)
    cv2.imshow('laplace_color', lap_color)
    cv2.imshow('gray_threshold', gray_threshold)
    cv2.waitKey(0)


# Sobel 算法
def sobel():
    img = cv2.imread('data/edge.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)  # x方向的梯度
    sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1)  # y方向的梯度
    sx = np.uint8(np.absolute(sx))  # x方向梯度的绝对值
    sy = np.uint8(np.absolute(sy))  # y方向梯度的绝对值
    combine = cv2.bitwise_or(sx, sy)  # 合并
    threshold = cv2.threshold(combine, 100, 255, cv2.THRESH_BINARY_INV)[1]  # 轮廓二值化
    cv2.imshow('origin', img)
    cv2.imshow('gray', gray)
    cv2.imshow('sobel', combine)
    cv2.imshow('threshold', threshold)
    cv2.waitKey(0)


# 形态学
def morphology():
    img = cv2.imread('data/edge.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 定义结构元素，图像膨胀、侵蚀、开闭运算用
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
    # 腐蚀图像
    eroded = cv2.erode(gray, kernel)
    # 膨胀图像
    dilated = cv2.dilate(gray, kernel)
    # 获取轮廓
    open_close = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
    # 轮廓二值化
    threshold = cv2.threshold(open_close, 30, 255, cv2.THRESH_BINARY_INV)[1]
    cv2.imshow('origin', img)
    cv2.imshow('gray', gray)
    cv2.imshow('eroded', eroded)
    cv2.imshow('dilated', dilated)
    cv2.imshow('open_close', open_close)
    cv2.imshow('threshold', threshold)
    cv2.waitKey(0)


# Canny 算法
def canny():
    img = cv2.imread('data/canny.jpg', cv2.IMREAD_GRAYSCALE)
    # 获取轮廓
    canny_img = cv2.Canny(img, 200, 200)
    # 复制多维数组，用作画线
    canny_dst = np.copy(canny_img)
    # hough变换检测直线
    lines = cv2.HoughLines(canny_img, 1, np.pi / 180, 100)
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
        cv2.line(canny_dst, (x1, y1), (x2, y2), (255, 255, 0), 1)

    cv2.imshow('origin', img)
    cv2.imshow('canny_img', canny_img)
    cv2.imshow('canny_dst', canny_dst)
    cv2.waitKey(0)


# FindContours 轮廓检测
def find_contours():
    img = cv2.imread('data/edge.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 灰度图像二值化
    gray = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)[1]
    # 定义结构元素，图像膨胀、侵蚀、开闭运算用
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    # 获取轮廓
    opened = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)
    # 轮廓二值化
    closed = cv2.threshold(closed, 128, 255, cv2.THRESH_BINARY_INV)[1]
    # findContours计算轮廓
    contours = cv2.findContours(closed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours[1], -1, (0, 0, 255), 3)

    cv2.imshow('img', img)
    cv2.waitKey(0)


# Harris 角点检测
def harris():
    img = cv2.imread('data/edge.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    # 输入图像必须是float32，最后一个参数在0.04 到0.05 之间
    dst = cv2.cornerHarris(gray, 2, 3, 0.04)
    # result is dilated for marking the corners, not important
    dst = cv2.dilate(dst, None)
    # Threshold for an optimal value, it may vary depending on the image.
    img[dst > 0.01 * dst.max()] = [0, 0, 255]

    cv2.imshow('img', img)
    cv2.waitKey(0)


harris()
