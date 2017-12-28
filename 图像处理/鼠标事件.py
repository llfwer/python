import cv2
import numpy as np


def move_draw():
    img = np.zeros((512, 512, 3), np.uint8)

    def draw_circle(event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE:
            cv2.circle(img, (x, y), 10, (255, 0, 0), -1)

    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_circle)
    while True:
        cv2.imshow('image', img)
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()


def check_event():
    img = np.zeros((512, 512, 3), np.uint8)
    left_status = 4

    def draw_circle(event, x, y, flags, param):
        global left_status
        if event == 1 or event == 4:
            left_status = event
        if left_status == 1 and event == 0:
            cv2.circle(img, (x, y), 10, (255, 0, 0), -1)

    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_circle)
    while True:
        cv2.imshow('image', img)
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()


check_event()
