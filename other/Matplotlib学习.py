import matplotlib.image as mpimg
import numpy as np
import pylab
from matplotlib import pyplot as plt


# 绘制三角曲线
def l_trigonometric():
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)  # 获取采样数组
    C, S = np.cos(X), np.sin(X)  # 计算得出cos数组和sin数组
    plt.plot(X, C)  # 载入cos数组
    plt.plot(X, S)  # 载入sin数组
    plt.show()


# 绘制三角曲线
def l_trigonometric_more():
    # 设置图像大小为8x6, 像素密度为80
    plt.figure(figsize=(8, 6), dpi=80)
    # 创建子图，1x1，在第一个位置，创建子图要在plot.plot()前面
    plt.subplot(1, 1, 1)
    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C, S = np.cos(X), np.sin(X)
    # 用蓝色的线，宽度为1.0来绘制cos函数
    plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-", label="cosine")
    # 用绿色的线，宽度为1.0来绘制sin函数
    plt.plot(X, S, color="green", linewidth=1.0, linestyle="-", label="sine")
    # 添加图例
    plt.legend(loc='upper left')
    # 设置x轴的上下限
    plt.xlim(-4.0, 4.0)
    # 设置x轴的坐标
    plt.xticks(np.linspace(-4, 4, 9, endpoint=True))
    # Set y limits
    plt.ylim(-1.0, 1.0)
    # Set y ticks
    plt.yticks(np.linspace(-1, 1, 5, endpoint=True))
    # 保存图片，像素密度为72
    # plt.savefig("exercice_2.png", dpi=72)
    # 获取存在的轴心位置
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    # 在屏幕上显示出来
    plt.show()


# 绘制直方图
def l_histogram():
    n = 12
    X = np.arange(n)
    Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
    plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
    for x, y in zip(X, Y1):
        plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
    plt.ylim(-1.25, +1.25)
    plt.show()


# 绘制离散图
def l_discrete():
    n = 1024
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)
    plt.scatter(X, Y)
    plt.show()


# 绘制复杂曲线
def l_curve():
    X = np.arange(-10, 10, 0.1)
    plt.plot(X, X ** 2 + 10 * np.sin(X))
    plt.show()


# 图像处理
def l_image():
    img = mpimg.imread('data/stinkbug.png')
    # 从单通道模拟彩色图像
    # lum_img = img[:, :, 0]
    imshow = plt.imshow(img)
    # 改变 colormap
    # imshow.set_cmap('hot')
    pylab.show()


l_image()
