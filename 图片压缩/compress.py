import os

import tinify

# https://tinypng.com/ LuoLianFeng 272389862@qq.com 每个月免费500次请求
tinify.key = "XHHxNfx3MSGS4WgFbYWJFr2YJxGLlVsb"


def compress_image(file_path):
    # 获取文件夹路径，文件后缀名
    (dir_name, file_full_name) = os.path.split(file_path)
    (file_name, file_ext) = os.path.splitext(file_full_name)

    print('compress', file_full_name, 'start...')

    source = tinify.from_file(file_path)

    # 先保存到临时文件
    temp_path = os.path.join(dir_name, 'temp' + file_ext)
    source.to_file(temp_path)

    # 临时文件覆盖源文件
    os.remove(file_path)
    os.rename(temp_path, file_path)

    print('compress', file_full_name, 'complete.')


def find_images_folder(path):
    if not os.path.isdir(path):
        return None

    dirs = os.listdir(path)

    for item in dirs:
        if item == 'images':
            return os.path.join(path, item)
    return None


def compress_folder(path):
    dirs = os.listdir(path)

    print(path)

    for item in dirs:
        compress_image(os.path.join(path, item))


def check_path(path):
    dirs = os.listdir(path)

    for item in dirs:
        folder = find_images_folder(os.path.join(path, item))

        if folder is not None:
            compress_folder(folder)


def main():
    check_path(r"C:\Users\ROWE\Desktop\hello")


if __name__ == '__main__':
    main()
