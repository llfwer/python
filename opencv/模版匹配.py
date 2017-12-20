import time

import cv2
import numpy as np
from matplotlib import pyplot as plt


def template_match():
    img = cv2.imread("data/whole.png", 0)
    img2 = img.copy()
    template = cv2.imread("data/sub.png", 0)
    w, h = template.shape[::-1]
    # 6 中匹配效果对比算法
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
               'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    for meth in methods:
        img = img2.copy()

        method = eval(meth)

        res = cv2.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        cv2.rectangle(img, top_left, bottom_right, 255, 2)

        plt.figure(meth)
        plt.subplot(221), plt.imshow(img2, cmap="gray")
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(222), plt.imshow(template, cmap="gray")
        plt.title('template Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(223), plt.imshow(res, cmap="gray")
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(224), plt.imshow(img, cmap="gray")
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.show()


def template_match2():
    # 加载原始RGB图像
    img_rgb = cv2.imread("data/whole.png")
    # 创建一个原始图像的灰度版本，所有操作在灰度版本中处理，然后在RGB图像中使用相同坐标还原
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    # 加载将要搜索的图像模板
    template = cv2.imread('data/sub.png', 0)
    # 记录图像模板的尺寸
    w, h = template.shape[::-1]

    # 使用matchTemplate对原始灰度图像和图像模板进行匹配
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    # 设定阈值
    threshold = 0.7
    # res大于70%
    loc = np.where(res >= threshold)

    # 使用灰度图像中的坐标对原始RGB图像进行标记
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7, 249, 151), 2)
    # 显示图像
    cv2.imshow('Detected', img_rgb)
    cv2.waitKey(0)


def template_match3(source_image, template_image, method, threshold, show_image):
    """
        :param source_image:原图
        :param template_image:模版
        :param method:匹配模式
        :param threshold:阈值
        :param show_image:是否绘制结果
    """
    start = int(round(time.time() * 1000))
    # 加载原始RGB图像
    img_rgb = cv2.imread(source_image)
    # 创建一个原始图像的灰度版本，所有操作在灰度版本中处理，然后在RGB图像中使用相同坐标还原
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    # 加载将要搜索的图像模板
    template = cv2.imread(template_image, 0)
    # 记录图像模板的尺寸
    w, h = template.shape[::-1]

    # 使用matchTemplate对原始灰度图像和图像模板进行匹配
    res = cv2.matchTemplate(img_gray, template, method)
    # res大于70%
    loc = np.where(res >= threshold)
    # 是否成功匹配
    success = len(list(zip(*loc[::-1]))) > 0

    if show_image:
        # 使用灰度图像中的坐标对原始RGB图像进行标记
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7, 249, 151), 2)
        # 显示图像
        cv2.imshow('Detected', img_rgb)
        cv2.waitKey(0)

    print('花费时间 : ', int(round(time.time() * 1000)) - start, 'ms')
    return success


print(template_match3('data/whole.png', 'data/sub.png', cv2.TM_CCOEFF_NORMED, 0.7, True))


def filter_matches(kp1, kp2, matches, ratio=0.75):
    mkp1, mkp2 = [], []
    for m in matches:
        if len(m) == 2 and m[0].distance < m[1].distance * ratio:
            m = m[0]
            mkp1.append(kp1[m.queryIdx])
            mkp2.append(kp2[m.trainIdx])
    p1 = np.float32([kp.pt for kp in mkp1])
    p2 = np.float32([kp.pt for kp in mkp2])
    kp_pairs = zip(mkp1, mkp2)
    return p1, p2, kp_pairs


def explore_match(win, img1, img2, kp_pairs, status=None, H=None):
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    vis = np.zeros((max(h1, h2), w1 + w2), np.uint8)
    vis[:h1, :w1] = img1
    vis[:h2, w1:w1 + w2] = img2
    vis = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)

    if H is not None:
        corners = np.float32([[0, 0], [w1, 0], [w1, h1], [0, h1]])
        corners = np.int32(cv2.perspectiveTransform(corners.reshape(1, -1, 2), H).reshape(-1, 2) + (w1, 0))
        cv2.polylines(vis, [corners], True, (255, 255, 255))

    if status is None:
        status = np.ones(len(kp_pairs), np.bool)
    p1 = np.int32([kpp[0].pt for kpp in kp_pairs])
    p2 = np.int32([kpp[1].pt for kpp in kp_pairs]) + (w1, 0)

    green = (0, 255, 0)
    red = (0, 0, 255)
    white = (255, 255, 255)
    kp_color = (51, 103, 236)
    for (x1, y1), (x2, y2), inlier in zip(p1, p2, status):
        if inlier:
            col = green
            cv2.circle(vis, (x1, y1), 2, col, -1)
            cv2.circle(vis, (x2, y2), 2, col, -1)
        else:
            col = red
            r = 2
            thickness = 3
            cv2.line(vis, (x1 - r, y1 - r), (x1 + r, y1 + r), col, thickness)
            cv2.line(vis, (x1 - r, y1 + r), (x1 + r, y1 - r), col, thickness)
            cv2.line(vis, (x2 - r, y2 - r), (x2 + r, y2 + r), col, thickness)
            cv2.line(vis, (x2 - r, y2 + r), (x2 + r, y2 - r), col, thickness)
    vis0 = vis.copy()
    for (x1, y1), (x2, y2), inlier in zip(p1, p2, status):
        if inlier:
            cv2.line(vis, (x1, y1), (x2, y2), green)

    cv2.imshow(win, vis)


def match():
    img1 = cv2.imread('data/whole.png')
    img2 = cv2.imread('data/sub.png')
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT()
    kp1, des1 = sift.detectAndCompute(img1_gray, None)
    kp2, des2 = sift.detectAndCompute(img2_gray, None)
    # BFmatcher with default parms
    bf = cv2.BFMatcher(cv2.NORM_L2)
    matches = bf.knnMatch(des1, des2, k=2)
    p1, p2, kp_pairs = filter_matches(kp1, kp2, matches, ratio=0.5)
    explore_match('matches', img1_gray, img2_gray, kp_pairs)
    # img3 = cv2.drawMatchesKnn(img1_gray,kp1,img2_gray,kp2,good[:10],flag=2)
    cv2.waitKey(0)

# match()
