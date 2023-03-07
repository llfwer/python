# coding:utf-8

import datetime as dt
import os
import sys

import paramiko

# 服务器ip
host = '172.16.8.152'
# 端口
port = 22
# 用户名
username = 'upchina'
# 密码
password = 'upchina333'
# 远程文件目录
rem_dir = '/home/upchina/temp'


def upload_file(file_path, target_path):
    t = paramiko.Transport((host, port))
    t.connect(username=username, password=password)

    sftp = paramiko.SFTPClient.from_transport(t)

    # 记录下载开始时间
    dt_start = dt.datetime.now()
    print('................. {} 开始上传!..................\n'.format(dt_start))

    # 判断文件是否存在
    if os.path.exists(target_path):
        # 若文件存在,则删除
        os.remove(target_path)

    try:
        # 下载文件, 本地已有同名文件则覆盖
        sftp.put(file_path, target_path)
        print('上传文件 {} 成功!\n该文件保存远程位置是 {} !\n'.format(file_path, target_path))
    except Exception as e:
        print('%s上传出错!:\n' % target_path, e)
        # 上传失败, 关闭连接
        sftp.close()

    # 上传成功, 关闭连接
    sftp.close()
    t.close()

    # 记录下载结束时间
    dt_end = dt.datetime.now()
    print('..................... {} 上传完成!..................'.format(dt_end))
    # 记录下载时长
    dt_long = dt_end - dt_start
    print('................ 本次上传共用时间 {} !...............\n'.format(dt_long))


def main(argv=None):
    if argv is None:
        argv = sys.argv
    if argv[1] is not None:
        loc_file = argv[1]
        rem_file = rem_dir + '/' + loc_file.split('\\')[-1]
        print('loc_file={},\nrem_file={}\n'.format(loc_file, rem_file))
        try:
            # 上传jce文件
            upload_file(loc_file, rem_file)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
