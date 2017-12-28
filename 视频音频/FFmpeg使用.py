import subprocess


# http://blog.csdn.net/u010106759/article/details/52662252

# 从视频获取帧
def get_frame():
    path = '../图像处理/data/women.mp4'
    strcmd = "ffmpeg -i " + path + " -r 10 -f image2 " + "data/%06d.jpg"
    subprocess.call(strcmd, shell=True)


get_frame()
