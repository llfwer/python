import cv2
import scipy as sp


# SIFT计算并画出特征点
def sift_key_points():
    img = cv2.imread('data/screen.png')
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(gray, None)
    cv2.drawKeypoints(image=img, outImage=img, keypoints=kp1, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
                      color=(51, 163, 236))
    cv2.imshow('image', img)
    cv2.waitKey(0)


# SURF计算并画出特征点
def surf_key_points():
    img = cv2.imread('data/screen.png')
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    sift = cv2.xfeatures2d.SURF_create()
    kp1, des1 = sift.detectAndCompute(gray, None)
    cv2.drawKeypoints(image=img, outImage=img, keypoints=kp1, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
                      color=(51, 163, 236))
    cv2.imshow('image', img)
    cv2.waitKey(0)


# BFMatcher匹配图像
def bf_match():
    img1 = cv2.imread('data/message.png', 0)  # queryImage
    img2 = cv2.imread('data/screen.png', 0)  # trainImage

    # Initiate SIFT detector
    orb = cv2.xfeatures2d.SIFT_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

    # Match descriptors.
    matches = bf.match(des1, des2)

    # Sort them in the order of their distance.
    matches = sorted(matches, key=lambda x: x.distance)

    # visualization
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    view = sp.zeros((max(h1, h2), w1 + w2, 3), sp.uint8)
    view[:h1, :w1, 0] = img1
    view[:h2, w1:, 0] = img2
    view[:, :, 1] = view[:, :, 0]
    view[:, :, 2] = view[:, :, 0]

    # Draw first 10 matches.
    cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], view, flags=2)

    cv2.imshow('image', view)
    cv2.waitKey(0)


# BFMatcher匹配图像
def bf_knn_match():
    img1 = cv2.imread('data/message.png', 0)  # queryImage
    img2 = cv2.imread('data/screen.png', 0)  # trainImage

    # Initiate SIFT detector
    orb = cv2.xfeatures2d.SIFT_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # BFMatcher with default params
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    # Apply ratio test
    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append([m])

    # visualization
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    view = sp.zeros((max(h1, h2), w1 + w2, 3), sp.uint8)
    view[:h1, :w1, 0] = img1
    view[:h2, w1:, 0] = img2
    view[:, :, 1] = view[:, :, 0]
    view[:, :, 2] = view[:, :, 0]

    # cv2.drawMatchesKnn expects list of lists as matches.
    cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, view, flags=2)

    cv2.imshow('image', view)
    cv2.waitKey(0)


# FLANNMatcher匹配图像
def flann_match():
    img1 = cv2.imread('data/message.png', 0)  # queryImage
    img2 = cv2.imread('data/screen.png', 0)  # trainImage

    # Initiate SIFT detector
    orb = cv2.xfeatures2d.SIFT_create()

    # find the keypoints and descriptors with SIFT
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # FLANN parameters
    index_params = dict(algorithm=0, trees=5)
    search_params = dict(checks=50)  # or pass empty dictionary

    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    # Need to draw only good matches, so create a mask
    matchesMask = [[0, 0] for i in range(len(matches))]

    # ratio test as per Lowe's paper
    for i, (m, n) in enumerate(matches):
        if m.distance < 0.7 * n.distance:
            matchesMask[i] = [1, 0]

    draw_params = dict(matchColor=(0, 255, 0), singlePointColor=(255, 0, 0), matchesMask=matchesMask, flags=0)

    # visualization
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    view = sp.zeros((max(h1, h2), w1 + w2, 3), sp.uint8)
    view[:h1, :w1, 0] = img1
    view[:h2, w1:, 0] = img2
    view[:, :, 1] = view[:, :, 0]
    view[:, :, 2] = view[:, :, 0]

    # cv2.drawMatchesKnn expects list of lists as matches.
    cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches, view, **draw_params)

    cv2.imshow('image', view)
    cv2.waitKey(0)


def image_distinguish1():
    img1 = cv2.imread('data/message.png', 0)  # queryImage
    img2 = cv2.imread('data/screen.png', 0)  # trainImage
    # Initiate SIFT detector
    sift = cv2.xfeatures2d.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    # FLANN parameters
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)  # or pass empty dictionary
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)
    print('matches...', len(matches))
    # Apply ratio test
    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append(m)
    print('good', len(good))
    # #####################################
    # visualization
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    view = sp.zeros((max(h1, h2), w1 + w2, 3), sp.uint8)
    view[:h1, :w1, 0] = img1
    view[:h2, w1:, 0] = img2
    view[:, :, 1] = view[:, :, 0]
    view[:, :, 2] = view[:, :, 0]
    for m in good:
        # draw the keypoints
        # print m.queryIdx, m.trainIdx, m.distance
        color = tuple([sp.random.randint(0, 255) for _ in range(3)])
        # print 'kp1,kp2',kp1,kp2
        cv2.line(view, (int(kp1[m.queryIdx].pt[0]), int(kp1[m.queryIdx].pt[1])),
                 (int(kp2[m.trainIdx].pt[0] + w1), int(kp2[m.trainIdx].pt[1])), color)
    cv2.imshow("view", view)
    cv2.waitKey()


def image_distinguish():
    img1 = cv2.imread('data/message.png', 0)  # queryImage
    img2 = cv2.imread('data/screen.png', 0)  # trainImage
    # Initiate SIFT detector
    sift = cv2.xfeatures2d.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    # FLANN parameters
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)  # or pass empty dictionary
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)
    print('matches...', len(matches))
    # Apply ratio test
    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append(m)
    print('good', len(good))
    # #####################################
    # visualization
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    view = sp.zeros((max(h1, h2), w1 + w2, 3), sp.uint8)
    view[:h1, :w1, 0] = img1
    view[:h2, w1:, 0] = img2
    view[:, :, 1] = view[:, :, 0]
    view[:, :, 2] = view[:, :, 0]
    for m in good:
        # draw the keypoints
        # print m.queryIdx, m.trainIdx, m.distance
        color = tuple([sp.random.randint(0, 255) for _ in range(3)])
        # print 'kp1,kp2',kp1,kp2
        cv2.line(view, (int(kp1[m.queryIdx].pt[0]), int(kp1[m.queryIdx].pt[1])),
                 (int(kp2[m.trainIdx].pt[0] + w1), int(kp2[m.trainIdx].pt[1])), color)
    cv2.imshow("view", view)
    cv2.waitKey()


image_distinguish()
