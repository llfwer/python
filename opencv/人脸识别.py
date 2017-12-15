import cv2

# 人脸识别
import numpy as np


def face_test():
    img = cv2.imread('data/face.jpg')

    # load detection file (various files for different views and uses)
    cascade = cv2.CascadeClassifier("data/haarcascade_frontalface_alt.xml")

    # preprocessing, as suggested by: http://www.bytefish.de/wiki/opencv/object_detection
    # img_copy = cv2.resize(img, (img.shape[1]/2, img.shape[0]/2))
    # gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
    # gray = cv2.equalizeHist(gray)

    # detect objects, return as list
    rects = cascade.detectMultiScale(img)

    # get a list of rectangles
    for x, y, width, height in rects:
        cv2.rectangle(img, (x, y), (x + width, y + height), (0, 0, 255), 1)
    # display!
    cv2.imshow('origin', img)
    cv2.waitKey(0)


def demo():
    cap = cv2.VideoCapture("data/women.mp4")

    def process(image):
        grey1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        grey = cv2.equalizeHist(grey1)
        keypoints = get_points(grey, grey1)
        # print keypoints

        # print image.shape
        if keypoints is not None and len(keypoints) > 0:
            for x, y in keypoints:
                cv2.circle(image, (int(x + 200), y), 3, (255, 255, 0))
        return image

    # p=cv2.imread('1.png')
    # p2=process(p)

    # cv2.imshow('my',p2)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    while (cap.isOpened()):
        ret, frame = cap.read()
        frame = process(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.waitKey(0)


def get_points(imag, input1):
    mask1 = np.zeros_like(input1)
    x = 0
    y = 0
    w1, h1 = input1.shape
    # print 666
    # print input1.shape
    input1 = input1[0:w1, 200:h1]
    # print input1.shape
    try:
        w, h = imag.shape

        # w=w/2
        # h=h/2
        # print w,h
    except:
        return None

    mask1[y:y + h, x:x + w] = 255

    keypoints = list()

    # kp=cv2.goodFeaturesToTrack(input1,
    # mask1,
    # **paras)
    # input1=input1.fromarray
    kp = cv2.goodFeaturesToTrack(input1, 200, 0.04, 7)

    # cv2.goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance)
    if kp is not None and len(kp) > 0:
        for x, y in np.float32(kp).reshape(-1, 2):
            keypoints.append((x, y))
    return keypoints


# GoodFeaturesToTrack函数追踪图像里的关键点
def track():
    img = cv2.imread('data/rect.png')
    grey1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grey = cv2.equalizeHist(grey1)
    keypoints = get_points(grey, grey1)
    # print keypoints

    # print image.shape
    if keypoints is not None and len(keypoints) > 0:
        for x, y in keypoints:
            cv2.circle(img, (int(x + 200), y), 3, (255, 255, 0))
    cv2.imshow('image', img)
    cv2.waitKey(0)


demo()
