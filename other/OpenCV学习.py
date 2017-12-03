import random

import cv2
import numpy as np


# 显示图像
def show_image():
    img = cv2.imread('../data/stinkbug.png')
    cv2.imshow('image', img)
    key = cv2.waitKey(20000)
    if key == 27:
        cv2.destroyAllWindows()
    elif key == ord('s'):
        cv2.imwrite('../data/test.png', img)
        cv2.destroyAllWindows()


# 显示灰度化图像
def show_gray_image():
    img = cv2.imread('../data/women.jpg', cv2.CV_8UC3)
    # 可选参数CV_LOAD_IMAGE_COLOR (BGR), CV_LOAD_IMAGE_GRAYSCALE (grayscale), CV_LOAD_IMAGE_UNCHANGED(neither)
    cv2.imshow('image', img)
    cv2.waitKey(20000)


# 图像属性
def show_image_property():
    img = cv2.imread('../data/women.jpg')
    print(type(img.shape), ' : ', img.shape)
    print(type(img.size), ' : ', img.size)
    # 在debug的时候，dtype很重要
    print(type(img.dtype), ' : ', img.dtype)


# 绘制文本
def draw_text():
    img = cv2.imread('../data/women.jpg')  # Load the image
    font = cv2.FONT_HERSHEY_TRIPLEX  # Creates a font
    x = int(img.shape[1] / 8)  # x position of the text
    y = int(img.shape[0] / 2)  # y position of the text
    # 八个参数，图片、字符串、坐标、字体、字号、颜色数组、线宽、线条种类
    cv2.putText(img, "Hello World !", (x, y), font, 1, (255, 255, 255), 4, cv2.LINE_AA)  # Draw the text
    cv2.imshow('image', img)  # Show the image
    cv2.waitKey(10000)


# 图像缩放
def resize_image():
    img = cv2.imread('../data/women.jpg')
    height, width = img.shape[:2]
    res = cv2.resize(img, (int(width / 2), int(height / 2)), interpolation=cv2.INTER_CUBIC)
    cv2.imshow('image', res)
    cv2.waitKey(10000)


# 图像平移
def translate_image():
    img = cv2.imread('../data/women.jpg')
    height, width = img.shape[:2]
    M = np.float32([[1, 0, 100], [0, 1, 50]])
    dst = cv2.warpAffine(img, M, (width, height))
    cv2.imshow('img', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 图像旋转
def rotate_image():
    img = cv2.imread('../data/women.jpg')
    rows, cols = img.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
    dst = cv2.warpAffine(img, M, (cols, rows))
    cv2.imshow('image', dst)
    cv2.waitKey(0)


# 仿射变换
def affinity_image():
    img = cv2.imread('../data/women.jpg')
    rows, cols, ch = img.shape
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    M = cv2.getAffineTransform(pts1, pts2)
    dst = cv2.warpAffine(img, M, (cols, rows))
    cv2.imshow('image', dst)
    cv2.waitKey(0)


# 图像灰度等处理
def color_change_image():
    img = cv2.imread('../data/women.jpg')
    if len(img.shape) == 3 or len(img.shape) == 4:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img
    cv2.imshow("origin", img)
    cv2.imshow("cvtColor", gray)
    cv2.waitKey(0)


# 识别图像中的指定区间颜色
def recognition_color():
    frame = cv2.imread('../data/women.jpg')
    # 将图片从 BGR 空间转换到 HSV 空间
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 定义在HSV空间中蓝色的范围
    upper_blue = np.array([245, 225, 214])
    lower_blue = np.array([52, 37, 40])
    # 根据以上定义的蓝色的阈值得到蓝色的部分
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.waitKey(0)


# 通道分离
def pass_split():
    img = cv2.imread('../data/women.jpg')
    b, g, r = cv2.split(img)
    merge = cv2.merge((b, g, r))
    cv2.imshow('origin', img)
    cv2.imshow('r', r)
    cv2.imshow('g', g)
    cv2.imshow('b', b)
    cv2.imshow('merge', merge)
    cv2.waitKey(0)


# 图片边框
def copy_make_border():
    BLUE = [255, 0, 0]
    img = cv2.imread('../data/women.jpg')
    replicate = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REPLICATE)
    reflect = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT)
    reflect101 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_REFLECT_101)
    wrap = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_WRAP)
    constant = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=BLUE)
    cv2.imshow('origin', img)
    cv2.imshow('replicate', replicate)
    cv2.imshow('reflect', reflect)
    cv2.imshow('reflect101', reflect101)
    cv2.imshow('wrap', wrap)
    cv2.imshow('constant', constant)
    cv2.waitKey(0)


