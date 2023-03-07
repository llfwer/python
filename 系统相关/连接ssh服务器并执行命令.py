# coding:utf-8

import datetime as dt
import os
import stat
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
# 本地文件目录
loc_dir = 'C:\\Users\\ROWE\\Desktop\\新建文件夹\\com'
# 远程文件目录
rem_dir = '/home/upchina/com'


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


def exe_cmd_line(ssh, cmd_line):
    stdin, stdout, stderr = ssh.exec_command(cmd_line)

    # 获取命令结果
    res, err = stdout.read(), stderr.read()
    if err:
        raise Exception(err.decode('utf-8'))
    else:
        print(res.decode('utf-8'))


def exe_cmd(rem_file):
    # 创建SSH对象
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(host, port, username=username, password=password)

    try:
        print('pwd')
        exe_cmd_line(ssh, 'pwd')
        print('rm -rf com')
        exe_cmd_line(ssh, 'rm -rf com')

        print('/usr/local/taf/cpp/tools/jce2android ' + rem_file)
        exe_cmd_line(ssh, '/usr/local/taf/cpp/tools/jce2android ' + rem_file)
    except Exception as e1:
        ssh.close()
        raise e1

    ssh.close()


def get_remote_files(sftp, remote_dir):
    # 加载sftp服务器文件对象(根目录)
    files_attr = sftp.listdir_attr(remote_dir)
    try:
        # foreach遍历
        for file_attr in files_attr:
            # 判断是否为目录
            if stat.S_ISDIR(file_attr.st_mode):
                # 1.当是文件夹时
                # 计算子文件夹在ftp服务器上的路径
                son_remote_dir = remote_dir + '/' + file_attr.filename
                # 生成器, 迭代调用函数自身
                yield from get_remote_files(sftp, son_remote_dir)
            else:
                # 2.当是文件时
                # 生成器, 添加"路径+文件名"到迭代器"
                yield remote_dir + '/' + file_attr.filename

    except Exception as e:
        print('get_remote_files exception:', e)


def download_file(local_dir, remote_dir):
    t = paramiko.Transport((host, port))
    t.connect(username=username, password=password)

    sftp = paramiko.SFTPClient.from_transport(t)

    # 记录下载开始时间
    dt_start = dt.datetime.now()
    print('................. {} 开始下载!..................\n'.format(dt_start))

    # 判断输入的本地目录是否存在
    if not os.path.exists(local_dir):
        # 若本地目录不存在,则创建该目录
        os.makedirs(local_dir)

    # 实例化生成器, 获取sftp指定目录下的所有文件路径
    files = get_remote_files(sftp, remote_dir)

    # foreach遍历
    for file in files:
        # 要下载的远程文件, 本地时路径+文件名
        remote_file_name = file
        # 定义下载保存到本地时的路径+文件名
        local_file_name = os.path.join(local_dir, file.split('/')[-1])

        try:
            # 下载文件, 本地已有同名文件则覆盖
            sftp.get(remote_file_name, local_file_name)
            print('sftp服务器文件 {} 下载成功!\n该文件保存本地位置是 {} !\n'.format(remote_file_name, local_file_name))
        except Exception as e:
            print('%s下载出错!:\n' % remote_file_name, e)
            # 下载失败, 关闭连接
            sftp.close()

    # 下载成功, 关闭连接
    sftp.close()
    t.close()

    # 记录下载结束时间
    dt_end = dt.datetime.now()
    print('..................... {} 下载完成!..................'.format(dt_end))
    # 记录下载时长
    dt_long = dt_end - dt_start
    print('................ 本次下载共用时间 {} !...............\n'.format(dt_long))


def delete_remote_dir():
    # 创建SSH对象
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(host, port, username=username, password=password)

    try:
        print('pwd')
        exe_cmd_line(ssh, 'pwd')
        print('rm -rf com')
        exe_cmd_line(ssh, 'rm -rf com')
    except Exception as e1:
        ssh.close()
        raise e1

    ssh.close()


def main(argv=None):
    if argv is None:
        argv = sys.argv
    if argv[1] is not None:
        loc_file = argv[1]
        rem_file = '/home/upchina/temp' + '/' + loc_file.split('\\')[-1]
        print('-------------------------------------------\n')
        print('loc_file={},\nrem_file={}\n'.format(loc_file, rem_file))
        try:
            # 上传jce文件
            upload_file(loc_file, rem_file)

            # 执行命令
            exe_cmd(rem_file)

            # 下载文件
            download_file(loc_dir, rem_dir)

            # 删除远程目录
            delete_remote_dir()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
