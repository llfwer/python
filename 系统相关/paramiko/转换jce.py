# coding:utf-8

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
rem_dir = '/home/upchina/temp'
# 执行文件路径
exe_file = '/usr/local/taf/cpp/tools/jce2android'


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
        print('rm -rf ' + rem_dir + '/com')
        exe_cmd_line(ssh, 'rm -rf ' + rem_dir + '/com')

        print(exe_file + ' --dir=' + rem_dir + ' ' + rem_file)
        exe_cmd_line(ssh, exe_file + ' --dir=' + rem_dir + ' ' + rem_file)
    except Exception as e1:
        ssh.close()
        raise e1

    ssh.close()


def main(argv=None):
    if argv is None:
        argv = sys.argv
    if argv[1] is not None:
        loc_file = argv[1]
        rem_file = rem_dir + '/' + loc_file.split('\\')[-1]
        print('-------------------------------------------\n')
        print('loc_file={},\nrem_file={}\n'.format(loc_file, rem_file))
        try:
            # 执行命令
            exe_cmd(rem_file)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
