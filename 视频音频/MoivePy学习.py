import random

from moviepy.editor import *


def deal_replace_voice():
    path = '../图像处理/data'
    name = 'women'
    video = VideoFileClip(r"{}/{}.mp4".format(path, name), audio=False)
    v_duration = video.duration  # 视频时间长短
    s_d = 0
    v_d = v_duration
    audio_n = AudioFileClip(r"data/test.mp3")
    audio = audio_n.subclip(s_d + 20, v_d + s_d + 20)
    v_w, v_h = video.size  # 视频长宽
    h__w = v_h / v_w
    if v_h == v_w:
        # 正方形的剪成规定尺寸
        video = video.subclip(s_d, v_d + s_d).resize((1280, 1280))
        video = video.crop(y_center=640, height=720)
    elif h__w == 0.5625:
        video = video.subclip(s_d, v_d + s_d).resize((1280, 720))
    elif v_h / v_w < 0.5625:
        # 不符合比例的，先resize，然后再crop裁剪
        video = video.subclip(s_d, v_d + s_d).resize(height=720)
        video = video.crop(x1=0, width=1280, y1=0, height=720)
    elif v_h / v_w > 0.5625:
        video = video.subclip(s_d, v_d + s_d).resize(width=1280)
        video = video.crop(y_center=video.size[1] / 2, height=720)
    result = CompositeVideoClip([video]).set_audio(audio)
    # 保存文件
    result.write_videofile(r"data/{}_30.mp4".format(name), fps=25)
    # 再拿result流裁剪，不用再重新打开文件。
    video_5 = result.subclip(4, random.randint(8, 9))
    result_5 = CompositeVideoClip([video_5])
    result_5.write_videofile(r"data/{}_5.mp4".format(name), fps=25, codec=None)
    # 关闭视频流
    video.reader.close()
    del video.reader


deal_replace_voice()
