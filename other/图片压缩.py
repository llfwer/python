# coding=utf-8

import os

from PIL import Image


# 功能：博客图片生成缩略图，1280横屏压缩，1000竖屏压缩
# 参数：图片名称
# 返回：OK，保存同名文件在thumb目录下
def thumbnail_image(path, file_name):
    im = Image.open(os.path.join(path, file_name))
    print('格式', im.format, '，分辨率', im.size, '，色彩', im.mode)
    if max(im.size[0], im.size[1]) > 1000:
        if im.size[0] > im.size[1]:
            im.thumbnail((1280, 1280))
        else:
            im.thumbnail((1000, 1000))
        im.save(get_thumbnail_path(path, file_name), 'JPEG', quality=90)
    return 'OK'


def get_thumbnail_path(path, file_name):
    thumb_path = os.path.join(path, 'thumbnail')
    if not os.path.exists(thumb_path):
        os.makedirs(thumb_path)
    return os.path.join(thumb_path, file_name)


def get_all_jpg(path):
    file_list = os.listdir(path)
    for i in file_list:
        file_path = os.path.join(path, i)
        if os.path.isfile(file_path) and i.endswith('.jpg'):
            thumbnail_image(path, i)


get_all_jpg('D:\\')

# # 全处理
# OutCheck = map(JfzBlogImgThumb, imgname)
# print(list(OutCheck))
