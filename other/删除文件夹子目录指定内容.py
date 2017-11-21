import os
import shutil

path = 'N:\\软件SDK等\\安卓代码2015年11月03日备份'


def deleteSub(p):
    for i in os.listdir(p):
        if i == 'res' or i == 'src':
            continue
        f = os.path.join(p, i)
        if os.path.isfile(f):
            os.remove(f)
        elif os.path.isdir(f):
            shutil.rmtree(f)


def deleteFolder():
    for sub in os.listdir(path):
        subPath = os.path.join(path, sub)
        if os.path.isdir(subPath):
            deleteSub(subPath)
            print('删除完成 --- ' + sub.title())
        else:
            print('不是目录 --- ' + sub.title())


deleteFolder()
# os.remove('N:\\软件SDK等\\安卓代码2015年11月03日备份\\内容提供者之短信备份\\.classpath')
