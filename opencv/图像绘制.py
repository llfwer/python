import cv2
import numpy as np


def draw_line():
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def draw_rectangle():
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def draw_circle():
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def draw_ellipse():
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def draw_polylines():
    img = np.zeros((512, 512, 3), np.uint8)
    pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    img = cv2.polylines(img, [pts], True, (0, 255, 255))
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def draw_text():
    img = np.zeros((512, 512, 3), np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def nothing(x):
    pass


def palette():
    # Create a black image, a window
    img = np.zeros((300, 512, 3), np.uint8)
    cv2.namedWindow('image')

    # create trackbars for color change
    cv2.createTrackbar('R', 'image', 0, 255, nothing)
    cv2.createTrackbar('G', 'image', 0, 255, nothing)
    cv2.createTrackbar('B', 'image', 0, 255, nothing)

    # create switch for ON/OFF functionality
    switch = '0 : OFF \n1 : ON'
    cv2.createTrackbar(switch, 'image', 0, 1, nothing)

    while True:
        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        # get current positions of four trackbars
        r = cv2.getTrackbarPos('R', 'image')
        g = cv2.getTrackbarPos('G', 'image')
        b = cv2.getTrackbarPos('B', 'image')
        s = cv2.getTrackbarPos(switch, 'image')

        if s == 0:
            img[:] = 0
        else:
            img[:] = [b, g, r]

    cv2.destroyAllWindows()


palette()