# 滤镜
def filter_image():
    img = cv2.imread('../data/women.jpg')
    cv2.imshow('origin', img)
    # 灰度
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imshow('gray', gray)
    # 图像均值平滑滤波
    blurred = np.hstack([cv2.blur(img, (3, 3)), cv2.blur(img, (5, 5)), cv2.blur(img, (7, 7))])
    cv2.imshow('blurred', blurred)
    # 图像中值滤波
    median = np.hstack([cv2.medianBlur(img, 3), cv2.medianBlur(img, 5), cv2.medianBlur(img, 7)])
    cv2.imshow('median', median)
    # 图像高斯平滑滤波
    gaussian = np.hstack([cv2.GaussianBlur(img, (3, 3), 0), cv2.GaussianBlur(img, (5, 5), 0), cv2.GaussianBlur(img, (7, 7), 0)])
    cv2.imshow('gaussian', gaussian)
    # 图像双边滤波
    bilateral = np.hstack([cv2.bilateralFilter(img, 5, 21, 21), cv2.bilateralFilter(img, 7, 31, 31), cv2.bilateralFilter(img, 9, 41, 41)])
    cv2.imshow('bilateral', bilateral)
    cv2.waitKey(0)


# 均衡处理、灰度化、二值化
def gray_two():
    img = cv2.imread('../data/women.jpg')
    cv2.imshow('origin', img)
    # 灰度
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imshow('gray', gray)
    # 均衡处理
    equalize = cv2.equalizeHist(gray)
    cv2.imshow('equalize', equalize)
    # 二值化处理
    binary = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow('binary', binary)
    inv = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY_INV)[1]
    cv2.imshow('inv', inv)
    trunc = cv2.threshold(img, 100, 255, cv2.THRESH_TRUNC)[1]
    cv2.imshow('trunc', trunc)
    to_zero = cv2.threshold(img, 100, 255, cv2.THRESH_TOZERO)[1]
    cv2.imshow('to_zero', to_zero)
    to_zero_inv = cv2.threshold(img, 100, 255, cv2.THRESH_TOZERO_INV)[1]
    cv2.imshow('to_zero_inv', to_zero_inv)
    cv2.waitKey(0)


# HighGUI
def high_gui():
    img = cv2.imread('../data/women.jpg')

    def change(val):
        binary = cv2.threshold(img, val, 255, cv2.THRESH_BINARY)[1]
        cv2.imshow('image', binary)

    change(100)
    cv2.createTrackbar("Thresh", "image", 100, 255, change)
    cv2.waitKey(0)


# 选区操作
def select_operation():
    img = cv2.imread('../data/women.jpg')
    roil_img = img[200:300, 0:200]
    # 高斯模糊
    gray_roil_img = cv2.blur(roil_img, (5, 5))
    img[0:100, 0:200] = gray_roil_img
    cv2.imshow('image', img)
    cv2.waitKey(0)


# 运算
def arithmetic():
    img1 = cv2.imread('../data/women.jpg')[0:200, 0:200]
    img2 = cv2.imread('../data/stinkbug.png')[0:200, 0:200]
    add = cv2.add(img1, img2)
    cv2.imshow('add', add)
    diff = cv2.absdiff(img1, img2)
    cv2.imshow('diff', diff)
    power = cv2.pow(img1, 2)
    cv2.imshow('power', power)
    cv2.waitKey(0)


