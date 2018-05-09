import os
import shutil
import sys
import time
import zipfile

apk_version = "5.3.2"  # 注意这里，每次需要把这个版本号改成我们所期望的
src_fileName = "source.apk"  # 读取我们打包好的apk文件
target_dir = os.path.abspath('.')
channel_file = open("channel.txt")  # 打开包含渠道名称的文件


def write_channel_to_apk(filename, channel_name):
    z = zipfile.ZipFile(filename, 'a', zipfile.ZIP_DEFLATED)
    empty_channel_file = "META-INF/channel_{channel}".format(channel=channel_name)
    target_file = "channel.apk"
    z.write(target_file, empty_channel_file)
    z.close()
    print("Write channel to apk channel " + channel_name + " , " + filename + "\n")


def copy_file(src_path, file_name):
    target_path = target_dir + os.path.sep + file_name
    if os.path.exists(src_path) and not os.path.exists(target_path):
        shutil.copy(src_path, target_path)


def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


if not os.path.exists(src_fileName):
    print("sourcefile " + src_fileName + " not exists")
    sys.exit(1)

start = time.clock()

for line in channel_file:
    channel = line.strip('\n').strip()
    target_fileName = "apk_" + channel + "-" + apk_version + "-" + get_time() + ".apk"  # 在这里调整渠道包的名称
    print("copyfile : " + target_fileName)
    copy_file(src_fileName, target_fileName)
    write_channel_to_apk(target_fileName, channel)

end = time.clock()

print("The function run time is : %.03f seconds" % (end - start))
