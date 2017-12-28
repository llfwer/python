from queue import Queue

import cv2
# 播放mp4文件
import numpy as np


def gray_mp4():
    try:
        cap = cv2.VideoCapture('data/test.mp4')
    except IOError as e:
        print(e)
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()


# 显示摄像头内容
def operation_camera():
    try:
        cap = cv2.VideoCapture(0)
    except IOError as e:
        print(e)
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            return

            # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


# 从摄像头录制视频
def from_camera_write_avi():
    try:
        cap = cv2.VideoCapture(0)
    except IOError as e:
        print(e)
        return

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('data/output.avi', fourcc, 20.0, (640, 480))
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            frame = cv2.flip(frame, 0)

            # write the flipped frame
            out.write(frame)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()


# 处理mp4，检测轮廓
def outline_mp4():
    try:
        cap = cv2.VideoCapture('data/test.mp4')
    except IOError as e:
        print(e)
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 获取轮廓
            canny = cv2.Canny(gray, 125, 350)
            # 灰度轮廓二值化
            threshold = cv2.threshold(canny, 50, 255, cv2.THRESH_BINARY_INV)[1]
            cv2.imshow('frame', gray)
            cv2.imshow('threshold', threshold)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()


# 从摄像头检测轮廓
def outline_camera():
    try:
        cap = cv2.VideoCapture(0)
    except IOError as e:
        print(e)
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 高斯降噪
            gray = cv2.GaussianBlur(gray, (3, 3), 0)
            # 获取轮廓
            canny = cv2.Canny(gray, 125, 350)
            # 灰度轮廓二值化
            threshold = cv2.threshold(canny, 128, 255, cv2.THRESH_BINARY_INV)[1]
            cv2.imshow('frame', gray)
            cv2.imshow('threshold', threshold)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()


# 处理mp4，人脸识别
def face_mp4():
    try:
        cap = cv2.VideoCapture('data/women.mp4')
    except IOError as e:
        print(e)
        return

    cascade = cv2.CascadeClassifier("data/haarcascade_frontalface_alt.xml")
    index = 1

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            if index % 3 == 0:  # 跳帧
                rects = cascade.detectMultiScale(frame)
                for x, y, width, height in rects:
                    cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 1)
                cv2.imshow('frame', frame)
            index = index + 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()


# 角点光流轨迹跟踪
def lucas_kanade():
    try:
        cap = cv2.VideoCapture('data/women.mp4')
    except IOError as e:
        print(e)
        return

    # 设置 ShiTomasi 角点检测的参数
    feature_params = dict(maxCorners=100,
                          qualityLevel=0.3,
                          minDistance=7,
                          blockSize=7)

    # 设置 lucas kanade 光流场的参数
    # maxLevel 为使用图像金字塔的层数
    lk_params = dict(winSize=(15, 15),
                     maxLevel=2,
                     criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

    # 产生随机的颜色值
    color = np.random.randint(0, 255, (100, 3))

    # 获取第一帧，并寻找其中的角点
    ret, old_frame = cap.read()
    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
    p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

    # 创建一个掩膜为了后面绘制角点的光流轨迹
    mask = np.zeros_like(old_frame)

    while True:
        ret, frame = cap.read()
        if ret:
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # 计算能够获取到的角点的新位置
            p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

            # 选取好的角点，并筛选出旧的角点对应的新的角点
            good_new = p1[st == 1]
            good_old = p0[st == 1]

            # 绘制角点的轨迹
            for i, (new, old) in enumerate(zip(good_new, good_old)):
                a, b = new.ravel()
                c, d = old.ravel()
                cv2.line(mask, (a, b), (c, d), color[i].tolist(), 2)
                cv2.circle(frame, (a, b), 5, color[i].tolist(), -1)

            img = cv2.add(frame, mask)

            cv2.imshow("frame", img)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break

            # 更新当前帧和当前角点的位置
            old_gray = frame_gray.copy()
            p0 = good_new.reshape(-1, 1, 2)

        else:
            break

    cv2.destroyAllWindows()
    cap.release()


# 目标跟踪
def capture_camera_object():
    # 捕获视频图像
    camera = cv2.VideoCapture(0)
    # 打开摄像头，将第一帧作为整个输入背景
    es = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
    kernel = np.ones((5, 5), np.uint8)
    background = None

    while True:
        ret, frame = camera.read()
        # 对背景帧进行灰度和平滑处理
        if background is None:
            background = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            background = cv2.GaussianBlur(background, (21, 21), 0)
            continue
        # 将其他帧进行灰度处理和模糊平滑处理
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)
        # 计算其他帧与背景之间的差异，得到一个差分图
        diff = cv2.absdiff(background, gray_frame)
        # 应用阈值得到一副黑白图像，并通过dilate膨胀图像，从而对孔和缺陷进行归一处理
        diff = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
        diff = cv2.dilate(diff, es, iterations=2)

        # 显示矩形框，在计算出的差分图中找到所有的白色斑点轮廓，并显示轮廓
        image, cnts, hierarchy = cv2.findContours(diff.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for c in cnts:
            if cv2.contourArea(c) < 1500:
                continue
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)

        cv2.imshow("contours", frame)
        cv2.imshow("dif", diff)
        if cv2.waitKey(int(1000 / 12)) & 0xff == ord("q"):
            break

    cv2.destroyAllWindows()
    camera.release()


