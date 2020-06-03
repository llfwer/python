import base64
import os


def find_json_file(path):
    if not os.path.isdir(path):
        return None

    dirs = os.listdir(path)

    for item in dirs:
        if item == 'data.json':
            return os.path.join(path, item)
    return None


def replace_json(path):
    if not os.path.isfile(path):
        return

    json1 = open(path, 'r', encoding='UTF-8')
    json_text = json1.read()
    json1.close()

    json_text = json_text.replace('"u":"images/"', '"u":""')

    (dir_path, file_name) = os.path.split(path)

    for root, dirs, files in os.walk(os.path.join(dir_path, 'images')):
        for file in files:
            print(file)
            f = open(os.path.join(root, file), 'rb')  # 二进制方式打开图文件
            ls_f = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
            f.close()

            json_text = json_text.replace(file, 'data:image/png;base64,' + ls_f.decode('utf-8', 'ignore'))

    json2 = open(os.path.join(dir_path, 'data1.json'), 'w', encoding='UTF-8')
    json2.write(json_text)
    json2.close()


def check_path(path):
    dirs = os.listdir(path)

    for item in dirs:
        file = find_json_file(os.path.join(path, item))

        if file is not None:
            replace_json(file)


def main():
    check_path(r"C:\Users\ROWE\Desktop\hello")


if __name__ == '__main__':
    main()
