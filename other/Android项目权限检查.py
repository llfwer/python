import os

from bs4 import BeautifulSoup

# 项目路径 动态改动
projectPath = 'E:/GNN' + '/'
# projectPath = 'H:/AndroidProjects/EyeShield' + '/'
# host主目录 as 缓存都是在此目录下 一般是死的，除非你的修改过主盘
USER_HOME = "C:/Users/ROWE"

path = projectPath + '.idea/libraries/'


class LibData:
    def __init__(self, name, path):
        self.name = name
        self.path = path


class PermissionData:
    def __init__(self, name, permissions):
        self.name = name
        self.permissions = permissions


# 获取文件名和路径
def getLibrariesList(path):
    f = os.walk(path)
    list = []
    for root, dirs, files in f:
        for i in files:
            p = root + i
            # print('路径：',p)
            # print('文件名：',i)
            try:
                s = open(p, 'r', encoding='utf-8')
            except:
                print("文件不存在：", p)
            content = s.read()
            soup = BeautifulSoup(content, 'html.parser')
            urls = soup.find_all('root')

            for l in urls:
                url = l.get('url')
                if not url:
                    continue
                if url.endswith("res"):
                    # print('文件名：', i)
                    # print('文件路径： ', url)
                    list.append(LibData(i, url.replace('/res', '/AndroidManifest.xml')))
                    break
            soup.clear()
    return list


# 获取含有权限的文件数据
def getHavePermissionList(mainPathList):
    list = []
    for item in mainPathList:
        if not item.path:
            continue
        else:
            l = item.path
            # print('处理前path: ',l)
            l = l.replace('file://$USER_HOME$', USER_HOME)
            l = l.replace('file://', "")
            l = l.replace('jar://$USER_HOME$', USER_HOME)
            l = l.replace('jar://', "")
            # print('处理后path: ', l)

            # print('\n\n打开文件名：', item.name)
            # print('打开路径：',l)
            try:
                file = open(l, 'r', encoding='utf-8')
            except:
                print("文件不存在：", l)
                continue

            content = file.read()
            file.close()
            # print(content)
            soup = BeautifulSoup(content, 'html.parser')
            ps = soup.find_all('uses-permission')
            if not ps:
                continue
            else:
                strArr = []
                for u in ps:
                    p = u.get('android:name')
                    strArr.append(p)
                    # print(p)
                list.append(PermissionData(item.name, strArr))
            soup.clear()
    return list


mainPathList = getLibrariesList(path)
print('---------发现第三方数：{}个'.format(len(mainPathList)))
list = getHavePermissionList(mainPathList)
print('---------含有权限的库数：{}个'.format(len(list)))

for m in list:
    print("\n")
    print('第三库名: ', m.name)
    print('第三库里含有的权限: ', m.permissions)
