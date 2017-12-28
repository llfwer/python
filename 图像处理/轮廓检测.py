import cv2


# FindContours 轮廓检测
def find_contours():
    img = cv2.imread('data/contours.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 灰度图像二值化
    gray = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)[1]
    # findContours计算轮廓
    contours = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]
    # 移除宽高过小的轮廓
    for i in contours[:]:
        if i.size < 5:
            contours.remove(i)
    # 画轮廓
    cv2.drawContours(img, contours, -1, (0, 0, 255), 2)  # 最后一个参数若为-1:cv2.FILLED表示填充模式

    pentagram = contours[1]  # 第二条轮廓是五角星
    # 计算五角星的X轴极值点
    leftmost = tuple(pentagram[:, 0][pentagram[:, :, 0].argmin()])
    rightmost = tuple(pentagram[:, 0][pentagram[:, :, 0].argmax()])
    cv2.circle(img, leftmost, 2, (255, 0, 0), 3)
    cv2.circle(img, rightmost, 2, (255, 0, 0), 3)
    # 计算五角星的Y轴极值点
    topmost = tuple(pentagram[:, 0][pentagram[:, :, 1].argmin()])
    bottommost = tuple(pentagram[:, 0][pentagram[:, :, 1].argmax()])
    cv2.circle(img, topmost, 2, (0, 255, 0), 3)
    cv2.circle(img, bottommost, 2, (0, 255, 0), 3)

    cv2.imshow('img', img)
    cv2.waitKey(0)


find_contours()
