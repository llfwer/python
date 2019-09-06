#!/usr/bin/python
# -*- coding: UTF-8 -*-
import base64
import os

json1 = open('data.json', 'r', encoding='UTF-8')
jsonString = json1.read()
json1.close()

jsonString = jsonString.replace('"u":"images/"', '"u":""')

for root, dirs, files in os.walk('images'):
    for file in files:
        print(file)
        f = open(os.path.join(root, file), 'rb')  # 二进制方式打开图文件
        ls_f = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
        f.close()

        jsonString = jsonString.replace(file, 'data:image/png;base64,' + ls_f.decode('utf-8', 'ignore'))

json2 = open('data1.json', 'w', encoding='UTF-8')
json2.write(jsonString)
json2.close()
