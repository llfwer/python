import subprocess


def get_app_pid(package):
    pid = ''

    adb_proc = subprocess.Popen(['adb', 'shell', 'ps -ef | grep ' + package], stdout=subprocess.PIPE)
    while True:
        line = adb_proc.stdout.readline().strip().decode("utf-8")
        if line != '':
            if 'grep' in line:
                continue
            split_line = line.split()
            if len(split_line) < 8:
                continue
            if split_line[7] != package:
                continue
            pid = split_line[1]
            break
        else:
            break

    return pid


def get_app_uid(pid):
    uid = ''

    adb_proc = subprocess.Popen(['adb', 'shell', 'cat /proc/' + pid + '/status'], stdout=subprocess.PIPE)
    while True:
        line = adb_proc.stdout.readline().strip().decode("utf-8")
        if line != '':
            if not line.startswith("Uid:"):
                continue
            split_line = line.split()
            if len(split_line) < 5:
                continue
            uid = split_line[1]
            break
        else:
            break

    return uid


pid = get_app_pid('com.upchina.teach')
print('pid:' + pid)
uid = get_app_uid(pid)
print('uid:' + uid)
