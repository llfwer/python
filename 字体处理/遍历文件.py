#!/usr/bin/python

import glob
import sys

# glob 文件名模式匹配

# 测试使用
sys.argv = ['遍历文件.py', '.\data\png\\']

if len(sys.argv) < 2:
    print("Usage : 遍历文件.py strike-prefix...")
    sys.exit(1)

prefix = sys.argv[1]
del sys.argv

match = "%s*.png" % prefix

print("Looking for images matching '%s'." % match)

files = {}

for file in glob.glob(match):
    u = int(file[len(prefix):-4], 16)
    files[u] = file

if not files:
    raise Exception("No image files found in '%s'." % match)
else:
    print(files)
