import os.path
import re
import shutil


def clear_module(root):
    if not os.path.isdir(root):
        return

    for parent, dir_names, file_names in os.walk(root):

        # 删除文件夹
        for d in dir_names:

            if d == 'build' or d == '.cxx':
                p = parent + os.sep + d
                if os.path.isdir(p):
                    print(p)
                    shutil.rmtree(p)
            if d == 'libs':
                p = parent + os.sep + d
                if os.path.isdir(p) and not os.listdir(p):
                    print(p)
                    shutil.rmtree(p)

        # 删除文件
        for f in file_names:

            if f == '.gitignore':
                p = parent + os.sep + f
                if os.path.isfile(p):
                    print(p)
                    os.unlink(p)
            if re.match(r'(.*)\.iml', f) is not None:
                p = parent + os.sep + f
                if os.path.isfile(p):
                    print(p)
                    os.unlink(p)


def clear_project(root):
    if not os.path.isdir(root):
        return

    for parent, dir_names, file_names in os.walk(root):

        # 删除文件夹
        for d in dir_names:

            if d == '.gradle' or d == '.idea' or d == 'gradle':
                p = parent + os.sep + d
                if os.path.isdir(p):
                    print(p)
                    shutil.rmtree(p)
            else:
                p = parent + os.sep + d
                if os.path.isdir(p):
                    clear_module(p)

        # 删除文件
        for f in file_names:

            if f == '.gitignore' or f == 'gradlew' or f == 'gradlew.bat' or f == 'local.properties' or f == 'settings.gradle':
                p = parent + os.sep + f
                if os.path.isfile(p):
                    print(p)
                    os.unlink(p)
            if re.match(r'(.*)\.iml', f) is not None:
                p = parent + os.sep + f
                if os.path.isfile(p):
                    print(p)
                    os.unlink(p)


if __name__ == '__main__':
    clear_project(r"E:\Demo9")