# 像素遍历
def pixel_ergodic():
    img = cv2.imread('../data/women.jpg')
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i, j] = img[i, j] + 30
    cv2.imshow('image', img)
    cv2.waitKey(0)


# 像素随机变化
def pixel_random():
    img = cv2.imread('../data/women.jpg')
    for k in range(5000):
        i = random.randint(0, img.shape[0] - 1)
        j = random.randint(0, img.shape[1] - 1)
        color = (random.randrange(256), random.randrange(256), random.randrange(256))
        img[i, j] = color
    cv2.imshow('image', img)
    cv2.waitKey(0)


# 创建空白图像
def create_empty_image():
    img = np.zeros((500, 500, 3), np.uint8)
    cv2.putText(img, "Hello World !", (200, 200), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), 4, cv2.LINE_AA)  # Draw the text
    cv2.imshow('image', img)
    cv2.waitKey(0)


# 绘制直方图
def draw_hist_image():
    def calc_and_draw_hist(image, color):
        hist = cv2.calcHist([image], [0], None, [256], [0.0, 255.0])
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
        histImg = np.zeros([256, 256, 3], np.uint8)
        hpt = int(0.9 * 256)
        for h in range(256):
            intensity = int(hist[h] * hpt / maxVal)
            cv2.line(histImg, (h, 256), (h, 256 - intensity), color)
        return histImg

    img = cv2.imread('../data/women.jpg')
    b, g, r = cv2.split(img)

    histImgB = calc_and_draw_hist(b, [255, 0, 0])
    histImgG = calc_and_draw_hist(g, [0, 255, 0])
    histImgR = calc_and_draw_hist(r, [0, 0, 255])

    cv2.imshow("histImgB", histImgB)
    cv2.imshow("histImgG", histImgG)
    cv2.imshow("histImgR", histImgR)
    cv2.imshow("Img", img)
    cv2.waitKey(0)


# 绘制直方图2
def draw_hist_image2():
    img = cv2.imread('../data/women.jpg')
    h = np.zeros((256, 256, 3))  # 创建用于绘制直方图的全0图像

    bins = np.arange(256).reshape(256, 1)  # 直方图中各bin的顶点位置
    color = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # BGR三种颜色
    for ch, col in enumerate(color):
        originHist = cv2.calcHist([img], [ch], None, [256], [0, 256])
        cv2.normalize(originHist, originHist, 0, 255 * 0.9, cv2.NORM_MINMAX)
        hist = np.int32(np.around(originHist))
        pts = np.column_stack((bins, hist))
        cv2.polylines(h, [pts], False, col)


# 反向投影
def reverse_projection():
    # roi图片，就想要找的的图片
    roi = cv2.imread('../data/in.png')
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    # 目标搜索图片
    target = cv2.imread('../data/whole.png')
    hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)

    # 计算目标直方图
    roihist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
    # 归一化，参数为原图像和输出图像，归一化后值全部在2到255范围
    cv2.normalize(roihist, roihist, 0, 255, cv2.NORM_MINMAX)
    dst = cv2.calcBackProject([hsvt], [0, 1], roihist, [0, 180, 0, 256], 1)

    # 卷积连接分散的点
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dst = cv2.filter2D(dst, -1, disc)

    ret, thresh = cv2.threshold(dst, 50, 255, 0)
    # 使用merge变成通道图像
    thresh = cv2.merge((thresh, thresh, thresh))

    # 蒙板
    res = cv2.bitwise_and(target, thresh)
    # 矩阵按列合并,就是把target,thresh和res三个图片横着拼在一起
    res = np.hstack((target, thresh, res))

    cv2.imwrite('res.jpg', res)
    # 显示图像
    cv2.imshow('1', res)
    cv2.waitKey(0)


reverse_projection()
