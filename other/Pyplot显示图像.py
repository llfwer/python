# -*-coding:utf8-*-
import matplotlib.image as mpimg  # mpimg 用于读取图片
import matplotlib.pyplot as plt  # plt 用于显示图片
import numpy as np
from PIL import Image


def open_with_pil():
    img = Image.open('E:\\我的图片\\QQ图片20170914200717.jpg')
    img.show()


def open_with_pyplot():
    lena = mpimg.imread('E:\\我的图片\\QQ图片20170914200717.jpg')
    lena_1 = lena[:, :, 0]
    # 热量图
    # plt.imshow(lena_1)
    # plt.show()
    # 灰度图
    # plt.imshow(lena_1, cmap='Greys_r')
    # plt.show()
    # 或者
    gray = np.dot(lena[..., :3], [0.299, 0.587, 0.114])
    plt.imshow(gray, cmap='Greys_r')  # 也可以用 plt.imshow(gray, cmap = plt.get_cmap('gray'))
    plt.show()


open_with_pyplot()