# meanshift目标跟踪
def meanshift_capture():
    cap = cv2.VideoCapture(0)
    # 获取第一帧
    ret, frame = cap.read()
    print(frame.shape)
    # 设置初始跟踪对象的窗口大小
    # r,h,c,w = 120,100,253,100
    r, h, c, w = 180, 80, 140, 90
    track_window = (c, r, w, h)

    cv2.rectangle(frame, (c, r), (c + w, r + h), 255, 2)
    cv2.imshow("frame", frame)
    cv2.waitKey(0)
    # 设置感兴趣的区域
    roi = frame[r:r + h, c:c + w]
    # cv2.imshow("roi",roi)
    # cv2.waitKey(0)
    hsv_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_roi, np.array((0., 0., 32.)), np.array((180., 255., 255.)))
    roi_hist = cv2.calcHist([hsv_roi], [0], None, [180], [0, 180])
    cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

    term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

    while True:
        ret, frame = cap.read()

        if ret is True:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

            # 调用meanshift获取新的位置
            ret, track_window = cv2.meanShift(dst, track_window, term_crit)

            # 画出它的位置
            x, y, w, h = track_window

            cv2.rectangle(frame, (x, y), (x + w, y + h), 255, 2)
            cv2.imshow("frame", frame)

            k = cv2.waitKey(60) & 0xff
            if k == 27:
                break
            # else:
            #    cv2.imwrite(chr(k)+".jpg",frame)

        else:
            break

    cv2.destroyAllWindows()
    cap.release()


# 运动方向判断
def move_test():
    camera = cv2.VideoCapture(0)
    width = int(camera.get(3))
    height = int(camera.get(4))

    first_frame = None
    lastDec = None
    firstThresh = None

    feature_params = dict(maxCorners=100,
                          qualityLevel=0.3,
                          minDistance=7,
                          blockSize=7)

    lk_params = dict(winSize=(15, 15),
                     maxLevel=2,
                     criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

    color = np.random.randint(0, 255, (100, 3))
    num = 0

    q_x = Queue(maxsize=10)
    q_y = Queue(maxsize=10)

    while True:
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if first_frame is None:
            first_frame = gray
            continue

        # 对两帧图像进行 absdiff 操作
        frame_delta = cv2.absdiff(first_frame, gray)
        # diff 之后的图像进行二值化
        thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
        # 下面的是几种不同的二值化的方法，感觉对我来说效果都差不多
        # thresh = cv2.adaptiveThreshold(frameDelta,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
        # cv2.THRESH_BINARY,11,2)
        # thresh = cv2.adaptiveThreshold(frameDelta,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
        #           cv2.THRESH_BINARY,11,2)
        thresh = cv2.dilate(thresh, None, iterations=2)
        # 识别角点
        p0 = cv2.goodFeaturesToTrack(thresh, mask=None, **feature_params)
        if p0 is not None:
            x_sum = 0
            y_sum = 0
            for i, old in enumerate(p0):
                x, y = old.ravel()
                x_sum += x
                y_sum += y
            # 计算出所有角点的平均值
            x_avg = x_sum / len(p0)
            y_avg = y_sum / len(p0)

            # 写入固定长度的队列
            if q_x.full():
                # 如果队列满了，就计算这个队列中元素的增减情况
                qx_list = list(q_x.queue)
                key = 0
                diffx_sum = 0
                for item_x in qx_list:
                    key += 1
                    if key < 10:
                        # 下一个元素减去上一个元素
                        diff_x = item_x - qx_list[key]
                        diffx_sum += diff_x
                # 加和小于0，表明队列中的元素在递增
                if diffx_sum < 0:
                    print("left")
                    cv2.putText(frame, "some coming form left", (100, 100), 0, 0.5, (0, 0, 255), 2)
                else:
                    print("right")

                print(x_avg)
                q_x.get()
            q_x.put(x_avg)
            cv2.putText(frame, str(x_avg), (300, 100), 0, 0.5, (0, 0, 255), 2)
            frame = cv2.circle(frame, (int(x_avg), int(y_avg)), 5, color[i].tolist(), -1)

        cv2.imshow("Security Feed", frame)
        first_frame = gray.copy()
        if cv2.waitKey(int(1000 / 12)) & 0xff == ord("q"):
            break

    frame.release()
    cv2.destroyAllWindows()


move_test()
